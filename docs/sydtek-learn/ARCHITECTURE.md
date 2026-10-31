# SydTek Learn architecture

## Foundation

Start with the current official Shopify React Router application pattern and maintained Shopify authentication/session libraries. Record the actual upstream version and dependencies in the application README and lockfile. The application is separate from ENOCH WORLD's Shopify theme. Public course browsing must not require Shopify merchant authentication or a donation.

## Boundaries

| Area | Responsibility |
|---|---|
| Identity and organizations | Verified user identity, isolated organization membership, and role scope |
| Catalog | Versioned programs, courses, lessons, source references, and publication state |
| Enrollment | Learner identity and access grants independent of purchaser identity |
| Assessment and evidence | Server-side attempts, grading decisions, outcome evidence, and completion records |
| Commerce | Verified paid offers for merchants that enable them; separate merchant app billing |
| Voluntary support | Donor/recipient/payment records independent of learning access and academic results |
| Integrations | Shopify, approved media sources, optional AI drafting and Roblox learning events |

These are ownership boundaries for successive chunks, not a claim that every service is implemented. PostgreSQL is the intended application data store; identify and document session storage separately from academic records.

## HRM-101 source handling

The source manifest is authoritative for captured playlist metadata. Each canonical activity has a stable identity independent of its playlist position. A repeated video may have multiple source references but should not earn duplicate completion. Proposed outcomes require lesson review and instructor-approved assessments before publication as an assessed offering.

## Website integration

Use the current shared Shopify master and existing `/pages/sydtek` education route. The prepared scoped fragment belongs at the top of that page; the Education menu's first child becomes SydTek Learn. `website/sydtek-learn` contains the exact prepared content, observed link inventory, change specification, and read-only checks. Authenticated source reconciliation, actual mutation, visual verification, and public publication remain distinct steps.

## Voluntary support

The source course remains available without payment. Contributions use a separately configured hosted processor and verified events. No client redirect, pledge, or test event is proof of settled funds. Donor data stays private and must not affect grades, credentials, or learner visibility. The existing support information page can be linked before payment collection is configured.

## Release evidence

Report what actually ran: installation, local startup, process health, database readiness, build/type checks, integration checks, and deployment. Record unavailable checks as blocked or not run. Preserve previous code and require fresh source fingerprints before updating shared external resources.
