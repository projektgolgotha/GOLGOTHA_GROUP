import prisma from "../db.server";
import { shopifyConnectionStatus } from "../lib/config.server";
export async function loader() {
  let database: "ready" | "not_ready" = "not_ready";
  try { await prisma.session.findFirst({ select: { id: true } }); database = "ready"; } catch { /* Never expose raw connection errors or paths. */ }
  return Response.json({ service: "sydtek-learn", version: "0.1.0", application: "running", database: { state: database, check: "session_schema_query" }, shopify: shopifyConnectionStatus(), learning: { publicLessons: "available", savedProgress: "not_implemented", credentials: "not_implemented" } }, { status: database === "ready" ? 200 : 503, headers: { "Cache-Control": "no-store" } });
}
