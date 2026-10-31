# SydTek Learn LMS Build Chunks

Build SydTek Learn in [projektgolgotha/GOLGOTHA_GROUP](https://github.com/projektgolgotha/GOLGOTHA_GROUP), beginning with HRM-101 and a voluntary donation model. Put SydTek Learn first in ENOCH WORLD's Education section and organize the existing education offerings beneath it. The first learning milestone is an instructor publishing a course that a learner can complete with accurate progress and an exportable record. These are implementation instructions; actual execution evidence belongs in the repository build ledger.

# Starting decisions

| Decision | Current choice |
|---|---|
| Product name | SydTek Learn |
| Repository | projektgolgotha/GOLGOTHA_GROUP |
| Application location | apps/sydtek-learn |
| Documentation and course sources | docs/sydtek-learn and content/sydtek-learn/courses |
| Product structure | Reusable learning service with isolated organizations and configurable branding |
| Website organization | SydTek Learn first in Education; existing education offerings grouped beneath it |
| First course | HRM-101 — Introduction to Human Resource Management — SydTek University Microcredential |
| Course source | Supplied YouTube playlist and author-owned material; reviewed source mappings before assessed publication |
| Support model | Voluntary donations, independent of learning access and academic decisions |
| New-project stack | TypeScript and the current official Shopify React Router template; PostgreSQL for application data |
| Existing project | Preserve its instructions and root README/license; verify new concurrent work before editing |
| Course credentials | Completion or assessed-skill credentials with explicit criteria and accurately stated educational status |
| School access | Free and sponsored enrollment supported independently of payment |

# Inputs needed at execution

| Input | Current position and next use |
|---|---|
| Repository | Resolved: projektgolgotha/GOLGOTHA_GROUP; first implementation belongs in apps/sydtek-learn |
| First course | Resolved: supplied HRM-101 playlist; complete source review and assessment mapping still needed |
| Shopify connection | Required for authorized page/menu changes and development-store integration |
| Donation destination | Configure verified receiving entity, provider/account, currency, and receipt/support details before collection |
| Hosting/domain/budget | Needed for application deployment and paid services |
| School/family notices and pilot owner | Needed for actual child/school enrollment |
| Roblox experience/access | Needed only for the optional learning-event integration |

These inputs can be supplied when the relevant chunk is executed. Credentials belong in the supported connection or secret-management process.

# How to run the chunks

Give the coding agent one chunk at a time in the same project. Read the completed chunk receipt before starting its dependents. Shared schema, authentication, and enrollment changes need a single integration owner; independent UI and documentation work can run in parallel after contracts are stable.

Every chunk must preserve the repository's applicable instructions and existing work. Derive organization and user access from trusted server-side context. Keep synthetic fixtures separate from real learners. Use persistent server-side records for progress and grades. Implement only the stated scope, and verify material behavior rather than merely checking that files exist.

Each completed chunk must report: the actual repository and branch; changed files; working behavior; meaningful checks and their results; unresolved integration or access needs; and the exact next eligible chunk. Update docs/sydtek-learn/BUILD_LEDGER.md using Not started, In progress, Blocked, or Verified. A stub, screenshot, local fixture, or successful compilation is not proof of a live external integration.

# Build sequence

| Chunk | Outcome | Dependencies |
|---|---|---|
| STL-001 | Project foundation | None |
| STL-002 | Canonical data model | STL-001 |
| STL-003 | Authentication and permissions | STL-002 |
| STL-004 | Course authoring and publication | STL-003 |
| STL-005 | Enrollment and learner portal | STL-004 |
| STL-006 | Progress and assessments | STL-005 |
| STL-007 | Outcomes and credentials | STL-006 |
| STL-008 | Shopify course purchase integration | STL-003, STL-005, STL-007 |
| STL-009 | Merchant onboarding billing and usage | STL-008 |
| STL-010 | Reports exports and data lifecycle | STL-007, STL-008 |
| STL-011 | Family accounts and school cohorts | STL-003, STL-005, STL-010 |
| STL-012 | Academic assessment and progression | STL-007, STL-010, STL-011 |
| STL-013 | Source to course AI workflow | STL-004, STL-007, STL-009 |
| STL-014 | Scheduled content and communities | STL-005, STL-009; STL-011 for minors |
| STL-015 | Roblox learning integration | STL-006, STL-007; STL-011 for minors |
| STL-017 | Voluntary donations and support records | STL-002, STL-003, STL-010; verified payment connection for live collection |
| STL-018 | Education hub and HRM101 course presentation | Verified current site/navigation and course sources; STL-004 for dynamic catalog integration |
| STL-016 | Pilot verification and release preparation | Core plus every enabled optional module |

The adult LMS release can proceed to STL-016 after the core learning and administration chunks are verified. The public education hub in STL-018 can be prepared independently. Voluntary collection in STL-017 is optional and must not block learning. Family and school releases additionally require the applicable permission and academic workflows.

# Course source and voluntary support

**First course:** [HRM-101 | Introduction to Human Resource Management | SydTek University Microcredential](https://www.youtube.com/playlist?list=PLtS4zDr2sp3S1ptnw-a0Q030421d6jHd0). The retrieved playlist contains 48 entries representing 47 unique video IDs; entries 42 and 43 repeat the same source video. Preserve source order and use a distinct canonical learning-activity map.

| Source fact | Treatment |
|---|---|
| Course title and playlist | Supplied by the creator; metadata retrieved from the public playlist |
| Authorship | Dr. Justin Goldston, as supplied by the creator |
| LearnDay Canada development and Canadian university use | Creator-reported provenance; retain attribution and request named adoption evidence only when making institution-specific claims |
| Durations and source titles | Record from the actual playlist; a duplicate must not create additional completion credit |
| Learning outcomes and assessments | Author/reviewer-approved design required before assessed publication |
| Voluntary contributions | Support learning development; separate from access, grades, and credentials |

Use the creator's supplied material to build the reference course. Keep source metadata, proposed instructional design, completed assessments, and earned credentials distinct. Course-description statements about credit equivalence or alignment are publisher statements until their underlying academic authority is verified.

**Support experience:** a visitor can start HRM-101 directly and choose whether to support the learning mission. Reuse the existing [SydTek support information](https://enochworld.com/pages/sydtek-support) while the actual receiving entity and hosted collection method are configured. A canceled or declined contribution returns the visitor to learning.

**Collection configuration:** receiving entity, approved provider/account, currency, optional amount choices or bounds, campaign purpose, acknowledgment/receipt details, and support/refund terms. Do not preselect a contribution or invent a live payment destination. These details do not block the public course.

Donations have no effect on learner assessment, earned grades, or credential decisions. Keep donor data private, use verified processor records for financial totals, and describe acknowledgments accurately. The earlier token discount design is superseded by this donation model.

# Ready to paste build instructions

## STL-001 Project foundation

**Dependencies:** None

```text
STL-001 — PROJECT FOUNDATION
Project: SydTek Learn, an original LMS for SydTek and independent Shopify merchants.

GOAL
Create a runnable development foundation that preserves existing work and can support multiple isolated organizations.

FIRST
Target the authorized repository https://github.com/projektgolgotha/GOLGOTHA_GROUP. Place application code in apps/sydtek-learn, documentation in docs/sydtek-learn, and course manifests in content/sydtek-learn/courses. Preserve the root README and LICENSE. Inspect the actual repository, applicable AGENTS.md files, branch, uncommitted changes, package manager, authentication, database, and existing tests. Reuse an existing suitable application. The repository initially contained only README.md and LICENSE; freshly verify the current branch before changing it. Keep this separate from existing Roblox projects and live Shopify theme code.

IMPLEMENT
1. Use the current official Shopify React Router template for a new Shopify app and TypeScript for new application code. Preserve a suitable existing stack. Record the actual dependency versions and lockfile.
2. Use PostgreSQL for new application data unless an existing compatible database is already established. Document the official template's session-storage choice separately. Test production-critical constraints on the intended production database.
3. Establish modules for identity, organizations, catalog, enrollment, assessment, evidence, commerce, and integrations. Do not create empty success responses that imply an integration works.
4. Add development configuration, an environment-variable example with names only, startup instructions, and a health endpoint that distinguishes process health from database readiness.
5. Add a basic instructor shell and learner shell with configurable organization branding. Use clear empty states for unfinished features.
6. Create docs/sydtek-learn/BUILD_CONTEXT.md, docs/sydtek-learn/ARCHITECTURE.md, and docs/sydtek-learn/BUILD_LEDGER.md. Record purchaser-versus-learner separation, tenant isolation, published course versions, separate merchant billing, and voluntary donations independent of learning access. HRM-101 is the first course. Do not add token or wallet dependencies.
7. If Shopify authorization is unavailable, continue independent local work and mark the adapter Unconnected. Development authentication must be explicitly local-only and fail closed in production.

VERIFY
The local app starts using documented commands. Existing work is preserved. Missing configuration is reported clearly. The architecture and ledger match the actual code. Do not register a production app, activate paid services, or publish a live site in this chunk.

RETURN
Repository and branch, changed files, commands/results, local run instructions, unresolved prerequisites, and whether STL-002 is ready.
```

## STL-002 Canonical data model

**Dependencies:** STL-001

```text
STL-002 — CANONICAL DATA MODEL
Dependency: STL-001. Continue the same project and read docs/sydtek-learn/BUILD_CONTEXT.md.

GOAL
Create persistent identities and learning records that can support adults, families, schools, and independent merchants.

IMPLEMENT
1. Add organization, user, organization membership/role, learner profile, purchaser mapping, guardian relationship, school assignment, and Shopify installation records.
2. Add program, course, published course version, lesson/activity version, assessment version, outcome, enrollment, access grant, attempt, evidence reference, completion decision, and credential records.
3. Keep learner IDs independent of email, Shopify customer IDs, and Roblox IDs. A purchaser can fund several learners; a learner can have multiple access grants.
4. Scope private records and relationships to an organization. Use database constraints, including tenant-aware foreign keys where appropriate, to prevent cross-organization relationships.
5. Model access grants separately from enrollment history. Record grant source, validity dates, status, and a unique source key.
6. Model privacy requests, retention decisions, webhook receipt/processing state, and audit events. Keep personal submissions in access-controlled, deletable storage; do not embed sensitive content in permanent audit messages.
7. Reserve tenant-scoped records for voluntary support campaigns, verified recipients, processor transactions, donation receipts, refunds, and restricted-purpose allocations where applicable. Keep donors separate from learners, and keep donation state separate from grades, credentials, and free access grants. No token identities, wallet links, or token quotes are required.
8. Create repeatable migrations and synthetic fixtures for SydTek Demo and an unrelated Demo Academy. Include one payer, two independent adult learners, and draft course placeholders.

VERIFY
Migrations succeed against the intended database. Cross-tenant relationships fail. Re-seeding is safe. One payer can be associated with two learners without combining their progress. No real children's data is used.

RETURN
Entity relationship summary, migration changes, meaningful constraint-check results, and next chunk.
```

## STL-003 Authentication and permissions

**Dependencies:** STL-002

```text
STL-003 — AUTHENTICATION AND PERMISSIONS
Dependency: STL-002. Preserve the existing authentication implementation.

GOAL
Enforce organization and learner permissions at every protected server boundary.

IMPLEMENT
1. Reuse maintained Shopify authentication/session libraries for merchant installation context when connected. Implement learner authentication through the project's chosen supported identity mechanism.
2. Define organization owner, administrator, course author, instructor, purchaser, learner, and scoped guardian permissions. Guardian relationships remain unverified until the later family workflow verifies them.
3. Derive organization membership and permissions from trusted server-side state. A request parameter naming a shop, organization, role, or learner is never sufficient authorization.
4. Protect reads, writes, exports, downloads, background jobs, and signed-media link creation. Apply equivalent checks through all entry points.
5. Keep development fixtures and mock identities clearly separated. Production must reject mock configuration and missing authentication.
6. Implement session revocation and installation-disabled checks without exposing secrets in logs.

VERIFY
With two synthetic organizations, test cross-tenant course reads, learner reads, writes, exports, and file access. Test another learner's attempt ID and an unverified guardian relationship. Deny each unauthorized request. Verify production cannot activate a seeded administrator or mock login.

RETURN
Permission matrix, exact negative checks/results, and any identity-provider prerequisite.
```

## STL-004 Course authoring and publication

**Dependencies:** STL-003

```text
STL-004 — COURSE AUTHORING AND PUBLICATION
Dependency: STL-003.

GOAL
Let an authorized instructor create a course and publish a stable version.

IMPLEMENT
1. Add a course editor with sections, ordered lessons, text, approved external media, downloadable resource references, objectives, and assessment definitions.
2. Record source title, source location, owner/permission status, and source version or capture date when applicable. Mark incomplete source material and unfinished lessons clearly.
3. Add draft, review-ready, published, and retired states. Validate required content before publication.
4. Publish a version snapshot that preserves lessons, assessments, scoring rules, and completion requirements. Later edits create a new version.
5. Bind existing enrollments and attempts to the version actually used. Make any migration to a newer version an explicit recorded action.
6. Use HRM-101 | Introduction to Human Resource Management | SydTek University Microcredential as the first reference course. Source playlist: https://www.youtube.com/playlist?list=PLtS4zDr2sp3S1ptnw-a0Q030421d6jHd0. Preserve the observed source order and provenance. The current playlist has 48 entries and 47 unique video IDs; entries 42 and 43 repeat the same video. Keep a source-to-canonical-activity map so the duplicate does not create duplicate completion credit. Review source lessons before creating assessed questions or claiming full syllabus coverage. Preserve SCAT Goals as titled in the source. Do not invent missing transcripts or present draft assessments as approved instruction.
7. Sanitize author content and restrict media/resource schemes and access.

VERIFY
An instructor can create and publish one complete demonstration course. A missing assessment rule blocks publication where that assessment is required. Editing and publishing version 2 preserves version 1 and its learner associations. Unauthorized publishing is rejected.

RETURN
Working author flow, versioning evidence, remaining content requirements, and next chunk.
```

## STL-005 Enrollment and learner portal

**Dependencies:** STL-004

```text
STL-005 — ENROLLMENT AND LEARNER PORTAL
Dependency: STL-004.

GOAL
Give each learner appropriate course access and a usable place to learn.

IMPLEMENT
1. Add free, sponsored, and authorized manual enrollment. Reserve a purchase-derived grant source for the Shopify adapter.
2. Keep payer, learner, enrollment, and access grant distinct. Support two learners funded by one payer and two valid grants for one enrollment.
3. Evaluate access dates and prerequisites on the server. Record why access was granted, changed, or revoked.
4. Add My Learning, course outlines, lesson views, next/previous navigation, accessible resource links, and resumable lesson location.
5. Persist authoritative learning records in the database. Browser storage may assist presentation but cannot be the gradebook or access authority.
6. Preserve enrollment and earned records when a grant expires, subject to the data-retention policy. An expired paid grant must not remove a still-valid sponsorship.
7. Apply keyboard navigation, visible focus, readable labels, and narrow-screen layouts to this core journey.

VERIFY
Two learners sharing a payer retain independent course state. Revoking one grant changes only the intended access. An active alternative grant continues to work. Reloading and signing in on another session restore the correct learner's position. An unauthorized user cannot fetch a protected lesson directly.

RETURN
A demonstrated enrollment-to-lesson flow and access-state check results.
```

## STL-006 Progress and assessments

**Dependencies:** STL-005

```text
STL-006 — PROGRESS AND ASSESSMENTS
Dependency: STL-005.

GOAL
Calculate progress and assessed completion from trustworthy server records.

IMPLEMENT
1. Distinguish lesson viewed, activity completed, assessment passed, and course completed.
2. Add versioned quiz attempts with server-side answers, scoring, passing rules, retry policy, and timestamps. Keep answer keys out of learner responses.
3. Record an attempt against the enrolled learner and assessment version. Reject caller-supplied scores, pass flags, or another learner's identity.
4. Make duplicate and concurrent submissions safe. Define whether an attempt may be resubmitted and preserve the original decision.
5. Calculate course completion using the published version's required activities and assessments.
6. Expose appropriate feedback and progress to the learner and authorized instructor.
7. Add auditable correction handling. Corrections record the actor and reason and recompute affected decisions through defined rules.

VERIFY
A learner who watches every video but fails a required assessment remains incomplete. A forged passing score is rejected. Duplicate submission does not create extra attempts or completions. Publishing a new course version does not alter an earlier attempt.

RETURN
A complete assessed demonstration flow, material failure checks, and next chunk.
```

## STL-007 Outcomes and credentials

**Dependencies:** STL-006

```text
STL-007 — OUTCOMES AND CREDENTIALS
Dependency: STL-006.

GOAL
Explain what each completion means and issue a traceable credential.

IMPLEMENT
1. Link course and program outcomes to activities, assessment criteria, and evidence references.
2. Store completion decisions with course version, criteria version, relevant attempts, issuer, and decision timestamp.
3. Issue a unique completion credential only after the required decision exists. Make repeat issuance requests idempotent.
4. Provide a learner download and a permission-aware verification endpoint. Publish only the minimum authorized verification information.
5. Support correction and revocation with clear status and attribution. Preserve enough decision history to explain a credential under the applicable retention policy.
6. Keep personal evidence private and deletable. Do not publish learner records to a blockchain.
7. Use accurate credential descriptions. Do not generate an accredited degree, license, or institutional approval claim.

VERIFY
A failed or unfinished course cannot produce a credential. Repeating the request returns the same valid issuance. A revoked credential verifies as revoked. Cross-learner and cross-tenant access to evidence fails.

RETURN
The complete publish-to-learning-to-credential demonstration and its evidence links or local records.
```

## STL-008 Shopify course purchase integration

**Dependencies:** STL-003, STL-005, STL-007

```text
STL-008 — SHOPIFY COURSE PURCHASE INTEGRATION
Dependencies: STL-003, STL-005, STL-007.

GOAL
Translate verified course purchases into the correct access grants for offerings that use paid access. HRM-101's public learning material remains accessible independently of voluntary support.

IMPLEMENT
1. Discover the authorized development app and exact store identity. Map the verified installation to one internal organization. Use the current GraphQL Admin API and official authentication helpers.
2. Map products or variants to course offers and preserve the mapping that applied to each order line. Support quantities and a purchaser assigning eligible seats to separate learners.
3. Use a clearly labeled fixture adapter until real development-store access is available. Production must not use it.
4. Verify webhook authenticity, persist receipt and processing state, and queue durable processing. Use delivery IDs to deduplicate delivery and event IDs to correlate the underlying action. Independently deduplicate domain grants.
5. Reconcile authoritative order/refund state before deciding access. Handle duplicate, concurrent, late, and out-of-order notifications.
6. Handle mixed physical/digital orders, line-item and quantity refunds, and cancellations under documented policies. Affect only the relevant grant; preserve another valid grant and applicable earned records.
7. Add retry, failure visibility, and reconciliation for missed events. A browser checkout-return URL cannot authorize access.
8. Keep donation transactions separate from course purchase grants. A donation must not become a condition for HRM-101 access, grading, credential decisions, or priority. Do not reprice unrelated existing products when introducing this donation model.

VERIFY
Test repeated payment events, refund-before-payment delivery, late payment after refund, partial refunds, multiple learners, and sponsorship surviving paid-grant revocation. Demonstrate a real development-store flow only if connected; otherwise report fixture verification accurately.

RETURN
Connection status, product mapping, tested scenarios, unresolved permissions, and next chunk.
```

## STL-009 Merchant onboarding billing and usage

**Dependencies:** STL-008

```text
STL-009 — MERCHANT ONBOARDING BILLING AND USAGE
Dependency: STL-008.

GOAL
Make the product configurable for an independent merchant and measure its cost.

IMPLEMENT
1. Add organization branding, settings, onboarding, instructor invitation, and product mapping screens.
2. Keep merchant app subscriptions separate from learner course purchases, sponsorships, and credentials.
3. For the eventual public app, use current Shopify App Pricing guidance for supported plans. Verify the merchant's subscription through the documented authoritative interface; do not trust a plan parameter from a redirect.
4. Use no-charge development testing. Keep prices provisional until approved for release. Do not activate real merchant charges in this chunk.
5. Record per-organization usage for stored media, delivered media where available, AI operations, and other attributable resources. Distinguish observed cost from estimates and unknown values.
6. Enforce clearly defined capacity and budget behavior without falsely advertising unlimited hosting or AI usage.
7. Handle uninstall, expired installation, canceled app plan, and reinstall according to a documented data/export policy. A merchant-plan change is not a learner refund.

VERIFY
A second demonstration organization can use its own branding and settings. Merchant billing cannot modify an unrelated learner purchase. No mock plan can activate production access. Usage events are idempotent and a failed external call does not fabricate a successful billable event.

RETURN
Onboarding demonstration, billing boundary description, cost measurements, and outstanding production setup.
```

## STL-010 Reports exports and data lifecycle

**Dependencies:** STL-007, STL-008

```text
STL-010 — REPORTS EXPORTS AND DATA LIFECYCLE
Dependencies: STL-007 and STL-008.

GOAL
Provide useful learning records and reliable handling of personal data.

IMPLEMENT
1. Add scoped learner, course, enrollment, completion, outcome, and credential reports.
2. Export documented CSV and structured JSON records, including course versions, results, evidence references, and decision history where the requester is authorized.
3. Keep reporting identifiers stable and provide a data dictionary. Protect exported files and remove them after a defined period.
4. Implement subject-data requests, deletion/redaction, and shop removal through the current applicable Shopify interfaces.
5. Define retention decisions explicitly. Do not invent a blanket exemption for all academic evidence.
6. Cover personal files, derived exports, queued jobs, analytics copies, and backups. Maintain only the minimal justified suppression information needed so late events or restored backups do not recreate deleted data.
7. Add completion/error tracking and an operator view that does not unnecessarily expose learner content.

VERIFY
An authorized export contains the correct learner and course version. Another tenant cannot read it. A deletion request reaches associated private resources. Replaying an old enrollment event does not restore deleted personal data. Re-run the restoration behavior in STL-016.

RETURN
Sample synthetic exports, data dictionary, lifecycle checks, and precise retention questions requiring institutional input.
```

## STL-011 Family accounts and school cohorts

**Dependencies:** STL-003, STL-005, STL-010

```text
STL-011 — FAMILY ACCOUNTS AND SCHOOL COHORTS
Dependencies: STL-003, STL-005, STL-010.

GOAL
Support parents, children, teachers, and sponsored school enrollment with explicit relationships.

IMPLEMENT
1. Add a parent dashboard that can manage several distinct learner profiles while preserving separate progress.
2. Verify guardian relationships through the configured process. Do not infer guardianship from payment, a matching surname, or an email domain.
3. Add consent/notice records and age-appropriate enrollment steps using requirements approved for the actual pilot. Keep real child enrollment disabled until those requirements and release checks are satisfied.
4. Add school cohorts, teacher assignments, and sponsored seat allocations. Schools can receive access without fabricated checkout orders.
5. Record sponsorship source, coverage, dates, and estimated/observed cost separately from family purchases.
6. Support revocation or change of a guardian/teacher relationship. Restrict each parent to their authorized learners and each teacher to assigned cohorts.
7. Provide accessible family views on the intended desktop and mobile browsers.

VERIFY
One parent can manage two synthetic children without mixing records. A parent cannot access another family's child. An unassigned teacher is denied. A sponsorship can expire without deleting the learner's retained academic history.

RETURN
Family and teacher demonstrations, permissions evidence, and the exact remaining prerequisites for a real pilot.
```

## STL-012 Academic assessment and progression

**Dependencies:** STL-007, STL-010, STL-011

```text
STL-012 — ACADEMIC ASSESSMENT AND PROGRESSION
Dependencies: STL-007, STL-010, STL-011.

GOAL
Support teacher judgment and progression across an actual program.

IMPLEMENT
1. Add private assignment submissions, versioned rubrics, instructor feedback, reassessment, and moderated grade corrections.
2. Connect course learning outcomes to program learning outcomes and expose missing coverage.
3. Add prerequisites and progression decisions using published requirements. Keep attendance or activity separate from proficiency where the curriculum requires assessed mastery.
4. Add academic-record views suitable for the current program, with accurate labels and clear distinctions between completed, in progress, and unavailable offerings.
5. Model supervised projects, capstones, research proposals, and review milestones as configurable activities. Do not imply that creating those fields establishes degree-awarding authority.
6. Preserve assessment evidence, reviewer identity, rationale, and correction history under the established privacy rules.
7. Add instructor workload and pending-review views.

VERIFY
A submitted assignment remains pending until the required review occurs. A learner who fails a required outcome cannot progress merely by visiting lessons. A corrected grade preserves who changed it and why. A program report identifies both achieved and unmet requirements.

RETURN
One complete instructor-assessed course demonstration and an honest capability/limitation record.
```

## STL-013 Source to course AI workflow

**Dependencies:** STL-004, STL-007, STL-009

```text
STL-013 — SOURCE TO COURSE AI WORKFLOW
Dependencies: STL-004, STL-007, STL-009.

GOAL
Convert authorized source material into reviewable course drafts with traceable references.

IMPLEMENT
1. Support supplied or authorized video transcripts, documents, books, datasets, and SOP excerpts. Record rights/permission status and source locations.
2. Generate draft objectives, lesson structure, explanations, questions, and outcome mappings with source references where support exists. Flag unsupported or uncertain claims.
3. Treat source text as untrusted content. Source instructions cannot change tool permissions, publish material, access secrets, or alter grades.
4. Require an authorized review transition before publication. Keep model/provider/version, source version, reviewer, and generation cost metadata.
5. Keep API credentials server-side, enforce per-organization usage budgets, and exclude private student records from general course-generation input by default.
6. Expose a documented, permission-scoped agent interface for draft creation and authorized administration. Use idempotent jobs and distinguish draft edits from publication and assessment decisions.
7. Keep provider mocks clearly development-only.

VERIFY
An adversarial instruction inside a source cannot trigger a privileged action. An AI-generated course remains a draft. A budget limit stops additional paid generation. Repeated job delivery does not duplicate courses.

RETURN
One reviewed source-to-course demonstration, its source mapping, and measured or explicitly unknown costs.
```

## STL-014 Scheduled content and communities

**Dependencies:** STL-005, STL-009; STL-011 for minors

```text
STL-014 — SCHEDULED CONTENT AND COMMUNITIES
Dependencies: STL-005 and STL-009; also STL-011 if minors are involved.

GOAL
Support scheduled learning and moderated discussion within the correct access boundaries.

IMPLEMENT
1. Add scheduled release dates and enrollment-relative release rules with explicit time zones.
2. Check release and membership access on the server, including direct requests for lessons or files.
3. Add organization- and course-scoped discussion spaces with instructor moderation, reporting, and appropriate notification preferences.
4. Define subscription-derived access using the selected verified commerce integration. A canceled subscription may retain access through its paid-through date under the offer's policy.
5. For child-facing spaces, apply the approved school moderation and communication rules before enabling participation.
6. Preserve the distinction between a merchant's software plan and a learner's community membership.

VERIFY
A learner cannot bypass a scheduled release by changing the client clock or URL. Cross-course/private discussion access is denied. Moderation actions are attributable. Subscription-state replay converges to the correct access end date.

RETURN
Scheduled-release and community demonstrations, policy dependencies, and enabled audience.
```

## STL-015 Roblox learning integration

**Dependencies:** STL-006, STL-007; STL-011 for minors

```text
STL-015 — OPTIONAL ROBLOX LEARNING INTEGRATION
Dependencies: STL-006 and STL-007; also STL-011 where minors are involved.

GOAL
Accept trustworthy learning evidence from an authorized Roblox experience.

IMPLEMENT
1. Record an explicit authorized link between internal learner identity and Roblox identity. Do not assume a display name or buyer email establishes the link.
2. Map observed experience and activity identifiers to versioned course activities and assessment rules.
3. Build a server-to-server event interface with scoped credentials, expiry/replay protections, durable receipt, deduplication, and rate limits.
4. Accept results only from authorized server contexts. A browser or game client cannot assert an academic grade.
5. Translate validated events into evidence or completion only according to the published course rules. Keep game XP and academic proficiency distinct.
6. Start with synthetic contract tests. Connect a real experience only when its identifiers, code location, and permissions are verified.
7. Limit this chunk to learning-record integration. Any external-payment or game-access monetization requires its own current platform-policy review and authorized task.
8. Preserve existing Roblox projects and progress.

VERIFY
Forged, duplicate, expired, wrong-experience, and cross-learner events fail safely. A valid event updates the intended activity once. Disconnection retries do not create duplicate credentials.

RETURN
The integration contract, actual connection status, tested events, and unresolved experience-side work.
```

## STL-017 Voluntary donations and support records

**Dependencies:** STL-002, STL-003, STL-010; verified payment connection for live collection

```text
STL-017 — VOLUNTARY DONATIONS AND SUPPORT RECORDS
Dependencies: STL-002, STL-003, STL-010. A verified payment connection and recipient are required only for actual collection.

GOAL
Let people voluntarily support SydTek learning while keeping access, assessment, and academic records independent of contributions.

IMPLEMENT
1. Remove the superseded token discount requirements from this application and its configuration. Do not request a token contract, wallet connection, holdings, conversion rate, spending approval, or blockchain transaction.
2. Keep HRM-101's public playlist and learning resources available without a donation. Provide a clear Continue learning action alongside any support invitation. Do not preselect a gift or turn the gift into a required course price.
3. Configure the actual receiving entity, approved payment provider/account, supported currency, campaign purpose, optional amount choices or custom amount bounds, receipt contact, and refund/support terms. Do not invent a recipient, account, processor link, charitable status, tax deduction, or live collection capability.
4. Reuse the verified existing support information page where useful: https://enochworld.com/pages/sydtek-support. A link to that page does not establish that a donation checkout is active.
5. Use the selected provider's maintained hosted checkout and verified server events for collection. Keep processor secrets server-side. Persist transaction IDs and verified status; deduplicate events and reconcile timeouts, failed payments, refunds, and chargebacks.
6. Store the voluntary contribution separately from any course enrollment or commercial purchase. Track donor, recipient, campaign, currency, gross amount, observed fees, refunds, net amount, and purpose restrictions only when the corresponding facts are available. Unknown fees remain unknown.
7. Provide private receipts only after confirmed collection. Distinguish a support/payment acknowledgment from a charitable tax receipt. A pledge, browser redirect, or test transaction cannot be reported as settled public donations.
8. Keep donors private by default. An adult may support a learner or cohort without publishing that learner's identity. Donation amount must never affect a grade, mastery decision, earned credential, or a learner's visibility.
9. Support campaign pause and safe provider-disconnected states. If collection is unavailable, show support information and keep learning available. Do not silently substitute test payments in production.

VERIFY
A person can use HRM-101 without contributing. Declining or canceling a donation returns to learning. Duplicate/forged events cannot create duplicate receipts or inflate totals. Refunds adjust financial records without altering academic history. Learner/teacher exports do not expose private donor data. No wallet or token dependency remains. Live collection stays disabled until the actual destination and credentials are configured and checked.

RETURN
Support UI, actual recipient/provider connection status, verified payment-event behavior or clearly labeled test results, receipt behavior, and unresolved activation fields.
```

## STL-018 Education hub and HRM101 course presentation

**Dependencies:** Verified current site/navigation and course sources; STL-004 for dynamic catalog integration

```text
STL-018 — EDUCATION HUB AND HRM-101 COURSE PRESENTATION
Dependencies: verified current ENOCH WORLD site/navigation and HRM-101 sources. Connect the dynamic catalog after STL-004 is ready.

GOAL
Put SydTek Learn first in Education and organize the existing education offerings beneath it, with HRM-101 as the first featured course.

IMPLEMENT
1. Freshly inspect the owner-approved integrated master, actual published MAIN, and newer drafts. The public site observed on October 30, 2026 used theme 189733863535, ENOCH WORLD — MASTER Wakaboomee Fundraising. This is a snapshot, not an evergreen target. Preserve the shared header, music controls, footer, directory, Sports/SydTek Saints/Cricket tree, and existing route content.
2. Add SydTek Learn at the top of Education. Group the current education destinations within that section: University, Scholars, Seminary, trade and industry learning, courses/languages, school/family information, and fundraising/support. Preserve every existing destination. If the current menu or renderer cannot support another nested level, use a visible hub heading with grouped links on the hub and a supported-depth menu; do not hide or silently drop deeper links.
3. Reuse the existing SydTek education overview route where appropriate rather than creating competing entry points. Create or update the HRM-101 course route only after looking for an existing canonical page. Record the exact final handles and IDs.
4. Feature HRM-101 with its supplied title, Dr. Justin Goldston, the verified playlist link/embed, source-count metadata, and a clear Start learning action. Separate available public videos from future LMS progress, assessed completion, and credential issuance.
5. Preserve the author's stated LearnDay Canada provenance with attribution. Independently verified institutional names, approvals, or adoption records are needed before adding university logos or specific endorsement claims. Do not infer credit hours, recognized credit, CEUs, accreditation, or teaching effectiveness from video count or a promotional description.
6. Publish the source-backed module overview and proposed learning outcomes with accurate status. Use the canonical source manifest. Do not turn the repeated playlist entry into duplicate academic credit or silently rewrite SCAT Goals.
7. Present voluntary support separately, using an approved support destination. A support button must not masquerade as an active payment checkout when it leads to information. No token information or contract requirement belongs in this course journey.
8. Add concise metadata and useful internal links. Use Course structured data only for facts the page actually presents; omit unsupported price offers, ratings, accreditation, and credential awards.
9. Prepare reversible page/menu payloads or a draft-theme patch from fresh source, with fingerprints and rollback references. Respect connector restrictions on live theme writes and publication. Do not replace a complete menu from an incomplete snapshot.
10. Verify affected desktop/mobile navigation, keyboard access, course and support links, playlist availability, and retained education destinations. Keep source checks, preview checks, publication, and actual public verification separate.

VERIFY
SydTek Learn is first under Education and all previous education destinations remain reachable. HRM-101 is the first featured course. Learning remains available without a donation. Course copy, lesson counts, and provenance match their evidence. Shared site navigation/music and Sports/Cricket remain intact. Claim live publication only after an authorized successful write and an outside-preview public check.

RETURN
Changed page/menu/theme paths, source fingerprints and rollback reference, exact public or preview URLs, link/navigation check results, and any connection or publication blocker.
```

## STL-016 Pilot verification and release preparation

**Dependencies:** STL-001–STL-010 and enabled optional modules

```text
STL-016 — PILOT VERIFICATION AND RELEASE PREPARATION
Dependencies: STL-001 through STL-010 and every optional module enabled for this release.

GOAL
Produce a concrete, reviewable release with verified behavior and accurate claims.

IMPLEMENT AND VERIFY
1. Run the complete instructor-to-learner flow: author, publish, enroll, learn, assess, complete, verify credential, and export.
2. Use two isolated organizations, one payer sponsoring two learners, and a mixed-grant enrollment. Verify the intended refund changes only the correct access.
3. Verify denied cross-tenant requests, revoked sessions, expired grants, forged grades, duplicate events, and failed external integrations.
4. Restore a backup into an isolated environment. Confirm required records recover and deletion/suppression rules still apply.
5. Inspect core journeys on keyboard, desktop, and narrow screens. Resolve concrete usability and accessibility blockers.
6. Add appropriate monitoring, alerts, reconciliation, recovery runbooks, support procedures, and a measured cost report. Do not present estimated usage as observed expense.
7. For public Shopify distribution, run the current applicable app-review preparation process and identify outstanding data-access, billing, distribution, and support requirements. Do not claim App Store approval before it is granted.
8. Record exact release commit, tested environment, supported capabilities, known limits, rollback steps, and operational owner.
9. If donations are enabled, verify STL-017 with the exact receiving entity, actual provider configuration, private receipts, deduplicated events, refund handling, and continued learning without a contribution. Verify STL-018 against the current shared site and retained education destinations. Financial support must never change an academic result. Record unresolved provider/site access checks accurately.
10. Present the actual deployment target, permissions, recurring-cost settings, and release consequences for the authorized publication step. This chunk does not itself authorize production publishing, paid-service activation, or real child enrollment.

RETURN
Release candidate and evidence, unresolved blockers, the eligible pilot audience, and the concrete next deployment action.
```

# Sources and implementation status

Updated October 30, 2026. The current source of implementation status is the repository's build ledger and release evidence. Recheck time-sensitive Shopify APIs, permissions, and current master/navigation before execution. Course provenance and academic claims must remain consistent with their supporting evidence.

- [Shopify app scaffolding](https://shopify.dev/docs/apps/build/scaffold-app): current recommended app template.

- [Shopify distribution options](https://shopify.dev/docs/apps/launch/distribution): public and custom distribution boundaries.

- [Shopify app pricing](https://shopify.dev/docs/apps/launch/billing/shopify-app-pricing): current merchant app billing path.

- [Shopify webhook verification](https://shopify.dev/docs/apps/build/webhooks/verify-deliveries): authenticity and delivery handling.

- [Shopify privacy requirements](https://shopify.dev/docs/apps/build/compliance/privacy-law-compliance): privacy-event integration.

- [HRM-101 source playlist](https://www.youtube.com/playlist?list=PLtS4zDr2sp3S1ptnw-a0Q030421d6jHd0): actual source inventory and publisher description.

- [GOLGOTHA GROUP repository](https://github.com/projektgolgotha/GOLGOTHA_GROUP): implementation and versioned build records.

- [Current SydTek education overview](https://enochworld.com/pages/sydtek): existing public entry point to preserve.

- [Current SydTek support information](https://enochworld.com/pages/sydtek-support): existing support destination.

- [Shopify page updates](https://shopify.dev/docs/api/admin-graphql/2026-10/mutations/pageUpdate): page publishing and content updates using the actual store permissions.

