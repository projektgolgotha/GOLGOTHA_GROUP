# SydTek Seminary website delivery

The page source uses the canonical registry, course manifest, and reviewed source map in `content/sydtek-seminary`. The generator never equates a playlist title with approved academic coverage. Units that require exact-text review, or lack an identified direct source, remain visibly marked for development.

## Files

- `build_site.py`: deterministic generator using Python's standard library.
- `site-config.json`: destinations and verified Skool publication flag.
- `page-candidate.html`: complete Seminary page body for the existing `/pages/sydtek-seminary` route.
- `hub-feature.html`: one additional Seminary feature following HRM-101 in the current education hub.
- `hub-candidate.html`: current `/pages/sydtek` body plus the bounded feature addition.
- `preview.html`: standalone local preview of the Seminary page.
- `preparation-checks.json`: generated inventory counts, preservation checks, and body hashes.
- `source-qa.json`: independent review of registry coverage, source links, and the bounded hub change.
- `rollback/`: prior public page bodies, page metadata, menu snapshot, and theme inventory.
- `publication/`: actual published read-back and browser evidence, when publication is completed.

Regenerate with `python website/sydtek-seminary/build_site.py` from the repository root. Generation does not publish. The publication workflow validates the Admin GraphQL operation, rereads current page versions, updates only the authorized page bodies/title/template fields, then reads the result back and performs public-browser checks.

## Change scope

The Seminary page replaces generic enrollment promotions with its own study pathway, orientation, 81-entry course map, teaching method, institutional-source links, program-status section, and voluntary-support link. The existing source repositories and evidence library remain linked. Historical content is recoverable in the rollback snapshot.

The existing `ew-learning` template is present with identical content in the current live theme and the newer maintenance draft. Reusing that page template avoids duplicate page titles. No theme file is written or theme published. The current Education navigation already contains a Seminary link, so no navigation mutation is needed.

The hub addition preserves the original page body exactly around the inserted feature. HRM-101 stays the first featured course. Other site pages and unrelated navigation branches are outside this change.

## Accessibility and availability

The course map is plain HTML with native `details`/`summary` controls and visible focus styles. It does not require JavaScript, external fonts, or tracking code. Layout uses fluid widths and a small-screen breakpoint. A source/HTML check does not establish rendered mobile accessibility; browser checks state their actual environment and remaining limits.

Support links point to the existing information page. This release does not configure a donation checkout. The public videos and study guides are learning resources; private student records, automated grading, and credential issuance are not implemented by this page.
