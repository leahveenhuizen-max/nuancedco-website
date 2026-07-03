# P1 Gold Standard Build Summary

**Date:** 2 July 2026. Follows the completed P0 Truth Pass. No commits, no pushes; all changes are unstaged in the working folder.

## What changed and why

### Homepage (index.html)
- The logo-only splash viewport is gone. The first screen now carries the eyebrow "Research-informed ADHD education for late-diagnosed adults", the headline "New language for the life you have already lived.", the approved positioning sentence naming Leah and her three roles, one primary CTA (Explore The Unmasked Life), one secondary CTA (Start with the Life Review, to Stan), and a one-line scope note. Verified rendering at 1440px and 390px.
- A founder strip sits directly under the hero: Leah's existing photo (leah-headshot-warm.jpg), the approved founder line, and a Meet Leah link. Founder presence is now within the first two screenfuls.
- The three-card "pathways" section was rebuilt as the four-rung product ladder: The Late Diagnosis Life Review ($19 AUD, buy via Stan), Companion Guides (from $29 AUD, first guide in production, notify CTA), Reader Edition (coming soon, notify CTA), The Unmasked Life full course (founding beta in preparation, flagship card). Each rung states who it is for, what it helps with, status, price or status honesty, and one CTA. No unavailable product has a buy link. A slim "Work with Leah" band below keeps 1:1 consultations visible without competing with the ladder.
- Community section CTA renamed "Join the updates list" so the course waitlist and the community list are no longer twins.
- Footer updated to current-era links (The Unmasked Life, Resources, Evidence, Workplace Consulting, Support) and drops fossil pages.

### Navigation (site-wide)
One unified nav (About / The Unmasked Life / Resources / Support / Contact / Book a Call) replaced the old five-dropdown menu on: index, about, the-unmasked-life, faq, book, contact, media, community-waitlist, the-unmasked-life-coming-soon, how-i-work, who-i-work-with, services. The mobile menu on index was rebuilt to match. workbooks.html (fossil) was deliberately left untouched.

### Course sales page (the-unmasked-life.html)
- Hero now states founding beta status and price context: "Founding beta in preparation. From $197 AUD when enrolment opens. One payment, lifetime access, no deadlines."
- New "How the course works" section describes the six-scene guided journey, the three routes (full, low-capacity, speed-read), the weekly Snapshot artefact the learner keeps, autosave, and the phone-first design. It includes an honest note that preview screenshots will be added when the beta build is final (no fake screenshots, no internal file links).
- New "Course or PDF?" section explains how the full course differs from the Life Review, Companion Guides and the coming Reader Edition.
- Leah bio block now links to the new evidence page.

### Evidence (new page: evidence.html)
Explains what research-informed means and does not mean, the education-only scope, Australian guidance priority (AADPA guideline, Healthdirect navigation), the evidence areas the course draws from, and the professional-plus-lived-experience basis. No references were invented; the page states that the full Evidence Base and References document is being prepared and carries a "written and reviewed July 2026" date. Linked from the homepage nav and footer, the course page bio, links.html and about.html. Added /evidence to _redirects.

### Links page (links.html)
Rebuilt as the public start-here page: all emojis removed, Life Review first with price, course waitlist second, free support directory third, Work with Leah (book.html, no longer a mailto), workplace, about, evidence, media. Removed the quiz card, the pricing card, the consult.html card and the discontinued "Understanding Who You Are After Your Diagnosis" course card. Bio line updated to the brand positioning sentence.

### About page (about.html)
The duplicated second introduction ("Hi, I'm Leah." section reusing the same photo) was removed. The remaining founder section now carries the heading "Hi, I'm Leah.", a role line (neurodivergent consultant, registered nurse, mental health educator), the credential chips, the Geelong line, and an evidence-page link.

### Fossil control
- noindex added to workbooks.html, pricing.html, courses.html, quiz.html, podcast.html (all other fossils were noindexed in P0).
- book.html quiz CTAs replaced with Life Review and resources links; the "took the free quiz" form option removed.
- Verified: no page in the current public pathway links to any fossil page.
- Deletion recommendations and the merge plan for services/how-i-work/who-i-work-with are in fossil-page-cleanup-plan.md. No files were deleted.

## Status lines

- **Product ladder:** all four rungs public, priced or honestly statused. Companion Guides and Reader Edition CTAs route to the existing course-updates capture rather than fake shop links.
- **Evidence:** public approach page live; full reference list still to be produced (P3.1).
- **Founder presence:** photo and credibility line on homepage screen two, sales page bio intact with evidence link, About deduplicated. Course-week audio remains outstanding (P2.7).

## QA results

Playwright at 1440/768/390 on index, the-unmasked-life, links, evidence, about, contact-success, support: zero horizontal overflow, zero console errors, all local links resolve, MailerLite form IDs and Stan links unchanged, hero and CTAs render inside the first viewport on desktop and mobile (secondary CTA sits just below the fold at 390px, primary fully visible). Remaining em dashes are inside code comments only, not visible copy.

## Fossil pages still needing Leah approval

Deletions: workbooks, course, enrol, portal, consult, course-mark, courses, quiz, podcast; decision on pricing.html; merge-then-delete for services, how-i-work, who-i-work-with; removal of the prototype/wireframe files from the deploy root.

## Remaining blockers

1. Real access control for paid course content (P0 warning note stands; noindex is not protection).
2. Weeks 2 to 4 content migration (course bodies still old sequence).
3. Leah audio and video recordings for the course.
4. Full reference list for the evidence page.
5. Sitewide comma-collision typo pass (P0.7 scope; sales page done, rest outstanding).
6. Favicon still missing (404 on every page).

## What Leah should review first

1. The new homepage hero and ladder (headline wording, prices shown, CTA labels).
2. evidence.html wording (this speaks in her professional voice and mentions AADPA and Healthdirect).
3. The "How the course works" and "Course or PDF?" sections on the sales page.
4. The rebuilt links.html ordering.
5. The fossil-page-cleanup-plan.md deletion list.
