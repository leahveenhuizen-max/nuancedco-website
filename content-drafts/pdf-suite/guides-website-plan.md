# Guides Website Plan — Nuanced Co.
Internal document. No website edits made under this plan yet.

## Main paid guides page
**Recommendation: rebuild `workbooks.html` as the paid guides page and rename it `guides.html`** (with a `_redirects` entry from /workbooks). Reasons: no guides.html exists; workbooks.html currently lists four fictional $15 products with dead buy buttons and emoji CTAs, duplicates the homepage title tag, and is indexable — it is the single most damaging commercial page on the site. Replacing its content converts the biggest liability into the ladder page. Nav label stays "PDF Downloads" or becomes "Guides".

## How each product is presented

**The Late Diagnosis Life Review ($19 — live)**
- Hero position on the guides page: cover image, one-paragraph promise ("the 'was that ADHD too?' stage"), what's inside (bullet list), founder line, scope line, price, single CTA "Get the guide on Stan" → existing Stan link (unchanged).
- Also stays: homepage primary CTA, links page top card.

**Grieving the Life You Thought You Had ($29 — in development)**
- Listed second as "In development" with no price shown until the file exists (per promo-script rule: do not promote until its Stan listing is live). One-line description + "Join updates to be told when it opens" → email CTA. Do NOT show a buy button.

**Planned suite (Masking, Overcompensation and Self-Blame · Support Needs Without Self-Blame · Rebuilding Self-Trust After Late Diagnosis)**
- One compact "What's coming" strip, titles only, no dates, no prices, tied to the same email CTA. This builds the ladder shape in the buyer's mind without overpromising.

**Free resources**
- Small section at the bottom: "Free starting points" linking to the support directory; free guides only if Leah confirms they stay free (free-resource-audit decision pending). Explicit line: "Paid guides are separate from free resources."

## Visible now vs hidden until ready
- Visible: Life Review (buyable), Grieving guide (named, unbuyable), planned-suite titles, email CTA, course-as-future-flagship line.
- Hidden: prices for unreleased products, any download/delivery links, course companion PDFs, fictional workbooks (removed).

## Stan link placement
Homepage hero (exists), guides page hero CTA, links page top card (exists). Nowhere else — keep one canonical purchase route.

## Email/update CTA placement
Guides page (after Grieving guide and in the coming-soon strip), plus the existing footer "Stay in the loop" boxes. Use the existing community-waitlist/MailerLite flow (unchanged).

## Course positioning
One short section at the bottom of the guides page: "The Unmasked Life — future flagship course" with the waitlist link. Never "available now".

## Internal links for Google
- Homepage → guides page (nav "PDF Downloads/Guides" already exists) and in the product ladder section
- guides page → evidence.html (evidence approach), about.html (founder), support.html (scope), the-unmasked-life.html (future course)
- evidence.html and about.html → guides page (one contextual link each)
- links.html already carries the social-traffic version of this ladder

## SEO
- Title: `ADHD Guides for Late-Diagnosed Adults | Nuanced Co.`
- Meta description: `Paid, research-informed ADHD guides for late-diagnosed adults, written by registered nurse and neurodivergent consultant Leah Veenhuizen. Start with the Late Diagnosis Life Review.`
- H1: `Guides for the life you are re-reading`
- H2s: The Late Diagnosis Life Review · In development: Grieving the Life You Thought You Had · What's coming next · Free starting points · The future flagship course
- Add to sitemap.xml on rebuild; ensure indexable (workbooks.html already is); fix its duplicate homepage title immediately on rebuild.
- Topic clusters served: late ADHD diagnosis (1), grief after diagnosis (2), ADHD resources for adults (9).
