# The Unmasked Life: Course Experience Audit

Audited locally with Playwright at 1440px and 390px: course-dashboard.html, week-1.html, week-1-production-candidate.html, week-2.html, week-3.html, week-4.html, downloads.html, glossary.html, support.html, nc-course.css. July 2026.

**Headline judgement:** the Week 1 production candidate is the only artefact in the course that feels designed rather than assembled. It is roughly 70 percent of the way to a template worth building the whole course on. Everything else in the course area is either an older generation (week-1.html), the wrong content wearing the right titles (weeks 2 to 4), or a portal that talks like a project-management tool (dashboard). The course does not currently feel worth paying for, and the reasons are specific and fixable.

---

## 1. Course architecture

**What exists:** dashboard → four week pages → downloads vault, glossary, support. Plus two parallel Week 1 builds (week-1.html and week-1-production-candidate.html) and an older prototype (week-1-experience-prototype.html).

**Fault 1: the course content does not match the locked sequence.** This is the defining problem. The pages carry TODO comments admitting it:

- week-2.html (titled Masking, Overcompensation and Self-Blame) contains the grief material from the earlier sequence ("What part of the grief is showing up?", "What am I allowed to grieve?").
- week-3.html (titled Support Needs, Executive Function and Environment) contains the masking and shame material ("What mask have you been wearing?").
- week-4.html carries a comment stating it "needs to be rewritten around identity after diagnosis, boundaries... self-trust".

The mismatch propagates outward: the sales page's week milestones, the dashboard's Milestone Matrix, and support.html's week titles all disagree with each other. A learner moving from the sales promise into Week 2 would find a different course than the one they bought. Nothing else in this audit matters as much as this.

**Fault 2: two Week 1s and no decision.** week-1.html (the long accordion document) and the production candidate (the six-scene journey) both exist, and the dashboard links to week-1.html. Until the candidate is promoted or killed, every hour spent on either is at risk.

**Fault 3: no enrolment boundary.** Every course page is publicly served, not gated, not noindexed, with robots.txt missing the actual filenames. There is currently no technical difference between the paid course and the free website.

## 2. Learner journey and emotional pacing

**week-1.html (current live version):** a single very long dark page: video placeholder, six accordion "Learn" sections, reflection prompts, the Life Review exercise, integration task, downloads, scope note. As a document it is thoughtful; as an experience it is a wall. Nothing changes rhythm: every section is the same width, same card style, same density. The 25:00 Pomodoro timer sits beside a page that would take far longer than 25 minutes to read, which quietly contradicts the low-capacity promise. This page is why the course feels flat.

**week-1-production-candidate.html:** a different species. Scene stepper (1 Week Opening → 6 Build Your Snapshot), one scene on screen at a time, route choice up front (Full journey ~45 min, Low-capacity route, Speed-read ~5 min), feelings chips in Scene 5, the Snapshot tool assembling the learner's own words in Scene 6, autosave, copy and print. The emotional sequencing (arrive → something changed → the old story → how the brain manages life → relief, grief and anger → snapshot) is genuinely well designed: it earns the heavy material before presenting it and ends with the learner holding an artefact.

**Where the candidate still falls short of premium:**

1. **Text density per scene is still article-grade.** Scenes present multiple long paragraphs at once. The Inflow-grade version of this shows one to three sentences per beat. The structure is cinematic; the script is still an essay.
2. **Placeholders leak system language into an intimate experience.** "[Complete Scene 3 to fill this]", "AUDIO PLACEHOLDER — NOT YET RECORDED", "Date: [to be confirmed] · Join link: [to be added]". A paying learner should never see the scaffolding.
3. **Leah is absent.** Every "A note from Leah" is an unrecorded placeholder. The single biggest flatness factor in the whole course is that its founder is a text label. Until at least short audio exists, the experience has no human voice.
4. **Em dashes throughout the candidate copy** ("a map that was already there — one that was drawn...", "goes deeper — at your own pace"), violating a stated non-negotiable. The public site had its dashes stripped (badly, creating comma collisions); the candidate never had them stripped at all. Both halves need one careful, hand-checked pass.
5. **Duplicated capacity controls.** A "Low-capacity route" card and a separate "Low-capacity mode" toggle sit on the same screen doing overlapping things. Pick one mental model.
6. **Naming collision with a paid product.** Scene 6 is called "The Life Review Map" and Week 1 also upsells "The Late Diagnosis Life Review" ($19 PDF). Two different things nearly share a name; buyers will conflate the free in-course exercise with the paid product and feel either cheated or confused. Rename the in-course tool (the Snapshot naming is already better) and keep "Life Review" exclusively for the paid PDF.
7. **Desktop right column dies after the route chooser** (large empty area in Scene 1); mobile has the floating "My Snapshot 0 of 5" chip overlapping the video title, and the header wraps untidily at 390px.

**Weeks 2 to 4 pacing:** irrelevant until the content migration happens; they are old documents in the week-1.html style with dead "PDF — coming" resource links.

## 3. Visual quality

The dark cocoa/plum course theme with Cormorant Garamond headings and Atkinson Hyperlegible body is a solid, differentiated foundation: calm, adult, not clinical, not Canva. The candidate's constellation dots and the gradient keyline on the Snapshot card are the beginnings of an ownable visual world (night sky, mapping, markers: it matches the Old Map / New Map metaphor exactly).

But the system is undercommitted. The metaphor is written, not drawn: there is no map illustration, no visual difference between "old map" and "new map" states, no motif carried between scenes, no imagery of any kind anywhere in the course. Every scene is typography on darkness. Premium digital education (School of Life, Inflow, Future ADHD) always has at least one crafted visual asset per unit. One commissioned or carefully built map/constellation illustration system, used across all four weeks, would do more than any amount of CSS refinement.

The dashboard and weeks 2 to 4 use a flatter, boxier version of the theme, so the course currently has two visual generations. The candidate's look should be declared the system.

## 4. Interaction quality

- **Candidate:** route choice, chip selection, snapshot assembly, autosave (localStorage), copy and print. This is the right interaction set: every interaction produces personal meaning rather than engagement for its own sake. Print/save-as-PDF of the Snapshot is the best single feature in the course: it turns reflection into a keepsake.
- **week-1.html and weeks 2 to 4:** interaction is accordions plus a Pomodoro timer. The timer (Start/Reset/Skip) feels bolted on and productivity-flavoured; it is also the only course tool on those pages.
- **Dashboard:** progress cards show demo state ("Week 1 Complete", "Week 2, 40% through") while the header chip says "6% complete": two progress systems disagreeing on a fake number. Milestone Matrix tickboxes are good ("Tick when it feels true for you" is a lovely line); the container names are not (see tone).

## 5. Low-capacity support

The thinking here is well ahead of most commercial courses: three formats per lesson, speed-read routes, reduce-motion and focus-mode toggles, "You do not need to finish this today", the Hit a Wall card, listening-only community participation. This is the course's genuine differentiator and it should be marketed as such. Gaps: the toggles' state does not visibly persist across pages everywhere, the low-capacity route content in the candidate is largely the same text (the route needs genuinely shorter variants, not just fewer scenes), and week-1.html's wall-of-accordions contradicts the promise outright.

## 6. Mobile experience

Candidate at 390px: readable type, sensible stacking, no horizontal overflow. Faults: floating Snapshot chip overlaps content; header brand wraps to two lines with the "Production Candidate" label crowding it; stepper collapses to unlabelled dots (fine, but current-scene name should persist somewhere). Dashboard and weeks 2 to 4 are usable but dense on mobile. Verdict: adequate, not yet the phone-in-bed experience the audience will actually have.

## 7. Weekly continuity

Each candidate week is meant to end by seeding the next ("Coming in Week 2: Masking, Overcompensation and Self-Blame..."), which is right. But continuity artefacts are missing: nothing carries the learner's Week 1 Snapshot forward into Week 2's opening; milestones on the dashboard do not reflect actual scene completion; the weekly catch-up has no date or link. Continuity is asserted, not built.

## 8. The dashboard as premium portal

Not yet. Specific reasons:

1. **Wrong register:** "Sprint Progress Tracker" and "Milestone Matrix" are agile-workplace words inside a course about grief and identity. The learner was promised calm; the labels talk like Jira.
2. **Marketing furniture inside a paid space:** a Subscribe/news signup block and "Media & Press Kit" footer link sit inside the course portal. Paying learners should get a course footer (support, downloads, glossary, contact), not the public site's.
3. **Fake state:** demo progress values and a dead video player with "--:--".
4. **What already works:** the welcome note's content ("The aim is not to finish perfectly."), the resource vault one-click cards, display toggles, and Hit a Wall. The bones are good; the voice and the truthfulness of state need fixing.

## 9. Downloads and resources

The vault currently damages the value story: placeholder rows ("Full Digital Workbook", "Evidence Base and References") sit alongside dead links (journal.html 404s, several workbook links are "#") and three PDFs offered free with "no email required". The three existing PDFs are branded consistently but read as utilitarian documents rather than premium artefacts. For a paid course, the vault is the trophy room; right now it is a storage cupboard mid-renovation. Also: offering the substantive guides free conflicts with the free-resource policy and undercuts the paid ladder.

## 10. Is it worth paying for?

Judged against $197 AUD expectations today: no. What a buyer gets now is one strong-but-unfinished week, three mislabelled old weeks, a portal with fake numbers and no video or audio anywhere. Judged on trajectory: the candidate plus the locked sequence plus recorded Leah presence is a course that could credibly justify $197 and more, because nothing on the market combines this emotional register, this accessibility machinery and Australian nurse-educator credibility.

## Answers to the direct questions

- **Is the Week 1 candidate good enough to become the template?** Yes, structurally: adopt it as the template now, with conditions: cut per-scene text density hard, remove all placeholder leakage, resolve the route/toggle duplication, rename the in-course Life Review Map, strip em dashes, fix the mobile chip collision, and add real Leah audio before beta.
- **Are Weeks 2 to 4 aligned?** No. They are the previous course wearing new titles. The content-migration-map work is the critical path for everything.
- **Does the dashboard feel premium?** No: tone, fake state and marketing furniture. Fixable in a day of work once decided.
- **Do downloads feel valuable?** No: placeholders, 404s and free leakage. The artefacts that exist are competent but not keepsake-grade.
- **Where does it feel generic or flat?** Wherever Leah is absent and text density is high: week-1.html in its entirety, all of weeks 2 to 4, and any candidate scene where three paragraphs arrive at once. The course is flat because it is currently a reading experience about feelings, with no voice, no imagery and no artefact until Scene 6. The Snapshot proves the fix: give the learner things they can hear, see and keep.
