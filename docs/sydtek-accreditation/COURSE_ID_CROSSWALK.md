# Seminary course-ID crosswalk — documentation convention

Prepared November 5, 2026. This introduces a disambiguating reference convention for evidence indexing; it does not rename published Skool pages, adopt academic credit or approve a program.

| Source context | Existing local code | Source meaning | Unambiguous register key |
|---|---|---|---|
| Proposed 48-SH diploma | SEM-101 | Canon Foundations | DIP48-v0.2.0::SEM-101 |
| Proposed 48-SH diploma | SEM-102 | Interpretation | DIP48-v0.2.0::SEM-102 |
| Noncredit Ethiopian survey | SEM-101 | Torah / Beginnings | ECS-NC-v0.2.0::SEM-101 |
| Noncredit Ethiopian survey | SEM-102 | History | ECS-NC-v0.2.0::SEM-102 |

These rows are the collisions identified in the review, not an exhaustive course equivalency map. Preserve source titles and local IDs. Store `program_id`, `source_version`, `local_course_id`, `delivery_version` and `credential_status` separately; never merge records solely on SEM-101 or SEM-102. No transfer/equivalency between the two programs is inferred.

Sources: [locked release](../sydtek-seminary/releases/2026-10-31-accreditation-skool-v0.2.0/README.md), including its proposed diploma source inside the archive and the separate course-build files. Institutional review must confirm the full catalog and authorize any future migration.
