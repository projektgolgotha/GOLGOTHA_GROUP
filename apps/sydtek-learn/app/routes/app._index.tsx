import type { LoaderFunctionArgs } from "react-router";
import { authenticate } from "../shopify.server";
export const loader = async ({ request }: LoaderFunctionArgs) => {
  await authenticate.admin(request);
  return null;
};
export default function InstructorAdmin() {
  return <s-page heading="SydTek Learn"><s-section heading="Instructor foundation"><s-paragraph>Your Shopify admin session has been verified. Source lessons are available in the public learning library. Course publishing, learner administration, assessments, and credentials are not active in this release.</s-paragraph><s-link href="/learn/hrm-101" target="_blank">Open HRM-101</s-link></s-section></s-page>;
}
