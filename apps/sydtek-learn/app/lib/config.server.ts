type Environment = Record<string, string | undefined>;
export function shopifyConnectionStatus(env: Environment = process.env) {
  const required = ["SHOPIFY_API_KEY", "SHOPIFY_API_SECRET", "SHOPIFY_APP_URL"] as const;
  const missing = required.filter((name) => !env[name]?.trim());
  if (env.SHOPIFY_CONNECTION !== "enabled") return { state: "disconnected" as const, reason: "not_enabled", missing: [] as string[] };
  if (missing.length) return { state: "disconnected" as const, reason: "configuration_missing", missing: [...missing] };
  try {
    const url = new URL(env.SHOPIFY_APP_URL!);
    if (url.protocol !== "https:" && !(env.NODE_ENV !== "production" && url.hostname === "localhost")) return { state: "disconnected" as const, reason: "invalid_app_url", missing: [] as string[] };
  } catch { return { state: "disconnected" as const, reason: "invalid_app_url", missing: [] as string[] }; }
  return { state: "configured_unverified" as const, reason: "authentication_required", missing: [] as string[] };
}
