import "@shopify/shopify-app-react-router/adapters/node";
import { ApiVersion, AppDistribution, shopifyApp } from "@shopify/shopify-app-react-router/server";
import { PrismaSessionStorage } from "@shopify/shopify-app-session-storage-prisma";
import prisma from "./db.server";
import { shopifyConnectionStatus } from "./lib/config.server";

function createShopifyApp() {
  return shopifyApp({
    apiKey: process.env.SHOPIFY_API_KEY!,
    apiSecretKey: process.env.SHOPIFY_API_SECRET!,
    apiVersion: ApiVersion.October26,
    scopes: process.env.SCOPES?.split(",").filter(Boolean),
    appUrl: process.env.SHOPIFY_APP_URL!,
    authPathPrefix: "/auth",
    sessionStorage: new PrismaSessionStorage(prisma),
    distribution: AppDistribution.AppStore,
    future: { expiringOfflineAccessTokens: true },
    ...(process.env.SHOP_CUSTOM_DOMAIN ? { customShopDomains: [process.env.SHOP_CUSTOM_DOMAIN] } : {}),
  });
}
let instance: ReturnType<typeof createShopifyApp> | undefined;
export function getShopify() {
  if (shopifyConnectionStatus().state === "disconnected") {
    throw new Response("Shopify is disconnected. Public lessons remain available at /learn/hrm-101.", { status: 503, headers: { "Cache-Control": "no-store" } });
  }
  instance ??= createShopifyApp();
  return instance;
}
// Preserve Shopify's maintained authentication and Prisma session implementation.
// No local/mock admin session is substituted when configuration is absent.
export const authenticate = {
  admin: (request: Request) => getShopify().authenticate.admin(request),
  webhook: (request: Request) => getShopify().authenticate.webhook(request),
};
export const login = (request: Request) => getShopify().login(request);
export const apiVersion = ApiVersion.October26;
export function addDocumentResponseHeaders(request: Request, headers: Headers) {
  headers.set("X-Content-Type-Options", "nosniff");
  if (shopifyConnectionStatus().state !== "disconnected") getShopify().addDocumentResponseHeaders(request, headers);
}
