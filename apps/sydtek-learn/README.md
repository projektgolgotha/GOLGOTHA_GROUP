# SydTek Learn — STL-001 foundation

A runnable, disconnected learning foundation for GOLGOTHA GROUP. HRM-101 public lessons are freely accessible. Support is voluntary through the existing ENOCH WORLD support-information page; this application does not process donations.

## Run locally

Requirements: Node.js 22.12+ (verified here on 24.22.1) and npm.

From apps/sydtek-learn:

    npm ci
    npm run setup
    npm run dev

The development server opens on http://localhost:3000. No Shopify credentials are required for public pages. The source manifest must remain at content/sydtek-learn/courses/hrm-101/course.json in the repository root. A missing or invalid manifest is reported honestly; the original YouTube playlist link still works.

## Commands

    npm test
    npm run typecheck
    npm run build
    npm run start

The start script serves the production build and must be run from this app directory. The setup script generates Prisma Client and applies the existing SQLite session-table migration. The database contains only the official Shopify session schema; PostgreSQL, academic records, tenant isolation, learner identity, progress, assessment, and credentials are not implemented in STL-001.

## Routes

- /: public landing page.
- /learn/hrm-101: opt-in YouTube player, original-source links, ordered inventory, duplicate marker.
- /learner: public learner-workspace shell; no personal account or saved progress.
- /instructor: public information shell with explicit Shopify connection state.
- /app and /auth/*: official Shopify authentication; HTTP 503 while disconnected.
- /health: application, session-database readiness, and Shopify configuration status; HTTP 503 if the database/session table cannot be queried, HTTP 200 when the session schema is ready. A configured Shopify environment is labeled configured_unverified, never authenticated solely because variables exist.

## Shopify integration boundary

The official Shopify React Router authentication and Prisma session adapter are retained behind lazy initialization. No mock authentication, placeholder Shopify session, payment recipient, donation charge, product mutation, or credential issuance is substituted. Copy .env.example to .env only when configuring a local environment; never commit credentials. Real integration requires a registered app, verified callback URL, appropriate access scopes, authenticated installation, and the later privacy/retention and distribution gates. The Shopify configuration deliberately has no client ID. This foundation is not an App Store submission or a live deployment.

The Support learning link leads to https://enochworld.com/pages/sydtek-support. It is an information link, not a verified payment destination or statement of tax deductibility. Public course access does not depend on support.

## Source provenance

Derived from Shopify's official React Router template at commit 81eb98b6ca095eb0b92657f6007939a418f61955:
https://github.com/Shopify/shopify-app-template-react-router

LICENSE.md and TEMPLATE_README.md retain the template attribution and documentation. Root repository README.md and LICENSE are preserved. The lockfile pins installed dependencies. The template's product-generation example and product-price subscription were removed to keep this release read-only toward Shopify.

## Verification limits

The source manifest documents 48 playlist entries and 47 unique video IDs. Original ordering is retained; repeated content is labeled. Viewing does not create a completion record. Source metadata is not evidence of attendance, mastery, accredited credit, or CEU recognition. Video embedding and individual playback remain controlled by YouTube and must be checked in a real browser. Automated browser rendering and real Shopify OAuth are not claimed as verified by the foundation tests.

The inherited Dockerfile has not been adapted or tested for this repository's shared content directory. An app-directory-only container build does not include the sibling source manifest and would show the inventory-unavailable fallback. Container packaging, persistent storage, and production deployment remain later release work; use the repository-local commands above for this foundation.
