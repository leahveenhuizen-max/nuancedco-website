# Redesign Brief — The Late Diagnosis Life Review
Internal document. Guides the professional rebuild of the $19 Stan PDF.

## Purpose
A guided, structured reflection tool for the "was that ADHD too?" stage after a late ADHD diagnosis. The buyer re-reads their own history through an accurate lens instead of the character-flaw story they grew up with. It is the first paid step in the Nuanced Co. ladder and must make the future course feel worth waiting for.

## Audience
Late-diagnosed (or awaiting-diagnosis) ADHD and AuDHD adults, mostly 28–55, mostly Australian, recently diagnosed or in the assessment queue. They are wary of hype, allergic to shame, and have seen every generic ADHD printable.

## Product promise
"New language for the life you have already lived." A structured way to review your past with accuracy and less self-blame — educational and reflective only, not therapy, diagnosis, treatment or clinical advice.

## Suggested page count
16–24 pages A4. Long enough to feel like a $19 product, short enough to finish in one or two sittings.

## Recommended structure
1. Cover (full-bleed ink, week-1-PDF style)
2. Welcome from Leah (half page, founder voice, RN + lived experience, scope note)
3. How to use this guide (one page: pacing, no deadline, permission to stop)
4. The old map and the new map (framing spread — signature language)
5. Part 1: The labels you were given (guided prompts)
6. Part 2: The patterns you can now see (life-domain prompts: school, work, relationships, energy, money)
7. Part 3: What it cost you (grief-adjacent, gentle; bridges to the Grieving guide)
8. Part 4: What you are no longer willing to call a character flaw (signature section, the shareable moment)
9. Part 5: Your new map (consolidation page the buyer keeps)
10. Evidence note (one page)
11. Support and scope page (Australian crisis lines, when to seek professional support)
12. Back page: about Nuanced Co. + next-step CTA

## Visual direction
The site's editorial world, not workbook-craft: cream `#F6F1E9` pages, warm ink `#2A1F1A`, purple `#6B4570` accents with lilac on dark, parchment prompt boxes with a purple rule (as in the Week 1 companion PDF). Flat surfaces, no gradients, no drop shadows, generous margins (20mm+), one accent per spread. No emojis, no em dashes, no stock imagery.

## Cover direction
Match the Week 1 companion cover system: full-bleed warm ink, stacked NUANCED CO. wordmark with gold subtitle, lilac eyebrow ("A GUIDED REFLECTION"), Cormorant Garamond light title, purple hairline, italic product line. Retire the soft-collage cover style for the interior product (the existing JPG can stay as a social tile until the new cover exists).

## Typography
Cormorant Garamond (300/500) for display, Atkinson Hyperlegible for body (10.5–11pt, 1.7 line height). Both already licensed (OFL) and embedded in `pdf-tools/fonts/`.

## Diagram ideas (keep to 2–3, flat vector)
- "Old map / new map" two-column re-labelling diagram (lazy → task initiation difficulty, etc.)
- A simple life-domain wheel for Part 2
- A "cost ledger" layout for Part 3 (two ruled columns, not a table grid)

## Reflection prompt layout
Parchment box, purple left rule, small-caps label ("REFLECT"), serif italic question, then 4–6 ruled lines (or generous white space) for writing. One prompt per box; never stack more than two boxes per page. Include a "skip freely" note once, early.

## Accessibility
Atkinson Hyperlegible body, minimum 10.5pt, contrast at WCAG AA on every spread (no gold text on cream), no full-justified text, short paragraphs, prompts phrased one question at a time, PDF title/author metadata set, logical reading order, real text (no text-as-image).

## Evidence note
One page: research areas the guide draws on (late diagnosis and identity, camouflaging/masking, executive function) with 3–5 verifiable citations. Reuse only citations that pass verification. VERIFY BEFORE PUBLICATION — do not carry over the corrupted "Component, L." reference pattern found in the free guides.

## Support and scope note
Educational and reflective only. Not therapy, counselling, diagnosis, treatment, medication advice or crisis support. Lifeline 13 11 14, and the support directory at nuancedco.com.au/support. If reflection brings up more than expected, pause and consider professional support.

## Back-page CTA
"This guide is part of a wider body of work." → nuancedco.com.au, the paid guides page, email updates signup, and one line naming The Unmasked Life as the future flagship course (waitlist).

## Stan product description improvements
- Lead with the stage, not the format: "For the weeks and months after a late ADHD diagnosis, when your whole past starts asking to be re-read."
- State exactly what it is: guided PDF, page count, A4 and screen-friendly, instant download, Australian-made.
- State what it is not (educational, not therapy or clinical advice) — trust, and conversion insurance.
- Add founder line: written by Leah Veenhuizen, registered nurse and neurodivergent consultant.
- Keep price at $19 AUD.

## New copy or mostly redesign?
Undetermined until the live file is reviewed. Working assumption: keep the prompt architecture, rewrite connective copy only where it drifts from the voice, and fully redesign the layout on the pdf-tools pipeline (recommendation B, possibly C).

## Recommended export file names
- `The-Late-Diagnosis-Life-Review-NuancedCo-v2.pdf` (Stan upload)
- Working files under `pdf-tools/` alongside the course build (new target in build-pdfs.mjs or a sibling script)

## Pre-upload checklist
1. Live Stan file reviewed and content decisions signed off by Leah
2. All citations verified (VERIFY BEFORE PUBLICATION items cleared)
3. Scope note and crisis line present and correct
4. Australian spelling pass; no em dashes; no emojis
5. Fonts embedded; file under 10 MB; opens correctly in Preview, Acrobat, iPhone
6. Page numbers and footer on every interior page
7. PDF metadata: title, author "Leah Veenhuizen — Nuanced Co."
8. Test purchase on Stan after upload; confirm the delivered file is the v2
9. Update the site cover image only after the new cover exists
