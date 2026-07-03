# Nuanced Co. Website Audit

Full audit of the public website, inspected locally (python3 http.server, Playwright) at 1440px, 1024px, 768px and 390px, July 2026. Verdicts use four options: keep, merge, rewrite, remove.

**Reading the overall picture first:** this is not one website. It is at least three websites from three eras layered on top of each other: an early "consultancy practice" era (how-i-work, who-i-work-with, quiz, consult, pricing, workbooks), a mid-era course funnel (course.html, enrol, portal, courses, course-mark), and the current era (index, the-unmasked-life, waitlist pages, course dashboard and weeks). Every era is still reachable. The single highest-value move available is deletion.

---

## index.html (Homepage)

- **Current purpose:** brand front door; route visitors to guides, consulting or the course.
- **Actual impression at 1440px:** the entire first viewport is the watercolour blob mark, the wordmark and "Geelong · Australia". No headline, no promise, no CTA except the nav's Book a Call. The real headline ("You don't need more discipline. You need better structure.") only appears after scrolling, behind a reveal animation. A first-time visitor learns nothing before the fold. The rest of the page is long, with large near-empty dark bands where scroll-reveal content sits invisible until triggered.
- **Visual quality:** the palette (cream, dark cocoa, plum, ochre) and serif are pleasant but the page reads as a template with a logo dropped in. The blob mark is washed out and does not survive small sizes.
- **Copy quality:** the good lines are genuinely good ("Late diagnosis is not a personality flaw. It is the absence of language you always deserved."). But comma-collision typos from stripped dashes appear in body copy, and the three pathway cards are text-dense with near-identical visual weight.
- **CTA clarity:** four competing CTAs (Book a Call, View Guides, Join the Waitlist twice for two different waitlists: course and community). The two waitlists are not distinguishable to a visitor.
- **Trust quality:** Leah barely appears. No credentials above the footer. No evidence markers.
- **Mobile quality:** sound; no horizontal overflow; headline legible.
- **Product-ladder clarity:** weak. Guides CTA goes straight to Stan (off-site) with no explanation of what a guide is; the course price appears here and nowhere else.
- **Verdict: rewrite** (structure and hero; keep palette, voice and the quote sections).
- **Top issues:** empty first viewport; two indistinguishable waitlists; scroll-reveal dead zones; typos; founder invisible.
- **Recommended fixes:** put headline, one-line positioning, and a single primary CTA in the first viewport with the logo as a supporting element; collapse to one primary CTA per screen; name Leah with credentials in the first two screens; fix stripped-dash typos.

## about.html

- **Current purpose:** founder credibility.
- **Actual impression:** the page introduces Leah twice: a "Hey! I'm Leah…" hero section and then a second "Hi, I'm Leah." section with the same photograph repeated and overlapping copy. It reads as an unfinished merge of two drafts. The nav renders differently from the homepage (items wrap with stray dropdown arrows), which signals template drift.
- **Visual quality:** the arched photo treatment with the orange underline has real personality; best visual moment on the site. Duplicated photo undercuts it.
- **Copy quality:** strong raw material; credential chips (Registered Nurse AHPRA, Mental Health First Aid Facilitator, Master of Counselling in progress, AuDHD lived experience) are exactly right. Duplication destroys the flow.
- **CTA clarity:** "Enrol Now" links to enrol.html, an obsolete funnel page for a course that is waitlist-only. Commercially wrong and trust-damaging.
- **Trust quality:** high potential, undermined by the broken structure.
- **Mobile quality:** acceptable.
- **Verdict: rewrite** (single narrative, one photo used once, keep the chips, CTA to the course page or waitlist).
- **Top issues:** duplicated sections; wrong CTA; nav drift.

## services.html

- **Current purpose:** unclear; overlaps how-i-work and workplace.
- **Actual impression:** a problem/solution grid ("Being told to try harder" / "Brain-based consultancy") with reasonable copy but no pricing, no booking path except the generic footer, and total overlap with how-i-work.html and workplace.html.
- **Visual/copy quality:** serviceable, generic.
- **Product-ladder clarity:** contributes to the three-pages-say-the-same-thing problem (services, how-i-work, who-i-work-with).
- **Verdict: merge** into a single "Work with Leah" page alongside book.html content; then remove.
- **Top issues:** redundancy; no path to action; title says "Services & How I Work" confirming the overlap.

## courses.html

- **Current purpose:** course index.
- **Actual impression:** a thin stub: one card for The Unmasked Life and a "To be announced" card whose More Information link is a dead "#". Robots.txt disallows /courses, so even the site's own configuration considers it not ready.
- **Verdict: remove** (redirect to the-unmasked-life.html). One course does not need an index page.
- **Top issues:** dead link; stub content; duplicated role with the-unmasked-life.html.

## course.html

- **Current purpose:** old long-form course sales page (1,752 lines, the largest file on the site).
- **Actual impression:** an entire previous generation of the course offer, still live, linking to portal.html and consult.html. Not linked from current nav but reachable and indexed history.
- **Verdict: remove** (redirect to the-unmasked-life.html). Its existence guarantees version drift.

## the-unmasked-life.html

- **Current purpose:** current course sales page. The most important commercial page on the site.
- **Actual impression:** structurally the best public page: dark hero, "You have a diagnosis. Now what?", four week cards, what's included, bio, scope note, waitlist close. It looks organised and calm.
- **Critical content fault:** the week cards carry the old sequence's content under the new titles. Week 2 (Masking) shows the grief milestone; Week 3 (Support Needs) shows the masking/shame milestone. Anyone comparing the sales page to the course will find the promise wrong.
- **Copy quality:** good bones, but comma-collision typos ("your actual life,the past", "education,not a symptom checklist", "Registered Nurse,Neurodivergent Consultant,Nuanced Co.") sit in the most-read sentences.
- **Trust quality:** the Leah bio block has an empty grey placeholder circle where her photo should be. On the page asking for money, the founder is faceless.
- **CTA clarity:** good (waitlist, consistently). But no price anywhere on the page while the homepage says "from $197 AUD"; a buyer cannot confirm the price on the sales page.
- **Product-ladder clarity:** no mention of the Reader Edition, Companion Guides or the Life Review; the ladder's flagship page ignores the rest of the ladder.
- **Mobile quality:** good.
- **Verdict: rewrite** (content corrections and additions on the existing structure).
- **Top issues:** wrong week milestones; missing photo; missing price; typos; no ladder context.

## the-unmasked-life-coming-soon.html

- **Current purpose:** course waitlist capture (MailerLite, wired correctly).
- **Actual impression:** functional, noindexed, does its job. Thin but acceptable.
- **Verdict: keep** (light polish; consider folding capture into the sales page at launch).

## workbooks.html

- **Current purpose:** none. Legacy page titled "The Nuanced Co. Strategy Workbooks" with the old first-person nav ("How I Work", "Who I Work With"), the homepage's meta title, and a newsletter form.
- **Actual impression:** a fossil from a previous business model, still linked from index.html, how-i-work.html and who-i-work-with.html.
- **Verdict: remove** (redirect to the future guides/resources page). Every link to it from live pages must be updated.

## downloads.html

- **Current purpose:** course resource vault, but publicly reachable.
- **Actual impression:** a mixed pile: three substantive ADHD PDF guides offered free with "No email required", placeholder entries for the full workbook and journal, week workbooks and quick references (several as dead links), and a "View" link to journal.html which does not exist (404).
- **Policy conflict:** the meta description says "Free guides, workbooks, and resources" and the page offers substantive ADHD education (Burnout guide, AuDHD Executive Dysfunction guide) free. The free-resource policy limits free items to crisis directories, service navigation and brief signposting. The Diagnosis in Australia guide arguably qualifies as service navigation; the other two do not.
- **Verdict: rewrite** (split into a public resources page holding only policy-compliant free items, and an in-course vault for everything else).
- **Top issues:** 404 to journal.html; policy conflict; placeholder rows visible; course assets publicly downloadable.

## pricing.html

- **Current purpose:** pricing for sessions, guides and course.
- **Actual impression:** orphaned (no internal page links to it; only the links.html external URL). It advertises "Understanding Who You Are After Your Diagnosis", a 7-module course with ADHD and AuDHD versions, which no longer exists. Session CTAs are mailto links. The page contradicts the homepage's $197 course claim by not mentioning The Unmasked Life at all.
- **Verdict: remove or fully rewrite.** If sessions remain a real offer, pricing content belongs on the Work with Leah page; a standalone pricing page is only worth keeping if it lists the entire current ladder accurately.
- **Top issues:** obsolete course; orphaned; mailto CTAs; contradicts the ladder.

## faq.html

- **Current purpose:** common questions.
- **Actual impression:** solid. Scope answer ("Is this therapy or clinical support?") is exactly right. Questions map to the current era mostly.
- **Issues:** "What digital guides are available?" answer routes to links.html rather than a guides page; no question covering the Reader Edition or Companion Guides; accordion "+" buttons could announce state better for screen readers.
- **Verdict: keep** (extend for the full product ladder at launch).

## book.html

- **Current purpose:** consultation bookings via Netlify form.
- **Actual impression:** one of the better pages: three clear enquiry types, expectations set, scope-safe copy, working form with honeypot, success redirect to /thank-you (exists in _redirects).
- **Issues:** "Take the free quiz" routes into the old quiz funnel; session prices absent (they live on the orphaned pricing page).
- **Verdict: keep** (light edits: add prices or a price range, retire the quiz link).

## contact.html

- **Current purpose:** general contact.
- **Critical fault:** the form posts with action="/contact-success", and neither contact-success.html nor a redirect entry exists. Every submitted enquiry ends on a 404. The submission likely still reaches Netlify, but the sender sees an error and cannot know it worked.
- **Verdict: keep with immediate fix** (create the success page or point the action at /thank-you). This is a live lead-loss bug.

## links.html

- **Current purpose:** Instagram bio link page.
- **Actual impression:** functional but off-brand: emoji bullets (🌿 🏢 💰 📄 🎤) against the no-emoji rule, and it leads with consultancy and pricing rather than the Life Review, which is presumably what Instagram followers most want.
- **Verdict: rewrite** (small job: remove emojis, reorder to Life Review first, match site typography).

## support.html

- **Current purpose:** crisis and support signposting for course participants. Policy-critical page.
- **Actual impression:** the strongest-purposed page on the site: 000, Lifeline, Beyond Blue, Suicide Call Back Service, ND-specific supports, practitioner-finding pathways, clear scope statement, and gentle "struggling with the course" options. This is exactly what the free-resource policy wants.
- **Critical fault:** the week navigation lists the old course titles (It Finally Makes Sense; Grief for What Could Have Been; The Mask, the Shame and the Big Feelings; Building a Life That Fits). A distressed learner clicking through sees titles that match nothing in their course.
- **Verdict: keep with immediate title fix.**

## privacy.html / refund-policy.html / terms-of-service.html

- **Current purpose:** legal.
- **Actual impression:** genuinely good. The terms' educational-scope and no-professional-relationship clauses are well drafted for the education-only model; refunds address Australian Consumer Law and digital products sensibly; privacy covers OAIC.
- **Issues:** minor: they should be checked against the final product ladder names before launch (they predate the Reader Edition naming).
- **Verdict: keep.**

## how-i-work.html / who-i-work-with.html

- **Current purpose:** old consultancy-era explainers, still in the current nav.
- **Critical fault:** how-i-work.html's meta description calls Nuanced Co. an "ADHD consulting and counselling practice". Nuanced Co. must never be described as a counselling practice; this is the most serious single line of copy on the site and it is in a search-visible meta tag.
- **Actual impression:** long, animated, first-person pages ("Support that fits how you actually think") that duplicate services.html, carry the homepage's meta title, and still link to workbooks.html.
- **Verdict: merge** the genuinely good "how I work" principles into the Work with Leah page; then remove both. Fix the meta description immediately regardless.

## workplace.html

- **Current purpose:** workplace consulting.
- **Actual impression:** surprisingly strong positioning ("Move beyond awareness. Build genuine psychological safety."), correct legislative framing for Australia, clear CTA. Slightly generic visually but coherent.
- **Verdict: keep** (align nav and footer; connect from the homepage pathway cards properly).

## community-waitlist.html (+ success pages)

- **Current purpose:** community updates list; MailerLite wired; noindexed appropriately.
- **Actual impression:** fine. The problem is upstream: the homepage presents this waitlist and the course waitlist with identical-looking CTAs.
- **Verdict: keep** (differentiate labelling upstream).

## quiz.html / consult.html / enrol.html / portal.html / course-mark.html / media.html / podcast.html

- **quiz.html:** old funnel lead magnet ("Where should we send your results?"). Competent but belongs to the consultancy era; if kept, it needs its recommendations remapped to the current ladder. **Merge or remove.**
- **consult.html:** old consult page reachable from course.html/portal.html only. **Remove.**
- **enrol.html:** sells "Late-Diagnosed Adult Integration Course" with "Begin Your The Unmasked Life™" (grammar error); linked from about.html's Enrol Now. **Remove immediately** (redirect to the-unmasked-life.html).
- **portal.html:** an entire old course portal (86KB) still live and linked from enrol/course. **Remove.**
- **course-mark.html:** orphaned scratch page. **Remove.**
- **media.html:** decent speaking/press page; keep if media work is a real goal, otherwise trim. **Keep.**
- **podcast.html:** stub. **Remove or fold into media.html.**

---

## Cross-site systemic issues

1. **Three navigation systems coexist** (We/I voice, different menus, different footers). A visitor crossing pages feels the seams immediately.
2. **Stripped-dash typos sitewide.** A find-replace that removed em dashes left "word,word" collisions across index, the-unmasked-life, how-i-work and the course pages. There are dozens. This single class of typo does more damage to the premium feel than any design choice.
3. **The paid course is public.** week-1 to week-4, course-dashboard and the PDFs are served openly, are not noindexed, and robots.txt does not cover them (it disallows /dashboard but the file is course-dashboard.html; it disallows /courses and /course.html but not week-*.html). Anything paid must be gated or at minimum noindexed before traffic grows.
4. **Trademark inconsistency:** ™ appears on most but not all uses of The Unmasked Life; decide once (recommendation: drop ™ everywhere unless there is a registered mark; unregistered ™ reads as small-business insecurity in a premium context).
5. **Favicon missing** (404 on every page load).
6. **Two waitlists, one visual language.** Course waitlist and community updates list need distinct names and buttons.
7. **Orphan and fossil pages create legal/brand risk** disproportionate to their traffic: they carry obsolete offers, scope-violating descriptions and broken CTAs. Deletion is the cheapest premium upgrade available.
