# 🚀 GEMINI HOMEPAGE INDEXER — QUICK REFERENCE

## One-Time Setup (5 minutes)

```bash
# 1. Clone/navigate to project
cd ~/Desktop/Nuance/nuancedco-deploy

# 2. Create Python virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Get API key at: https://makersuite.google.com/app/apikey

# 5. Set environment variable (macOS/Linux)
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
# Add to ~/.zshrc for persistence: echo "export GEMINI_API_KEY='..'" >> ~/.zshrc

# 6. Update homepage URL in script
# Edit gemini_homepage_indexer.py, line 27:
#   HOMEPAGE_URL = "https://yourdomain.com"
```

---

## Running the Indexer

```bash
# Activate virtual environment (if not active)
source venv/bin/activate

# Run the indexer
python3 gemini_homepage_indexer.py

# The script will:
# 1. Fetch your homepage
# 2. Extract clean text
# 3. Send to Gemini
# 4. Start interactive chat mode
```

---

## Interactive Chat Mode

Once the script is running:

```
🤖 Ask Gemini about the homepage: What does Nuanced Co. do?
✨ [Gemini responds based only on homepage content]

🤖 Ask Gemini about the homepage: How do I enroll?
✨ "I only have access to our homepage information..."

Type 'exit' to quit
```

---

## File Reference

| File | Purpose |
|------|---------|
| `gemini_homepage_indexer.py` | Main script (production-ready) |
| `robots.txt` | Crawler control (deploy to web root) |
| `requirements.txt` | Python dependencies |
| `GEMINI_SETUP_GUIDE.md` | Full documentation |
| `GEMINI_QUICK_REFERENCE.md` | This cheat sheet |

---

## Verify Setup

```bash
# 1. Check dependencies
python3 -c "import requests, bs4, google.generativeai; print('✅ OK')"

# 2. Verify API key is set
echo $GEMINI_API_KEY  # Should print your key

# 3. Test script execution
python3 gemini_homepage_indexer.py
# Should complete with "✅ Indexing complete!"

# 4. Check robots.txt is accessible
curl https://yourdomain.com/robots.txt | head -5
```

---

## Deployment Options

### Option A: Cron Job (Reindex Daily)

```bash
crontab -e
# Add: 0 2 * * * cd /path/to/project && /path/to/venv/bin/python3 gemini_homepage_indexer.py
```

### Option B: Docker

```bash
docker build -t gemini-indexer .
docker run -e GEMINI_API_KEY="key" gemini-indexer
```

### Option C: AWS Lambda

```bash
# Upload as Python function with environment variable
GEMINI_API_KEY = your_api_key
```

---

## Common Commands

```bash
# Activate virtual environment
source venv/bin/activate

# Deactivate virtual environment
deactivate

# Update dependencies
pip install --upgrade -r requirements.txt

# Check what's installed
pip list

# Uninstall everything (if needed)
pip uninstall -r requirements.txt -y

# Run with explicit Python path
/path/to/venv/bin/python3 gemini_homepage_indexer.py
```

---

## Environment Variables

### Required

```bash
GEMINI_API_KEY=YOUR_ACTUAL_API_KEY
```

### Optional Additions

```bash
# Log to file instead of stdout
GEMINI_LOG_FILE=/var/log/gemini_indexer.log

# Custom homepage URL (overrides script default)
HOMEPAGE_URL=https://yourdomain.com

# Model selection
GEMINI_MODEL=gemini-2.5-flash
```

---

## Troubleshooting Quick Fixes

| Problem | Solution |
|---------|----------|
| "GEMINI_API_KEY not found" | `export GEMINI_API_KEY="key"` |
| "Module not found" | `pip install -r requirements.txt` |
| "Connection timeout" | Check internet, verify domain URL |
| "403 Forbidden" | Check robots.txt allows your User-Agent |
| "Content exceeds limit" | Increase MAX_CONTENT_LENGTH in script |
| "Gemini returns course info" | Check system prompt is applied correctly |

---

## Security Checklist

- [ ] API key is in environment variable (NOT in code)
- [ ] robots.txt deployed to web root
- [ ] URL validation is enabled in script
- [ ] Excluded content keywords are set
- [ ] No sensitive credentials in files
- [ ] Script logs don't include API key
- [ ] Use HTTPS for all URLs

---

## Testing Checklist

- [ ] Script runs without errors
- [ ] Gemini responds to test query
- [ ] robots.txt blocks /courses path
- [ ] Interactive mode works
- [ ] URL validation rejects non-homepage
- [ ] Content filtering works
- [ ] Token counts are reasonable

---

## API Costs (Google AI Studio)

- **Free Tier:** 60 requests/minute
- **Cost:** Currently free for Gemini API
- **Limits:** Check https://ai.google.dev/pricing

Monitor usage:
- https://makersuite.google.com/app/apikey (request count)
- Google Cloud Console (if using paid tier)

---

## Support & Resources

- **Official Docs:** https://ai.google.dev/
- **GitHub Issues:** Report bugs
- **Google Community:** ai.google.dev/forums
- **robots.txt Help:** https://www.robotstxt.org/

---

## Version Info

- **Script Version:** 1.0
- **Python Required:** 3.8+
- **Gemini Model:** gemini-2.5-flash
- **Last Updated:** June 6, 2026

---

## Next Steps After Setup

1. ✅ Run the indexer: `python3 gemini_homepage_indexer.py`
2. ✅ Test interactive chat
3. ✅ Deploy robots.txt to production
4. ✅ Set up cron job for automated reindexing
5. ✅ Monitor API usage and logs

---

**Need help?** See `GEMINI_SETUP_GUIDE.md` for detailed instructions.
