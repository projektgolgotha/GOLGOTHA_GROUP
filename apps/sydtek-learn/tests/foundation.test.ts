import { test } from "node:test";
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { shopifyConnectionStatus } from "../app/lib/config.server.ts";
import { HRM_PLAYLIST_ID, parseCourseInventory, playlistEmbedUrl } from "../app/lib/course.ts";

test("Shopify stays disconnected unless explicitly enabled", () => {
  const state = shopifyConnectionStatus({ SHOPIFY_API_KEY: "test", SHOPIFY_API_SECRET: "test", SHOPIFY_APP_URL: "https://example.org" });
  assert.equal(state.state, "disconnected");
});
test("missing credentials fail closed and no secret values are exposed", () => {
  const state = shopifyConnectionStatus({ SHOPIFY_CONNECTION: "enabled", SHOPIFY_API_SECRET: "do-not-return-me" });
  assert.equal(state.state, "disconnected");
  assert.ok(!JSON.stringify(state).includes("do-not-return-me"));
});
test("configuration alone never claims an authenticated connection", () => {
  assert.equal(shopifyConnectionStatus({ SHOPIFY_CONNECTION: "enabled", SHOPIFY_API_KEY: "test", SHOPIFY_API_SECRET: "test", SHOPIFY_APP_URL: "https://example.org" }).state, "configured_unverified");
});
test("production rejects an insecure app URL", () => {
  assert.equal(shopifyConnectionStatus({ NODE_ENV: "production", SHOPIFY_CONNECTION: "enabled", SHOPIFY_API_KEY: "test", SHOPIFY_API_SECRET: "test", SHOPIFY_APP_URL: "http://localhost" }).state, "disconnected");
});
test("real source inventory retains playlist order and identifies the duplicate", async () => {
  const data = JSON.parse(await readFile(new URL("../../../content/sydtek-learn/courses/hrm-101/course.json", import.meta.url), "utf8"));
  const inventory = parseCourseInventory(data);
  assert.equal(inventory.entries.length, 48);
  assert.equal(inventory.uniqueVideoCount, 47);
  assert.equal(inventory.entries[42].duplicateOf, 42);
  assert.equal(inventory.entries[42].videoId, inventory.entries[41].videoId);
});
test("untrusted playback identifiers and wrong playlists are rejected", () => {
  assert.throws(() => playlistEmbedUrl("https://evil.example"));
  assert.throws(() => parseCourseInventory({ course: { course_id: "HRM-101", source_playlist_id: "wrong" }, entries: [] }));
  assert.ok(playlistEmbedUrl().includes(HRM_PLAYLIST_ID));
});
