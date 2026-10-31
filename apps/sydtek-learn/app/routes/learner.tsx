import { Link } from "react-router";
import { SiteShell } from "../components/site-shell";
export const meta = () => [{ title: "My learning | SydTek Learn" }];
export default function Learner() {
  return <SiteShell><section className="section workspace"><p className="eyebrow">LEARNER WORKSPACE</p><h1>A place for<br /><em>your next chapter.</em></h1><p className="hero-copy">Explore the public course library today. Individual learner accounts and saved learning records are being built.</p><div className="notice"><h2>Available now</h2><p>HRM-101’s public source lessons are open to everyone.</p><Link className="button" to="/learn/hrm-101">Open HRM-101</Link></div><div className="workspace-grid"><article><h3>Progress</h3><p>Not active. No viewing or completion history is being saved.</p></article><article><h3>Assessments</h3><p>Not active. No scores or grades have been assigned.</p></article><article><h3>Credentials</h3><p>Not active. No certificates or academic credit are issued by this foundation.</p></article></div></section></SiteShell>;
}
