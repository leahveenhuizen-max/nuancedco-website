# Fossil Page Cleanup Plan

**Date:** 2 July 2026 (P1 gold standard build pass)

Status of every page identified as fossil or duplicated in the strategic audit, what was done in P0/P1, and what still needs Leah's approval before deletion. Nothing has been deleted; deletion needs a deliberate decision plus redirects.

## Handled this pass (noindexed, unlinked from the main pathway)

| Page | State after P1 | Recommendation |
|---|---|---|
| workbooks.html | noindex added (P1); all inbound links retargeted (P0) | **Delete** and redirect to links.html |
| course.html | noindex (P0); only linked from other fossils | **Delete** and redirect to the-unmasked-life.html |
| enrol.html | noindex (P0); About's Enrol Now retargeted (P0) | **Delete** and redirect to the-unmasked-life.html |
| portal.html | noindex (P0); only linked from other fossils | **Delete** (no redirect needed; never publicly promoted) |
| consult.html | noindex (P0); links.html card removed (P1) | **Delete** and redirect to book.html |
| course-mark.html | already noindexed; orphaned | **Delete** |
| courses.html | noindex added (P1); robots-disallowed | **Delete** and redirect /courses to the-unmasked-life.html (update _redirects) |
| quiz.html | noindex added (P1); book.html CTA retargeted to the Life Review (P1) | **Decide:** delete, or remap quiz outcomes to the current ladder later. Default: delete |
| podcast.html | noindex added (P1); linked only from workbooks footer | **Delete** or fold content into media.html |
| pricing.html | noindex added (P1); discontinued course replaced with accurate Unmasked Life copy (P0); still orphaned (only reachable via links page URL history) | **Decide:** keep hidden until the ladder pages are final, then either rebuild as the full-ladder pricing page or delete. Default: keep hidden |

## Semi-fossil (still live, no longer in main nav)

| Page | State | Recommendation |
|---|---|---|
| services.html | Nav unified (P1) so it is no longer in the menu; content overlaps how-i-work and workplace | **Merge** the useful copy into a future Work with Leah page, then delete |
| how-i-work.html | Meta description fixed (P0); nav unified (P1); no longer in menu | **Merge and delete** with services.html |
| who-i-work-with.html | Nav unified (P1); no longer in menu | **Merge and delete** with services.html |
| week-1-experience-prototype.html | noindexed; internal prototype in deploy root | **Remove from deploy directory** (keep in content-drafts or archive) |
| week-1-production-candidate.html | noindexed; internal candidate in deploy root | Keep until promoted to week-1.html (P2), then remove |
| _wireframe-renderer.html | noindexed; internal tool in deploy root | **Remove from deploy directory** |

## When deleting (checklist for the future pass)

1. Add a redirect line in `_redirects` for any page that ever appeared in marketing, Instagram or search.
2. Re-crawl internal links afterwards (no page should 404).
3. Remove the corresponding robots.txt lines only after the files are gone.
4. Keep copies in an archive folder outside the deploy root if Leah wants the copy history.

**Needs Leah approval:** every deletion above; the quiz decision; the pricing.html decision.
