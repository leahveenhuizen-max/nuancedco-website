#!/usr/bin/env node
// Build the five sellable Unmasked Life PDFs.
// Usage: node pdf-tools/build-pdfs.mjs   (regenerates everything)
import { execFileSync } from "node:child_process";
import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { createServer } from "node:http";
import path from "node:path";
import { chromium } from "playwright-core";
import { PDFDocument } from "pdf-lib";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.dirname(HERE);
const BUILD = path.join(HERE, "build");
const OUT = path.join(ROOT, "pdf-exports");
mkdirSync(OUT, { recursive: true });

console.log("Extracting manuscript from week pages...");
execFileSync("python3", [path.join(HERE, "extract.py")], { stdio: "inherit" });

const DOCS = [
  ["welcome", "The-Unmasked-Life-00-Welcome-Start-Here.pdf"],
  ["week-1", "The-Unmasked-Life-Week-1-The-Late-Diagnosis-Disruption.pdf"],
  ["week-2", "The-Unmasked-Life-Week-2-Masking-Overcompensation-and-Self-Blame.pdf"],
  ["week-3", "The-Unmasked-Life-Week-3-Support-Needs-Executive-Function-and-Environment.pdf"],
  ["week-4", "The-Unmasked-Life-Week-4-Rebuilding-Self-Trust-After-Diagnosis.pdf"],
];

const FOOTER = `
<div style="width:100%;font-family:Helvetica,Arial,sans-serif;font-size:6.5pt;letter-spacing:.04em;color:#8a7f76;
  padding:0 20mm;display:flex;justify-content:space-between;align-items:center;">
  <span>The Unmasked Life &middot; Nuanced Co. &middot; nuancedco.com.au</span>
  <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
</div>`;

// Serve pdf-tools/ over http so Chrome loads the @font-face files reliably.
const MIME = { ".html": "text/html", ".css": "text/css", ".ttf": "font/ttf" };
const server = createServer((req, res) => {
  const p = path.join(HERE, decodeURIComponent(new URL(req.url, "http://x").pathname));
  try {
    res.setHeader("Content-Type", MIME[path.extname(p)] || "application/octet-stream");
    res.end(readFileSync(p));
  } catch { res.statusCode = 404; res.end(); }
});
await new Promise(r => server.listen(0, "127.0.0.1", r));
const BASE = `http://127.0.0.1:${server.address().port}/build`;

const browser = await chromium.launch({ channel: "chrome" });
const page = await browser.newPage();

for (const [slug, outName] of DOCS) {
  // 1. cover — full bleed, no footer
  await page.goto(`${BASE}/${slug}-cover.html`, { waitUntil: "networkidle" });
  const coverPdf = await page.pdf({
    format: "A4", printBackground: true,
    margin: { top: 0, bottom: 0, left: 0, right: 0 },
  });
  // 2. body — cream pages, branded footer with page numbers
  await page.goto(`${BASE}/${slug}-body.html`, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  const bodyPdf = await page.pdf({
    format: "A4", printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: "<span></span>",
    footerTemplate: FOOTER,
    margin: { top: "20mm", bottom: "18mm", left: "20mm", right: "20mm" },
  });
  // 3. merge cover + body
  const merged = await PDFDocument.create();
  for (const buf of [coverPdf, bodyPdf]) {
    const src = await PDFDocument.load(buf);
    const pages = await merged.copyPages(src, src.getPageIndices());
    pages.forEach(p => merged.addPage(p));
  }
  merged.setTitle(outName.replace(/\.pdf$/, "").replace(/-/g, " "));
  merged.setAuthor("Leah Veenhuizen — Nuanced Co.");
  merged.setProducer("Nuanced Co. PDF pipeline");
  const bytes = await merged.save();
  const outPath = path.join(OUT, outName);
  writeFileSync(outPath, bytes);
  console.log(`✓ ${outName} (${merged.getPageCount()} pages, ${(bytes.length / 1024).toFixed(0)} KB)`);
}

await browser.close();
server.close();
console.log("Done. Output in pdf-exports/");
