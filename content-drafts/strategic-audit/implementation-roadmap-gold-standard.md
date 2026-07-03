# Implementation Roadmap: Gold Standard

Priority-ordered roadmap from the July 2026 strategic audit. Effort: S (under 1 hour), M (half day), L (1 to 3 days), XL (a week or more). Risk describes the risk of doing the item, not of skipping it.

---

## P0: Stop, protect or clarify before more building

| # | Page/asset | Issue | Action | Why it matters | Effort | Risk | Depends on | Leah approval |
|---|---|---|---|---|---|---|---|---|
| P0.1 | how-i-work.html meta description | Describes Nuanced Co. as an "ADHD consulting and counselling practice" | Remove "counselling practice" wording immediately | Scope/regulatory positioning: Nuanced Co. must never imply counselling; this is in a search-engine-visible tag | S | None | Nothing | Notify, then fix (wording of replacement: yes) |
| P0.2 | contact.html | Form action posts to /contact-success which does not exist; every sender lands on a 404 | Point action to /thank-you or create contact-success.html | Live lead loss and trust damage on a working site | S | None | Nothing | No |
| P0.3 | week-1 to week-4, course-dashboard, PDFs | Paid course fully public, indexable; robots.txt misses the real filenames | Add noindex meta to all course pages now; plan real gating for beta | Protects the paid product before any traffic or launch buzz | S (noindex) / XL (gating) | Low | Gating depends on platform choice | Gating approach: yes |
| P0.4 | Weeks 2 to 4 + sales page + support.html + dashboard | Locked sequence titles sit on old-sequence content; week titles disagree across surfaces | Freeze all new feature work until content migration (content-migration-map.md) is executed; fix support.html titles and sales-page milestones as the first step | Selling one course and delivering another is the single largest commercial and trust risk | S (titles) / XL (full migration) | Medium (content work needs care) | Locked sequence (done) | Migrated content: yes |
| P0.5 | pricing.html, enrol.html, portal.html, course.html, workbooks.html, consult.html, course-mark.html, courses.html | Fossil pages sell discontinued offers and contradict the ladder | Remove and redirect (_redirects entries); update inbound links (about.html Enrol Now, index/how-i-work/who-i-work-with links to workbooks.html) | Deletion is the fastest premium and clarity upgrade available | M | Low (redirects preserve any bookmarks) | Decide session-pricing home first (see P1.6) | Yes (list of deletions) |
| P0.6 | downloads.html | Links to journal.html (404); dead "#" workbook links; placeholder rows public | Remove dead links and placeholder rows from anything reachable | 404s inside a paid experience destroy the premium claim | S | None | Nothing | No |
| P0.7 | Whole site + candidate | Em dashes in course candidate; comma-collision typos sitewide from an earlier dash-stripping pass | One careful copy pass: restore intended punctuation as commas/colons/full stops with correct spacing | Brand non-negotiable; currently violated in both directions | M | Low (hand-check, no blind find-replace) | Nothing | Spot-check sample: yes |

## P1: Must fix before launch or significant traffic

| # | Page/asset | Issue | Action | Why it matters | Effort | Risk | Depends on | Leah approval |
|---|---|---|---|---|---|---|---|---|
| P1.1 | index.html | First viewport is logo-only; headline hidden behind scroll reveal; four competing CTAs; two look-alike waitlists | Rebuild hero (headline, positioning line, single CTA); collapse CTA hierarchy; name the two lists differently | The most valuable screen on the site currently says nothing | L | Medium (homepage sensitivity) | Ladder decisions (P1.6) | Yes |
| P1.2 | the-unmasked-life.html | Old milestones under new titles; no price; bio photo placeholder; typos | Correct week cards to locked sequence; add price and founding-beta framing; add real photo; fix copy | This is the money page | M | Low | P0.4 titles; price decision | Yes (price/beta terms) |
| P1.3 | about.html | Duplicated intro sections, same photo twice, Enrol Now to dead funnel | Rewrite as single narrative with credential chips; CTA to course page | Founder credibility is the trust engine | M | Low | P0.5 | Yes (her story, her words) |
| P1.4 | The Late Diagnosis Life Review | No on-site page; $19 visible only on links.html; sold sight-unseen | Create product page: what it is, who for, 3+ interior previews, Stan buy button | First paid rung must be visible and previewable | M | Low | Interior preview images | Yes |
| P1.5 | links.html | Emojis; consultancy-first ordering | Strip emojis, reorder (Life Review first), match brand type | Highest-traffic touchpoint for Instagram audience | S | None | Nothing | No |
| P1.6 | Product ladder | Reader Edition and Companion Guides absent from public site; session pricing homeless after pricing.html removal | Decide ladder presentation: Guides index page + Reader Edition page (even as "coming") + sessions folded into Work with Leah page | A ladder that exists only in planning documents converts nobody | L | Medium | Product naming/pricing decisions | Yes |
| P1.7 | Navigation and footer | Three nav systems, we/I drift, workbooks links | Unify to one five-item nav and one footer sitewide | Coherence is the cheapest premium signal | M | Low | P0.5 deletions | Structure: yes |
| P1.8 | Sitewide | Favicon 404; ™ inconsistency | Add favicon; decide ™ policy once | Small trust abrasions | S | None | ™ decision | ™: yes |

## P2: Must fix before course beta

| # | Page/asset | Issue | Action | Why it matters | Effort | Risk | Depends on | Leah approval |
|---|---|---|---|---|---|---|---|---|
| P2.1 | week-1-production-candidate.html | Two Week 1s; dashboard points at the old one | Promote candidate to week-1.html (retire old page and prototype) | Ends split effort; declares the template | M | Medium (verify all inbound links) | P2.2 to P2.4 polish | Yes |
| P2.2 | Candidate copy | Scene text at article density; placeholder strings learner-visible; "[Complete Scene 3...]" system language | Density cut (one idea per beat); replace placeholder strings with warm empty-states | The difference between a document and an experience | L | Medium | Nothing | Yes (copy) |
| P2.3 | Candidate UX | Low-capacity route vs low-capacity toggle duplication; mobile Snapshot chip overlaps content; header wrap at 390px; dead right column in Scene 1 | Resolve to one capacity model; fix mobile collisions | Mobile is the primary context | M | Low | Nothing | Capacity model: yes |
| P2.4 | Course naming | "The Life Review Map" (free, in-course) vs "The Late Diagnosis Life Review" (paid PDF) | Rename in-course tool (extend the Snapshot naming) | Buyers will conflate free tool and paid product | S | Low | Nothing | Yes |
| P2.5 | Weeks 2 to 4 | Old content, old template, dead resource links | Rebuild on candidate template with migrated locked-sequence content | The product is four weeks, not one | XL | Medium | P0.4, P2.1 | Yes |
| P2.6 | course-dashboard.html | Fake progress (6% vs Week 2 40%); "Sprint Progress Tracker"/"Milestone Matrix" language; Subscribe block and press-kit link in portal; dead video player | True state wired to localStorage; calm labels; course-only footer; remove player until video exists | The portal is the daily face of the product | L | Medium | P2.1 | Label copy: yes |
| P2.7 | Leah presence in course | All notes-from-Leah are unrecorded placeholders | Record short audio notes (phone-quality is acceptable for beta) for every note slot in Week 1 minimum | The founder's voice is the anti-flatness asset | M (per week) | Low | Script sign-off | Yes (she records) |
| P2.8 | downloads.html split | Paid course assets and "free" substantive guides mixed on a public page | Public page keeps only policy-compliant free items (service navigation, crisis directories); vault becomes course-internal | Free-resource policy compliance and ladder integrity | M | Medium (decide fate of Burnout/AuDHD guides: paid, in-course, or gated) | P1.6 | Yes |
| P2.9 | Weekly catch-up | "[to be confirmed] · [to be added]" in learner-facing card | Either schedule it for beta or remove the card | Placeholder promises break trust | S | None | Beta logistics | Yes |

## P3: Should improve before wider paid launch

| # | Page/asset | Issue | Action | Why it matters | Effort | Risk | Depends on | Leah approval |
|---|---|---|---|---|---|---|---|---|
| P3.1 | Evidence | No public citations anywhere despite "research-informed" positioning | Public Evidence page (APA 7); references + "reviewed [date]" per course week; sourced claims on sales page | The cheapest unclaimed differentiator for an RN-led brand | L | Low (needs literature time) | Course content final | Yes (sources) |
| P3.2 | Visual motif | Map/constellation world written but not drawn | Develop the illustration system (hero, dividers, week maps, PDF covers); refresh the blob mark toward contour forms | The ownable device that ends generic-ness | XL | Medium (creative direction) | P1.1 live first | Yes |
| P3.3 | Paid PDFs | Existing guides utilitarian; no interior previews at points of sale | Re-typeset to keepsake grade in the map world; shoot previews | Future ADHD proves the premium-PDF ceiling | XL | Low | P3.2 | Yes |
| P3.4 | Snapshot artefact | Functional but plain; the keepsake potential untapped | Design pass on Snapshot layout + print CSS | Most shareable object in the course | M | Low | P2.1 | Yes |
| P3.5 | Real gating | Noindex is not access control | Choose and implement delivery (simplest viable: paid-link delivery of a members URL space, or a proper course platform decision) | Beta can run on trust; launch cannot | XL | High (platform choice shapes everything) | P0.3 decision | Yes |
| P3.6 | faq.html | No ladder questions; accordion a11y | Extend FAQ; aria state on accordions | Pre-sale objection handling | S | None | P1.6 | Copy: yes |
| P3.7 | Practitioner clarity | Nothing tells a GP/psychologist what this is for referral | One-paragraph "for practitioners" section (About or FAQ) | Referral channel and credibility | S | Low (scope wording care) | Nothing | Yes |
| P3.8 | Continuity | Week N artefact not reflected in Week N+1 opening | Carry Snapshot lines forward via localStorage | Turns four pages into one journey | M | Low | P2.5 | No |

## P4: Future enhancements

| # | Asset | Action | Why | Effort | Approval |
|---|---|---|---|---|---|
| P4.1 | Video | Record week lesson videos (candidate already has chaptered player slots) | Completes the three-format promise | XL | Yes |
| P4.2 | Community | Real weekly catch-up cadence + moderated space (currently waitlist) | Retention and word of mouth | XL | Yes |
| P4.3 | Reader Edition production | Typeset from final course content | Second revenue rung | XL | Yes |
| P4.4 | Companion Guide line extension | Additional guides beyond Grieving the Life You Thought You Had | Ladder depth | XL | Yes |
| P4.5 | Testimonials | Collect founding-beta stories (with consent process) | Social proof currently absent | M | Yes |
| P4.6 | Analytics | Privacy-respecting analytics + monthly link/form/placeholder crawl (trust standard test) | Keeps the truth pass permanent | S | Yes (tool choice) |
| P4.7 | Workplace tier | Case study + one-pager PDF for workplace.html | B2B revenue with zero ladder confusion | M | Yes |

---

**Sequencing note:** P0 is one to two focused days and requires almost no design. Nothing in P1 to P3 should start before P0.4 (content alignment) and P0.5 (deletions) are agreed, because both change what every later page says.
