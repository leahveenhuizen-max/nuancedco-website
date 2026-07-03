# Paid Content Access Warning

**Date:** 2 July 2026 (P0 truth pass)

## What was done in the P0 pass

- `noindex, nofollow` meta tags added to: course-dashboard.html, week-1.html, week-2.html, week-3.html, week-4.html, downloads.html, glossary.html, week-1-production-candidate.html, _wireframe-renderer.html, course.html, portal.html, enrol.html, consult.html. (week-1-experience-prototype.html and course-mark.html already had them.)
- robots.txt updated to disallow the actual course delivery filenames (course-dashboard.html, week-*, downloads.html, glossary.html, consult.html, course-mark.html, _wireframe-renderer.html) in all three crawler blocks, and the sitemap URL corrected to nuancedco.com.au.
- Confirmed no current public page (homepage, about, sales page, FAQ, etc.) links into the course delivery pages.

## What this does and does not do

**It reduces discovery only. It is not access protection.**

- noindex asks search engines not to list the pages. Compliant crawlers honour it; nothing else does.
- robots.txt asks crawlers not to visit. It is advisory, and it also acts as a public list of the URLs it names.
- Anyone with a direct URL (shared link, browser history, guess) can still open every course page and download every PDF, free, right now.
- Static HTML on Netlify cannot check who is enrolled. There is no login, no session, no entitlement check anywhere in this build.

## What is still exposed

- All four week pages, the dashboard, the vault (downloads.html), the glossary, and the three PDF guides are openly served to anyone who has or finds the URL.
- The Week 1 production candidate and prototype remain publicly served internal files (now noindexed) until removed from the deploy directory.

## Before paid launch, Leah needs a real access method

Options to evaluate later (not implemented in this pass, deliberately; a fake gate would imply security that does not exist):

- Netlify Basic Auth or Netlify Identity with gated paths
- A membership layer such as Memberstack or Outseta over the existing static pages
- A dedicated course platform (Podia, Teachable, Kajabi or similar)
- Shopify customer accounts, or delivery through Stan's own paid-content delivery
- Signed/expiring download links for the paid PDFs

**Decision needed from Leah before beta invitations go out:** which access method, and whether beta runs on trust (unlisted URLs) with eyes open, or behind real authentication.
