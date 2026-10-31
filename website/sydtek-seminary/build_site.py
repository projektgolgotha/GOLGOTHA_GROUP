"""Build the Seminary page and a bounded addition to the current Education hub.

Only source-linked candidates with automatic_direct_watch_allowed are rendered
as study links. Publication is a separate, verified Admin API operation.
"""
from __future__ import annotations

import hashlib
import html
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def link(url: str, label: str, css: str = "") -> str:
    if not url.startswith(("https://", "#", "/pages/")):
        raise ValueError(f"Unexpected link scheme: {url}")
    return f'<a{f" class={chr(34)}{esc(css)}{chr(34)}" if css else ""} href="{esc(url)}">{esc(label)}</a>'


def main() -> None:
    config = read_json(HERE / "site-config.json")
    registry = read_json(ROOT / "content/sydtek-seminary/canon/canon-registry.json")
    curriculum = read_json(ROOT / "content/sydtek-seminary/canon/curriculum-manifest.json")
    inventory = read_json(ROOT / "content/sydtek-seminary/sources/playlist-inventory.json")
    source_map = read_json(ROOT / "content/sydtek-seminary/sources/canon-source-map.json")
    units = {u["id"]: u for u in registry["units"]}
    sources = {p["playlist_id"]: p for p in inventory["playlists"]}
    videos = {v["video_id"]: v for v in inventory.get("videos", [])}
    mappings = {u["canon_id"]: u for u in source_map["units"]}
    assigned = [uid for c in curriculum["courses"] for uid in c["unit_ids"]]
    assert len(units) == 81 and len(mappings) == 81
    assert set(assigned) == set(units) and all(n == 1 for n in Counter(assigned).values())
    assert sum(u["testament"] == "OT" for u in units.values()) == 46
    assert sum(u["testament"] == "NT" for u in units.values()) == 35
    assert all(m["coverage_verified"] is False for m in mappings.values())

    classroom_url = config["skool_classroom_url"]
    classroom_label = "Start in the Skool classroom" if config["skool_publication_verified"] else "Visit the SydTek academy"
    if not config["skool_publication_verified"]:
        classroom_url = config["skool_group_url"]
    gh = config["github_base"]
    orientation_url = gh + "/docs/sydtek-seminary/SEM-000_ORIENTATION.md"
    academic_url = gh + "/docs/sydtek-seminary/ACADEMIC_PROGRAM.md"
    canon_url = "https://ethiopianorthodox.org/english/canonical/books.html"

    course_html = []
    for course in curriculum["courses"]:
        unit_html = []
        for uid in course["unit_ids"]:
            unit, mapped = units[uid], mappings[uid]
            resources = []
            if mapped["automatic_direct_watch_allowed"]:
                for pid in mapped["candidate_playlist_ids"]:
                    source = sources[pid]
                    assert not source.get("excluded_from_recommended_learning", False)
                    resources.append(link(source["url"], source["title"]))
                for vid in mapped["candidate_video_ids"]:
                    source = videos[vid]
                    assert not source.get("excluded_from_recommended_learning", False)
                    resources.append(link(source["url"], source["title"]))
            if resources:
                resource_html = '<div class="ss-resources"><span class="ss-small">Related video resources</span><ul>' + "".join(f"<li>{r}</li>" for r in resources) + "</ul></div>"
            else:
                note = "Exact text and teaching-source selection awaits academic review." if mapped["status"] == "text_identity_review" else "Reading and teaching resources are being prepared."
                resource_html = f'<p class="ss-pending">{esc(note)}</p>'
            components = ""
            if len(unit["components"]) > 1:
                components = '<p class="ss-small">Study these components: ' + esc("; ".join(unit["components"])) + ".</p>"
            unit_html.append(f'<li class="ss-unit" id="unit-{esc(uid)}"><div class="ss-unit-heading"><strong>{esc(unit["display_title"])}</strong><span>{esc(uid)}</span></div>{components}{resource_html}</li>')
        if course["code"] == "SEM-000":
            body = '<ol class="ss-steps"><li>Set your four-week study plan.</li><li>Learn how the 81-book map is organized.</li><li>Keep a traceable reading record.</li><li>Prepare your first passage analysis and reflection.</li></ol>' + link(orientation_url, "Read the full orientation →")
        elif course["code"] == "SEM-199":
            body = '<p>Build a portfolio of your reading records, compare canonical traditions using cited sources, and prepare a teaching project that you can explain and revise after feedback. The assessment plan includes a written project and an oral discussion.</p>'
        else:
            body = '<ul class="ss-units">' + "".join(unit_html) + "</ul>"
            if course["code"] == "SEM-101":
                body = '<p>' + link(gh + '/docs/sydtek-seminary/SEM-101_SYLLABUS_AND_LESSONS.md', 'Read the SEM-101 syllabus, passages, and assignments →') + '</p>' + body
        readiness = "Starter materials authored" if course["status"] == "authored_draft" else "Course outline and resource map"
        course_html.append(f'<details class="ss-course" id="{esc(course["code"].lower())}"><summary><span class="ss-course-code">{esc(course["code"])}</span><span class="ss-course-title">{esc(course["title"])}</span><span class="ss-course-meta">{course["estimated_study_hours"]} estimated study hours</span></summary><div class="ss-course-body"><p>{esc(course["summary"])}</p><p class="ss-small ss-readiness">{readiness}</p>{body}</div></details>')

    modules = [p for p in inventory["playlists"] if p.get("category") == "existing_seminary_module" and not p.get("excluded_from_recommended_learning")]
    module_links = "".join(f'<li>{link(p["url"], p["title"])}</li>' for p in modules)
    page = f'''<section class="ss-seminary" id="sydtek-seminary" aria-labelledby="ss-title" data-seminary-version="0.1">
  <style>
    .ss-seminary{{--ss-ink:#172e37;--ss-muted:#52656a;--ss-paper:#f6f3eb;--ss-line:#d8ded9;--ss-gold:#d5b578;max-width:1180px;margin:24px auto 48px;color:var(--ss-ink);background:var(--ss-paper);border:1px solid var(--ss-line);border-radius:18px;overflow:hidden;font-family:inherit;font-size:16px;line-height:1.65;scroll-margin-top:260px}}
    .ss-seminary *{{box-sizing:border-box}}.ss-seminary h1,.ss-seminary h2,.ss-seminary h3,.ss-seminary p{{margin:0}}.ss-seminary h1,.ss-seminary h2,.ss-seminary h3{{color:var(--ss-ink);line-height:1.15;letter-spacing:-.025em}}.ss-seminary h1{{font-size:clamp(42px,6vw,76px);margin:14px 0 20px}}.ss-seminary h2{{font-size:clamp(28px,4vw,42px);margin-bottom:18px}}.ss-seminary h3{{font-size:23px;margin-bottom:12px}}.ss-seminary a{{color:inherit;text-underline-offset:4px;overflow-wrap:anywhere}}.ss-seminary a:focus-visible,.ss-seminary summary:focus-visible{{outline:3px solid #267e9c;outline-offset:5px}}.ss-seminary section[id],.ss-seminary details[id],.ss-seminary li[id]{{scroll-margin-top:260px}}
    .ss-seminary .ss-hero{{padding:clamp(26px,5vw,58px);background:linear-gradient(120deg,#f5f0e4,#fffdf6)}}.ss-seminary .ss-eyebrow{{font-size:12px;font-weight:800;text-transform:uppercase;letter-spacing:.14em}}.ss-seminary .ss-lead{{font-size:clamp(18px,2.5vw,22px);max-width:780px}}.ss-seminary .ss-intro{{max-width:820px;color:var(--ss-muted);margin-top:16px}}.ss-seminary .ss-actions{{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px;align-items:center}}.ss-seminary .ss-button{{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:11px 19px;border:1px solid var(--ss-ink);border-radius:7px;font-weight:750;text-decoration:none;line-height:1.35}}.ss-seminary .ss-primary{{background:var(--ss-ink);color:#fff}}.ss-seminary .ss-button:hover{{box-shadow:0 0 0 2px var(--ss-gold)}}.ss-seminary .ss-status{{display:inline-block;margin-top:22px;font-size:13px;color:#34534b;background:#e6eee5;padding:7px 11px;border-radius:5px}}.ss-seminary .ss-facts{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));padding:25px clamp(26px,5vw,58px);background:var(--ss-ink);color:#fff;gap:20px}}.ss-seminary .ss-fact strong{{display:block;color:#e5c78f;font-size:28px;line-height:1.2}}.ss-seminary .ss-fact span{{display:block;font-size:13px;margin-top:6px;color:#e0e9e7}}
    .ss-seminary .ss-section{{padding:clamp(26px,4.5vw,52px);border-bottom:1px solid var(--ss-line)}}.ss-seminary .ss-section>p+p{{margin-top:14px}}.ss-seminary .ss-small{{font-size:13px;color:var(--ss-muted)}}.ss-seminary .ss-quicklinks{{display:flex;gap:12px 20px;flex-wrap:wrap;margin:22px 0}}.ss-seminary .ss-grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin-top:24px}}.ss-seminary .ss-card{{background:#fff;border:1px solid var(--ss-line);border-radius:10px;padding:24px;min-width:0}}.ss-seminary .ss-card p+p{{margin-top:12px}}.ss-seminary .ss-card ul,.ss-seminary .ss-steps{{padding-left:23px}}.ss-seminary li+li{{margin-top:9px}}.ss-seminary .ss-course{{background:#fff;border:1px solid var(--ss-line);border-radius:9px;margin-top:13px;overflow:hidden}}.ss-seminary .ss-course summary{{display:grid;grid-template-columns:85px minmax(0,1fr);gap:6px 14px;cursor:pointer;padding:22px;min-height:72px}}.ss-seminary .ss-course summary::after{{content:'Open study guide +';grid-column:2;font-size:12px;color:var(--ss-muted)}}.ss-seminary .ss-course[open] summary::after{{content:'Close study guide −'}}.ss-seminary .ss-course-code{{font-size:12px;font-weight:800;letter-spacing:.05em;color:#655329}}.ss-seminary .ss-course-title{{font-size:19px;font-weight:750;line-height:1.3}}.ss-seminary .ss-course-meta{{grid-column:2;font-size:12px;color:var(--ss-muted)}}.ss-seminary .ss-course-body{{padding:0 22px 24px}}.ss-seminary .ss-readiness{{margin:10px 0 18px}}.ss-seminary .ss-units{{list-style:none;padding:0;margin:20px 0 0}}.ss-seminary .ss-unit{{border-top:1px solid var(--ss-line);padding-top:18px;margin-top:18px}}.ss-seminary .ss-unit-heading{{display:flex;justify-content:space-between;gap:15px;align-items:baseline}}.ss-seminary .ss-unit-heading>span{{font-size:12px;color:var(--ss-muted);white-space:nowrap}}.ss-seminary .ss-resources{{margin-top:9px}}.ss-seminary .ss-resources ul{{font-size:14px;padding-left:20px;margin:5px 0}}.ss-seminary .ss-pending{{font-size:13px;color:#735820;margin-top:8px}}.ss-seminary .ss-note{{border-left:3px solid var(--ss-gold);padding:12px 18px;background:#fffaf0;margin-top:20px}}.ss-seminary .ss-foundations{{list-style:none;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}}.ss-seminary .ss-foundations li{{margin:0}}.ss-seminary .ss-related summary{{font-weight:750;cursor:pointer}}.ss-seminary .ss-related ul{{padding-left:20px;font-size:14px}}.ss-seminary .ss-signature{{padding:22px 30px;font-size:12px;color:var(--ss-muted)}}
    @media(max-width:640px){{.ss-seminary{{margin:16px 0 32px;border-radius:10px}}.ss-seminary .ss-grid,.ss-seminary .ss-foundations{{grid-template-columns:1fr}}.ss-seminary .ss-facts{{gap:12px;padding:22px}}.ss-seminary .ss-fact strong{{font-size:23px}}.ss-seminary .ss-button{{width:100%;text-align:center}}.ss-seminary .ss-course summary{{grid-template-columns:1fr;padding:19px}}.ss-seminary .ss-course summary::after,.ss-seminary .ss-course-meta{{grid-column:1}}.ss-seminary .ss-course-body{{padding:0 19px 22px}}.ss-seminary .ss-unit-heading{{display:block}}.ss-seminary .ss-unit-heading>span{{display:block}}.ss-seminary .ss-card{{padding:20px}}}}
    @media(prefers-reduced-motion:reduce){{.ss-seminary *{{scroll-behavior:auto}}}}
  </style>
  <header class="ss-hero">
    <p class="ss-eyebrow">{link(config['hub_url'], 'Education at ENOCH WORLD')} / Ethiopian Canon Studies</p>
    <h1 id="ss-title">SydTek Seminary</h1>
    <p class="ss-lead">Study Scripture. Practice interpretation. Grow in service.</p>
    <p class="ss-intro">Explore the Ethiopian biblical tradition through a structured 81-book study map, recorded teaching, close reading, reflection, and teaching practice. Begin with the orientation and build a portfolio of what you understand.</p>
    <div class="ss-actions">{link(classroom_url, classroom_label, 'ss-button ss-primary')}{link('#ss-study-map', 'Explore the 81-book study map', 'ss-button')}</div>
    <p class="ss-status">Open learning resources · Noncredit pathway in development</p>
  </header>
  <div class="ss-facts" aria-label="Pathway at a glance"><div class="ss-fact"><strong>81</strong><span>canon entries mapped</span></div><div class="ss-fact"><strong>12</strong><span>parts in the study pathway</span></div><div class="ss-fact"><strong>Read → Reflect</strong><span>Explain → Apply → Revise</span></div></div>

  <section class="ss-section" id="ss-start">
    <p class="ss-eyebrow">Start with understanding</p><h2>Your first step is a reading record.</h2>
    <p>Choose a translation you can legally access and read Genesis 1:1–2:3. Record the edition, passage, and source. Then write 150–200 words that distinguish three observations from one interpretation. Bring one question you want to investigate.</p>
    <div class="ss-grid"><article class="ss-card"><h3>Begin the orientation</h3><p>Set a study schedule, learn how the canon map works, practice source-aware reading, and assemble your first portfolio.</p><div class="ss-actions">{link(orientation_url, 'Read SEM-000 orientation →')}{link(classroom_url, 'Open the classroom →')}</div></article><article class="ss-card"><h3>Keep your own learning portfolio</h3><p>Save your passage notes, reflections, teaching drafts, and revisions. Use your instructor’s private submission instructions when an assessed cohort is available.</p><p class="ss-small">Watching a lesson is a starting activity. Reviewed written work and teaching practice form the planned assessment pathway.</p></article></div>
  </section>

  <section class="ss-section" id="ss-study-map">
    <p class="ss-eyebrow">The course pathway</p><h2>One connected study of the canon.</h2>
    <p>The map follows the {link(canon_url, 'Ethiopian Orthodox Tewahedo Church’s published list')}: 46 Old Testament entries and 35 New Testament entries. Some entries combine books or distinguish parts of a larger work. Open each course below to see the assigned entries and related video resources.</p>
    <p class="ss-note">This is a developing survey pathway. Video links are related teaching resources; primary-text selections and assessed course coverage await academic review. Study hours are planning estimates for reading, viewing, writing, and feedback.</p>
    <nav class="ss-quicklinks" aria-label="Study map sections">{link('#sem-000', 'Orientation')}{link('#sem-101', 'Old Testament')}{link('#sem-107', 'New Testament')}{link('#sem-110', 'Ethiopian church order')}{link('#sem-199', 'Capstone')}</nav>
    {''.join(course_html)}
    <p class="ss-small" style="margin-top:20px">The current design estimates 420 total study hours across the pathway. Workload estimates will be refined during an assessed pilot. See the {link(academic_url, 'academic program and assessment design')}.</p>
  </section>

  <section class="ss-section" id="ss-method"><p class="ss-eyebrow">From study to service</p><h2>Demonstrate what you understand.</h2><div class="ss-grid"><article class="ss-card"><h3>For each book or component</h3><ol class="ss-steps"><li><strong>Read:</strong> identify the assigned text, edition, and passage.</li><li><strong>Observe:</strong> describe its language, structure, and context.</li><li><strong>Interpret:</strong> make a claim supported by the passage and cited sources.</li><li><strong>Apply:</strong> explain an implication for teaching, practice, or service.</li><li><strong>Revise:</strong> respond to questions and feedback.</li></ol></article><article class="ss-card"><h3>For the final portfolio</h3><p>Bring together reading records across the canon, a comparative study, and a teaching project. The proposed assessment uses clear criteria for textual understanding, evidence, reasoning, application, and revision.</p><p>The Seminary’s existing formation framework includes Mirror → Water → Fire and portfolio-based ministry learning.</p></article></div></section>

  <section class="ss-section" id="ss-foundations"><p class="ss-eyebrow">The wider Seminary</p><h2>Build on the existing teaching.</h2><p>The 81-book survey develops the existing Ethiopian Canon Studies program. Biblical Studies, Ministry Formation, and Digital Ministry remain related areas in the Seminary’s institutional framework.</p><details class="ss-related" style="margin-top:22px"><summary>Explore existing Seminary teaching modules</summary><ul>{module_links}</ul></details><ul class="ss-foundations"><li>{link('https://github.com/GoldstonianConcordanceBible/SydTek-Seminary', 'Seminary institutional repository →')}</li><li>{link('https://enochworld.com/pages/sydtek-evidence-library#seminary', 'Seminary source documents →')}</li><li>{link('https://github.com/GoldstonianConcordanceBible/canonical-index', 'GCB canonical index →')}</li><li>{link('https://enochworld.com/pages/sydtek-role-applications?institution_id=seminary#apply', 'Faculty and leadership opportunities →')}</li><li>{link('https://enochworld.com/pages/sydtek-connected-learning', 'Connected learning development →')}</li></ul></section>

  <section class="ss-section" id="ss-status"><p class="ss-eyebrow">Program development</p><h2>A documented path toward accreditation.</h2><p>Current status: noncredit curriculum development. Accreditation, degree-awarding authority, and an approved certificate award are not established by this release.</p><p>The next institutional stages are faculty adoption of the curriculum, documented governance and learner support, jurisdiction-specific authorization review, measured pilot learning, and an appropriate accreditor’s eligibility and evaluation process. Each milestone needs its own evidence.</p><div class="ss-actions">{link(gh + '/docs/sydtek-seminary/ACCREDITATION_PATHWAY.md', 'Read the accreditation development plan', 'ss-button')}{link('https://enochworld.com/pages/sydtek-accreditation-meter#seminary', 'Institutional status and evidence →')}</div></section>

  <section class="ss-section" id="ss-support"><h2>Help the learning grow.</h2><p>The public study resources are free to explore. Voluntary support helps develop teaching resources and the learning program. Assessment and academic decisions follow the published learning requirements.</p><div class="ss-actions">{link(config['support_url'], 'Explore voluntary support', 'ss-button')}{link(classroom_url, 'Continue to the classroom →')}</div></section>
  <p class="ss-signature">SydTek Seminary · ENOCH WORLD · Goldstonian Concordance Bible · Dedicated to Sydney Goldston</p>
</section>
'''
    feature = f'''  <article id="stl-seminary" class="stl-feature" aria-labelledby="stl-seminary-title">
    <div class="stl-feature-copy"><span class="stl-badge">Seminary · Ethiopian Canon Studies</span><h3 id="stl-seminary-title">Study the 81-book Ethiopian canon.</h3><p>Follow a connected study map through Scripture, source-aware reading, reflection, and teaching practice. Start with the orientation in the SydTek Seminary classroom.</p><p class="stl-meta">81 canon entries · 12-part pathway · Noncredit program development</p><div class="stl-actions">{link(config['public_url'], 'Explore SydTek Seminary →', 'stl-button stl-primary')}{link(classroom_url, 'Open the Skool classroom', 'stl-button')}</div></div>
    <div class="stl-feature-side"><p class="stl-eyebrow" style="color:#dfc689">Theology &amp; ministry formation</p><h4>Read. Reflect. Explain. Apply.</h4><ul><li>Old and New Testament study</li><li>Enoch, Jubilees, and Meqabyan</li><li>Ethiopian church order</li><li>Reading portfolios and a teaching capstone</li></ul><p style="font-size:13px;color:#e0e8e8">Open learning resources now; the assessed certificate and accreditation pathway are in development.</p></div>
  </article>
'''
    baseline = (HERE / "rollback/sydtek-before.html").read_text(encoding="utf-8")
    marker = '<div class="stl-section-head" id="stl-programs">'
    assert baseline.count(marker) == 1 and 'id="stl-seminary"' not in baseline
    hub_candidate = baseline.replace(marker, feature + marker, 1)
    assert hub_candidate.replace(feature, "", 1) == baseline
    (HERE / "page-candidate.html").write_text(page, encoding="utf-8")
    (HERE / "hub-feature.html").write_text(feature, encoding="utf-8")
    (HERE / "hub-candidate.html").write_text(hub_candidate, encoding="utf-8")
    (HERE / "preview.html").write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>SydTek Seminary preview</title><style>body{margin:0;padding:20px;background:#e9ede8;font-family:system-ui,sans-serif}</style></head><body>' + page + '</body></html>', encoding="utf-8")
    manifest = {
        "status": "prepared_not_published",
        "canon_units": len(units),
        "courses": len(curriculum["courses"]),
        "resource_status_counts": dict(Counter(u["status"] for u in mappings.values())),
        "skool_publication_verified": config["skool_publication_verified"],
        "hub_baseline_preserved_exactly": True,
        "menu_change_required": False,
        "theme_file_changes": [],
        "intended_page_template": "ew-learning",
        "page_candidate_sha256": hashlib.sha256(page.encode()).hexdigest(),
        "hub_candidate_sha256": hashlib.sha256(hub_candidate.encode()).hexdigest(),
    }
    (HERE / "preparation-checks.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
