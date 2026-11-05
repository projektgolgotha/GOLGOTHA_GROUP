# Upstream corrections — prepared, not yet imported

November 5, 2026. The connected GitHub account can write `projektgolgotha/GOLGOTHA_GROUP`; it has read-only access to the original Scholars and Seminary repositories. These patches are prepared against the exact reviewed revisions below. No upstream modification is claimed.

| Repository | Reviewed revision | Patch |
|---|---|---|
| GoldstonianConcordanceBible/SydTek_Scholars_Canon | 757d2e5176ab9eaede98082adb1b73bf68c7176a | [Scholars correction patch](patches/scholars-status-2026-11-05.patch) |
| GoldstonianConcordanceBible/SydTek-Seminary | c3ebe5474ccd45aa82242d43fe0a3e37c673e44b | [Seminary correction patch](patches/seminary-status-2026-11-05.patch) |

## Corrections prepared

1. Scholars README: remove unsupported active-registration/nationwide-enrollment/deployed-dashboard claims; add the dated register and point navigation to existing combined filenames.
2. Scholars accreditation roadmap: replace unsupported completed institutional milestones and guaranteed recognition language with evidence gates; update Cognia terminology; label hours and credits as unreconciled planning assumptions.
3. Preserve original legal, state, hours and transfer drafts with prominent historical-planning notices pointing to the current register; no legal fact, policy adoption or credit authority is manufactured.
4. Seminary: preserve the misfiled minister-registry text in a clearly labeled draft file and replace STATEMENT_OF_FAITH.md with an unresolved/adoption-required notice. No theology is invented or adopted. ORDINATION_FRAMEWORK.md remains an unresolved missing reference.
5. Link the October 31 release in this audit repository and distinguish the diploma and noncredit survey code namespaces without renaming live content.

## Correct source navigation

- [Substantive Scholars source](https://github.com/GoldstonianConcordanceBible/SydTek_Scholars_Canon); the older `sydtek-scholars-canon-` repository is only a small pointer collection.
- [Transfer and curriculum combined source](https://github.com/GoldstonianConcordanceBible/SydTek_Scholars_Canon/blob/757d2e5176ab9eaede98082adb1b73bf68c7176a/TRANSFER_CREDITS.md%20%2B%20CURRICULUM_FRAMEWORK.md)
- [Governance and hours combined source](https://github.com/GoldstonianConcordanceBible/SydTek_Scholars_Canon/blob/757d2e5176ab9eaede98082adb1b73bf68c7176a/GOVERNANCE.md%20%2B%20SEAT_TIME_MODEL.md)
- [Shopify and dashboard combined source](https://github.com/GoldstonianConcordanceBible/SydTek_Scholars_Canon/blob/757d2e5176ab9eaede98082adb1b73bf68c7176a/SHOPIFY_INTEGRATION.md%20%2B%20PARENT_DASHBOARD_SPEC.md)
- [Seminary latest locked release](../sydtek-seminary/LATEST_RELEASE.md). The `accreditation/` source is inside the compressed source bundle, not a separately browsable release directory.

## Import procedure for a maintainer with write access

Fetch the target repository's current branch and compare it with the reviewed revision. Run `git apply --check` on the relevant patch before applying; if the branch changed, reconcile the patch rather than overwriting current files. Review the resulting diff, commit, and record the upstream commit URL here. The patch was locally application-checked against the exact reviewed file contents, not applied to the upstream branch.

An imported documentation correction will not resolve official formation/registration, enrollment authority, board adoption, actual study hours, transfer acceptance or accreditation. Those need their own sources and decisions.
