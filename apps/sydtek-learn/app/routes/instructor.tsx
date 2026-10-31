import { Link, useLoaderData } from "react-router";
import { SiteShell } from "../components/site-shell";
import { shopifyConnectionStatus } from "../lib/config.server";
export const loader = () => ({ shopify: shopifyConnectionStatus() });
export const meta = () => [{ title: "For instructors | SydTek Learn" }];
export default function Instructor() {
  const { shopify } = useLoaderData<typeof loader>();
  return <SiteShell><section className="section workspace"><p className="eyebrow">INSTRUCTOR WORKSPACE</p><h1>Teach with<br /><em>clear evidence.</em></h1><p className="hero-copy">The first course source inventory is prepared. Course publishing, assessments, and learner administration will be added in subsequent releases.</p><div className="notice"><h2>{shopify.state === "disconnected" ? "Shopify is disconnected" : "Shopify configuration awaits verification"}</h2><p>This public page provides no administrative access. The protected workspace requires Shopify’s authenticated admin session.</p>{shopify.state !== "disconnected" && <Link className="button" to="/auth/login">Continue to Shopify sign-in</Link>}</div><div className="workspace-grid"><article><h3>Source material</h3><p>Review HRM-101’s public playlist and original video links.</p><Link to="/learn/hrm-101">View the source playlist →</Link></article><article><h3>Publishing</h3><p>Not active. No draft is represented as an approved curriculum.</p></article><article><h3>Evidence review</h3><p>Not active. Learner submissions and grading tools are not connected.</p></article></div></section></SiteShell>;
}
