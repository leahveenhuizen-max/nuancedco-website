# PDF Asset Inventory — Nuanced Co.
Internal document. Not for publication. Generated 7 July 2026.

## Finished PDFs

| Path | Product | Type | Status | Leah review? | Concern |
|---|---|---|---|---|---|
| `ADHD-Burnout-Guide-NuancedCo.pdf` | Free guide: ADHD Burnout | Exported PDF (4 pp) | Live, offered free via downloads.html | Yes | One corrupted/unverifiable reference ("Component, L."); free-vs-paid policy conflict (free-resource-audit says convert to paid or signpost) |
| `ADHD-Diagnosis-Australia-Guide-NuancedCo.pdf` | Free guide: Getting an ADHD Diagnosis in Australia | Exported PDF (4 pp) | Live, offered free via downloads.html | Yes | Time-sensitive claims (2026 GP prescribing, costs); two blog-grade citations to verify |
| `AuDHD-Executive-Dysfunction-Guide-NuancedCo.pdf` | Free guide: AuDHD Executive Dysfunction | Exported PDF (4 pp) | Live, offered free via downloads.html | Yes | Mentions "ADHD coaching" (brand rule conflict); blog-grade citations |
| `pdf-exports/The-Unmasked-Life-00-Welcome-Start-Here.pdf` | Course companion | Generated PDF (3 pp) | Internal, gitignored, not deployed | Later | Course on hold; not for sale now |
| `pdf-exports/The-Unmasked-Life-Week-1-The-Late-Diagnosis-Disruption.pdf` | Course companion Week 1 | Generated PDF (11 pp) | Internal, gitignored | Later | Strongest content asset; could seed future paid guides |
| `pdf-exports/The-Unmasked-Life-Week-2...–Week-4...pdf` (3 files) | Course companions Weeks 2–4 | Generated PDFs (4 pp each) | Internal, gitignored | Later | Thin (manuscript for weeks 2–4 is ~300 words each); not sellable as-is |

## Source and pipeline

| Path | Product | Type | Status | Leah review? |
|---|---|---|---|---|
| `pdf-tools/` (extract.py, print.css, build-pdfs.mjs, fonts/) | Course companion pipeline | PDF build system, one command: `node pdf-tools/build-pdfs.mjs` | Internal, working | No |
| `pdf-tools/build/` | Intermediate HTML | Generated, gitignored | Internal | No |

Note: no source files exist in this project for the three free guides. They were produced outside this repo. Edits require recreating them or obtaining the source.

## Marketing assets

| Path | Product | Type | Status | Leah review? | Concern |
|---|---|---|---|---|---|
| `late-diagnosis-life-review-cover.jpg` | The Late Diagnosis Life Review | Cover/thumbnail image (social tile) | Live on site | Yes | Only project evidence of the Stan product's design |
| `the-unmasked-life-thumbnail.jpg` / `.png` | Course | Thumbnails | Live | No | — |
| `content-drafts/video-scripts/late-diagnosis-life-review-promo-script.md` | The Late Diagnosis Life Review | Stan promo video script + product promise wording | Draft | Yes | Best source of the product's positioning copy |

## Strategy documents referencing products

- `content-drafts/product-strategy/free-resource-audit.md` — free guides should become paid or signposts (decision pending)
- `content-drafts/strategic-audit/brand-product-ladder-audit.md` — locked product model incl. Companion Guides ("Grieving the Life You Thought You Had" first)
- `content-drafts/reader-edition/the-unmasked-life-reader-edition-plan.md` — future Reader Edition
- `content-drafts/course-rewrite/content-migration-map.md` — names "Grieving the Life You Thought You Had" as the Week 1 companion guide

## Not found anywhere in the project

- **The Late Diagnosis Life Review PDF** (the file sold on Stan) — no export, no source
- **Grieving the Life You Thought You Had** — no PDF, no draft copy, no source; concept exists only in strategy documents
- Any Stan product-description text file

## Likely Stan Live Asset

- **File path:** not found in this project.
- **Confidence:** high confidence that the live Stan file is NOT in this repo. The only Life Review artefacts here are the cover JPG and the promo script.
- **Reason:** exhaustive filename and content search found no matching PDF or source document; the cover JPG shows a designed PDF cover ("A reflective guide for adults seeing their life through an ADHD lens") that matches no file here.
- **Action:** Leah must download the current live file from Stan and place it in the project (suggested: `content-drafts/pdf-suite/stan-live/`) before any layout, accuracy or proofreading verdict on the live product can be given. Until then, all Life Review review notes are based on the cover image and promo script only.
