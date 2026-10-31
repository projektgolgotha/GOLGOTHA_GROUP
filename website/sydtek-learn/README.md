# SydTek Learn education section

Prepared for the owner's request to put SydTek Learn at the top of Education and organize the education offerings beneath it. HRM-101 is the first featured course, with voluntary support separate from public learning access.

## Current state

The Education hub and shared navigation are published at https://enochworld.com/pages/sydtek#sydtek-learn. A working authenticated Shopify connection was found after an earlier connection returned `Authentication required`. The update prepended only the scoped hub to the current page body and regrouped Education beneath SydTek Learn. All 22 existing Education destinations and all six unrelated menu branches are preserved. No theme, checkout, or payment provider was changed.

Authenticated inventory and public rendering confirmed MAIN theme `189733863535`, `ENOCH WORLD — MASTER Wakaboomee Fundraising`. The newer `189815685231`, `ENOCH WORLD — MASTER Maintenance Oct 30`, remains unpublished. Both read the same page body and shared `enoch-primary` menu through the existing `ew-learning` template and institutional navigation renderer. The update carries forward with the draft without a theme switch. These identities are recorded observations, not evergreen edit targets or an instruction to publish any draft.

## Contents

- `hub-fragment.html`: scoped, responsive section for the top of the existing `/pages/sydtek` page; includes HRM-101, every distinct destination captured in the current Education menu, and voluntary support.
- `preview.html`: local full-document review wrapper for that fragment. It is not a deployed ENOCH WORLD page.
- `navigation-baseline.json`: 27 observed Education links representing 22 distinct destinations, plus public source hash and theme identity.
- `navigation-proposal.json`: grouping specification, preserving existing destinations and defining the first item under Education.
- `deployment-plan.json`: applied target selectors, supported operations, publication checks, and rollback requirements, updated from authenticated resource IDs.
- `rollback/`: the actual page body, page metadata, and complete affected menu read before publication.
- `publication/`: submitted candidates, officially validated GraphQL operations, published read-back, and verification evidence.

## Procedure for a subsequent update

1. Fresh-read store identity, actual MAIN, newer drafts, canonical page handle `sydtek`, full Education menu, shared renderer, and relevant page templates. Verify which integrated master is owner-approved. Preserve the shared header, footer, music controls, directory, Sports, SydTek Saints, Cricket, and other trees.
2. Back up the actual page body/title/template and complete affected menu with hashes. Do not use rendered storefront HTML as an Admin page-body backup.
3. Insert or replace only the section with `id="sydtek-learn"` at the top of the existing SydTek page body; preserve all other content and the shared template. Do not create a competing education overview route. The canonical hub link is `/pages/sydtek#sydtek-learn`.
4. Add `SydTek Learn` first under Education. Group every current education destination beneath that hub. The proposed menu uses a flat set of leaves beneath the new parent to fit a supported menu depth; the page groups them into clear categories. Preserve target IDs and unrelated branches. Do not blindly replace a menu from the public-link snapshot.
5. Run official schema validation for generated operations, using the connected API's actual pinned version. Use the narrow required page/menu permissions. Theme-file writes through the Shopify connector are allowed only on unpublished themes; theme publication must follow the supported owner action. Do not bypass these restrictions.
6. Verify desktop, mobile, keyboard access, links, retained education destinations, and Sports/Cricket on the actual shared renderer. Check both native and alternate/query route families affected by navigation. Confirm publication separately through a fresh public request outside preview mode.
7. Record actual resource IDs, source and resulting hashes, rollback references, successful writes, and any unavailable checks in the release receipt.

## Contribution behavior

The support CTA links to the existing support-information page. It does not claim that a hosted donation checkout is active. Configure the verified receiving entity and provider before accepting funds. Contributions must remain optional and must not affect learning access, assessment, grades, or credentials. No token, wallet, or currency-conversion integration is part of this build.

## Course evidence

The source inventory is `content/sydtek-learn/courses/hrm-101/course.json`. The playlist has 48 entries and 47 distinct video IDs. Its duplicate, URL-like title, and module-order findings remain in the source record. The public page does not promise current LMS enrollment, automated credentials, credit transfer, accreditation, or independently verified university endorsement.
