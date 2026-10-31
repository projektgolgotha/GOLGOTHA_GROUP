/* ENOCH WORLD — SydTek Seminary Ask ENOCH supplement v1
   Adds public Seminary FAQ records to the existing catalog without replacing it. */
(() => {
  'use strict';
  if (window.__sydtekSeminaryKnowledgeV1) return;
  window.__sydtekSeminaryKnowledgeV1 = true;

  const nativeFetch = window.fetch.bind(window);
  const FAQ_URL = '/pages/sydtek-seminary-faq';
  const NAV_URL = '/pages/sydtek-seminary-accreditation-navigator';
  const reviewed = '2026-10-30';
  let additionsPromise;

  const clean = value => String(value || '').replace(/\s+/g, ' ').trim();
  const slug = value => clean(value).normalize('NFKD').replace(/[\u0300-\u036f]/g, '')
    .toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 76);

  const loadAdditions = () => additionsPromise || (additionsPromise = nativeFetch(FAQ_URL, {
    credentials: 'same-origin',
    headers: { Accept: 'text/html' }
  }).then(response => {
    if (!response.ok) throw new Error('Seminary FAQ unavailable');
    return response.text();
  }).then(html => {
    const documentCopy = new DOMParser().parseFromString(html, 'text/html');
    const records = [...documentCopy.querySelectorAll('#sydtek-seminary-faq details.faq')].map((item, index) => {
      const question = clean(item.querySelector('summary')?.textContent);
      const answer = clean(item.querySelector('div')?.textContent);
      if (!question || !answer) return null;
      return {
        id: `sydtek-seminary-faq-${slug(question) || index + 1}`,
        question,
        answer,
        keywords: clean(`${question} ${answer} SydTek Seminary Ethiopian canon accreditation ABHE Skool dataset evidence`),
        roles: ['all'],
        references: [
          { label: 'SydTek Seminary FAQ', url: FAQ_URL },
          { label: 'Accreditation Navigator', url: NAV_URL }
        ],
        reviewed,
        status: 'public-source-summary',
        canonicalUrl: `https://enochworld.com${FAQ_URL}`,
        classification: 'public',
        trainingEligible: false,
        trainingEligibilityMeaning: 'Public retrieval summary; source and license terms remain controlling.'
      };
    }).filter(Boolean);

    records.unshift({
      id: 'sydtek-seminary-accreditation-navigator',
      question: 'What is the SydTek Seminary Accreditation Navigator?',
      answer: 'The Accreditation Navigator separates completed curriculum and evidence from the legal, governance, faculty, student-record, financial, operating-history and external-review gates still required. SydTek Seminary is currently a noncredit institutional-development pathway and is not represented as accredited.',
      keywords: 'SydTek Seminary accreditation navigator pathway ABHE legal authority governance faculty audit enrollment self-study',
      roles: ['all'],
      references: [
        { label: 'Accreditation Navigator', url: NAV_URL },
        { label: 'Seminary FAQ', url: FAQ_URL }
      ],
      reviewed,
      status: 'public-source-summary',
      canonicalUrl: `https://enochworld.com${NAV_URL}`,
      classification: 'public',
      trainingEligible: false,
      trainingEligibilityMeaning: 'Public retrieval summary; source and license terms remain controlling.'
    });
    return records;
  }).catch(() => []));

  window.fetch = async (input, init) => {
    const url = typeof input === 'string' ? input : (input && typeof input.url === 'string' ? input.url : '');
    const response = await nativeFetch(input, init);
    if (!url.includes('enoch-knowledge-catalog.json') || !response.ok) return response;
    try {
      const [catalog, additions] = await Promise.all([response.clone().json(), loadAdditions()]);
      if (catalog?.publicAccess !== true || !Array.isArray(catalog.records) || !additions.length) return response;
      const ids = new Set(additions.map(record => record.id));
      catalog.records = [...catalog.records.filter(record => !ids.has(record?.id)), ...additions];
      catalog.reviewedAt = reviewed;
      catalog.updatedAt = reviewed;
      const headers = new Headers(response.headers);
      headers.set('content-type', 'application/json; charset=utf-8');
      headers.delete('content-length');
      return new Response(JSON.stringify(catalog), {
        status: response.status,
        statusText: response.statusText,
        headers
      });
    } catch {
      return response;
    }
  };

  const addDirectoryEntries = () => {
    const node = document.getElementById('ew-directory-data');
    if (!node) return;
    const additions = [
      {
        title: 'SydTek Seminary | Accreditation Navigator',
        url: NAV_URL,
        category: 'Learning & schools',
        description: 'Follow the stage gates from the 81-book curriculum and Skool pilot to legal authority, governance, faculty, finances, operating evidence and external review.',
        keywords: 'SydTek Seminary accreditation ABHE navigator legal authority governance faculty audit enrollment',
        rank: 8
      },
      {
        title: 'SydTek Seminary | FAQ, Status & Evidence',
        url: FAQ_URL,
        category: 'Learning & schools',
        description: 'Search public answers covering the 81-book map, Skool, datasets, source gaps, institutional requirements and accreditation status.',
        keywords: 'SydTek Seminary FAQ 81 books Skool datasets accreditation evidence Ask ENOCH',
        rank: 8
      },
      {
        title: 'SydTek Seminary Datasets & Accreditation Toolkit',
        url: '/collections/sydtek-seminary-datasets-accreditation-toolkit',
        category: 'Learning & resources',
        description: 'Licensed Seminary curriculum, canon-map, assessment, LMS, governance and accreditation-readiness packages.',
        keywords: 'SydTek Seminary datasets curriculum canon LMS accreditation toolkit',
        rank: 40
      }
    ];
    try {
      const current = JSON.parse(node.textContent || '[]');
      if (!Array.isArray(current)) return;
      const urls = new Set(additions.map(entry => entry.url));
      node.textContent = JSON.stringify([...additions, ...current.filter(entry => !urls.has(entry?.url))]);
    } catch {}
  };

  addDirectoryEntries();
})();
