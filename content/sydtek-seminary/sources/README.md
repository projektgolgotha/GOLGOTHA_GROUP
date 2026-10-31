# SydTek Seminary source inventory

This inventory preserves the creator’s submitted playlist evidence and connects it to identifiable public YouTube resources. It supplies **candidate teaching sources**, not a finding that the courses are complete, academically approved, or accredited.

## What was established

- **19 playlist screenshots** plus one cropped analytics screenshot were supplied in this conversation.
- **132 identifiable playlist observations** were transcribed: 114 main rows and 18 partially visible rows. They map to **110 distinct public playlist IDs**. Repeated screen rows remain separate evidence observations, not additional courses.
- All **128 visible playlist entry counts** in the mapped observations agree with the public metadata retrieved during this run. Four rows have cropped counts; their screenshot counts remain `null`.
- Nine public channel-listing pages yielded **244 playlist records**. Two additional collections in the first page were labeled by YouTube as course collections and are separately noted. The selected seminary inventory contains **118 playlists**: the 110 observed collections plus eight relevant discoveries.
- One individually identified **John Explained** video was added because no standalone Gospel of John playlist was found in this public listing.
- All **81 canon-registry units** have explicit source-mapping records: **65 ordinary title-level candidates, 13 requiring text/corpus-identity review, and 3 with no direct candidate established**. Verified academic coverage remains **zero** until substantive faculty review occurs.

Public source: [ENOCHLIVE1 playlists](https://www.youtube.com/@ENOCHLIVE1/playlists). The exact retrieval timestamp and pagination receipt are in `retrieval-receipt.json`. Public counts and collection contents can change.

## Files

| File | Purpose |
| --- | --- |
| `playlist-inventory.json` | Full verified playlist IDs, URLs, live titles/counts, categories, screenshot references, candidate canon relationships, and the distinct John video source. |
| `canon-source-map.json` | All 81 registry IDs, grouped-book components, direct candidates, contextual-only sources, review status, and direct-watch gating. |
| `screenshot-observations.json` | Visible title fragments, entry counts, source filenames and hashes, repeated rows, and the matching basis. Ellipses preserve truncation; bracketed text is an observer note. |
| `analytics-evidence.json` | Narrow transcription of the supplied analytics crop and limitations on what it establishes. |
| `duplicates-and-alternates.json` | Fourteen same-subject alternative-collection groups and repeated screenshot observations. Video overlap has not been measured. |
| `existing-framework.json` | Existing source modules I, III, IV, and X, preserved by their actual names and verified URLs. |
| `curation-findings.json` | Specific metadata findings that prevent automatic use of a mixed-topic collection and a wholesale “all books” coverage assumption. |
| `retrieval-receipt.json` | Retrieval method, pagination, source hashes, timestamps, and evidence limits. |

Raw uploaded screenshots are not committed to this public repository. Filename/hash provenance identifies the supplied evidence without republishing the images.

## Canon mapping and missing work

The crosswalk follows the [Ethiopian Orthodox Tewahedo Church’s canonical-book list](https://ethiopianorthodox.org/english/canonical/books.html), as represented in `../canon/canon-registry.json`: 46 Old Testament and 35 New Testament numbering units. Combined units retain their component-level relationships.

The three unfilled direct-source records are:

- **OT-16:** Ezra II and Ezra Sutuel. The Ezra/Nehemiah collection does not establish these texts.
- **OT-25:** Tegsats/Reproof. General Proverbs is contextual; a specific chapter/text selection has not been established.
- **OT-46:** Joseph ben Gorion/Josippon. The historical Josephus collection is contextual and is not substituted for this canonical text.

Additional review is explicit for Enoch, Proverbs/Messale, Wisdom/Metsihafe Tibeb, the Jeremiah and Daniel corpora, the four Sinodos divisions, the two Covenant divisions, Ethiopic Clement, and Ethiopic Didascalia. Similar names and generic group introductions cannot establish coverage of each exact Ethiopic text. Greek Maccabees is kept separate from 1–3 Meqabyan.

**John** uses the specific [John Explained video](https://www.youtube.com/watch?v=SsAIEvo6Xbw), observed at position 49 of the broad All Books collection. The broad parent collection is not assigned wholesale to fill missing books.

## Curation and implementation rules

The 165-entry collection titled “The Book of Genesis … All 81 Books” contains trading-related entry titles at observed positions 163–165. It is marked `excluded_from_recommended_learning: true`. Any relevant lessons must be selected individually after review. This finding concerns observed entry metadata; the videos were not watched.

Consumers should join playlists by `playlist_id`, videos by `video_id`, and canon units by `canon_id`. Only `candidate_sources_found` units have `automatic_direct_watch_allowed: true`; even these remain related learning resources with unverified instructional coverage. `text_identity_review` and `no_candidate_identified` units require curation before direct learning links are presented as assigned material.

Preserve the source module labels I, III, IV, and X. They are the creator’s existing framework, not proof that missing numbered modules were supplied or that a new LMS sequence must reuse those numbers.

## Analytics language

Permitted narrow description:

> The creator supplied an analytics screenshot showing **4,195,671 views** with the **365D** period selected. The crop does not display the channel header or calendar year.

This is creator-supplied screenshot evidence. It does not independently establish unique viewers, students, course completion, learning outcomes, organic traffic, views attributable entirely to the seminary, or accreditation. Playlist thumbnail numbers elsewhere in the screenshots are **entry counts**, not views.

## Verification performed

Public metadata was read through ordinary HTTPS and public listing continuations. No authenticated account, videos, audio, captions, or transcripts were downloaded. Referential checks passed for 81 unique canon units, 118 unique playlist records, all screenshot and source references, count agreement, exclusion of the mixed-topic collection from canon assignments, and withholding direct-watch permission for exact-text review units.
