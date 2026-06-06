# NUANCED CO. — GEMINI API INTEGRATION GUIDE
## Homepage-Only Indexing for AI-Powered Responses

**Last Updated:** June 6, 2026  
**Author:** Senior Software Engineer  
**Purpose:** Enable Google Gemini API to access ONLY your main homepage for AI responses

---

## 📋 TABLE OF CONTENTS

1. [Architecture Overview](#architecture-overview)
2. [Prerequisites](#prerequisites)
3. [Installation & Setup](#installation--setup)
4. [Configuration](#configuration)
5. [Deployment](#deployment)
6. [Testing & Verification](#testing--verification)
7. [Security Best Practices](#security-best-practices)
8. [Troubleshooting](#troubleshooting)

---

## 🏗️ ARCHITECTURE OVERVIEW

### System Components

```
┌─────────────────────────────────────────────────────────────────┐
│                         YOUR WEBSITE                            │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ index.html (Homepage) — ACCESSIBLE                       │  │
│  │ about.html, services.html — ACCESSIBLE                  │  │
│  │ /courses, /enrol, /payment — STRICTLY BLOCKED            │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ robots.txt (Layer 1: Crawler Control)                    │  │
│  │ User-agent: Google-Extended                              │  │
│  │ Allow: / (homepage only)                                 │  │
│  │ Disallow: /courses, /enrol, /payment                     │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│              gemini_homepage_indexer.py (Layer 2)               │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ 1. FETCH: Strict URL validation                          │  │
│  │    - Homepage URL ONLY (/ or /index.html)               │  │
│  │    - Block /courses, /enrol, /payment paths              │  │
│  │    - 500KB safety limit                                  │  │
│  ├──────────────────────────────────────────────────────────┤  │
│  │ 2. EXTRACT: Clean HTML → Text                            │  │
│  │    - Remove script/style tags                            │  │
│  │    - Strip navigation footers                            │  │
│  │    - Preserve semantic content                           │  │
│  ├──────────────────────────────────────────────────────────┤  │
│  │ 3. VALIDATE: Ensure no excluded content                  │  │
│  │    - Block "checkout", "payment", "course curriculum"    │  │
│  │    - Keyword-based safety checks                         │  │
│  ├──────────────────────────────────────────────────────────┤  │
│  │ 4. FEED TO GEMINI: System prompt with constraints        │  │
│  │    - Homepage text as sole context                       │  │
│  │    - Constraints: "ONLY homepage content"                │  │
│  │    - Redirect excluded topics                            │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│                    GOOGLE GEMINI API                            │
│  Constrained Model Instance                                    │
│  - Knowledge: Homepage content ONLY                            │
│  - Responses: Bounded to homepage scope                        │
│  - Excluded: Courses, payment, sensitive info                  │
└─────────────────────────────────────────────────────────────────┘
```

### Security Layers

| Layer | Mechanism | Purpose |
|-------|-----------|---------|
| **Layer 1** | robots.txt | Tell crawlers what to access |
| **Layer 2** | URL Validation | Block non-homepage requests at fetch time |
| **Layer 3** | Content Extraction | Remove HTML cruft, keep core text |
| **Layer 4** | Keyword Filtering | Detect & exclude sensitive content |
| **Layer 5** | System Prompt | Constrain Gemini's knowledge base |

---

## 📦 PREREQUISITES

### Required Software

- **Python 3.8+** — Language runtime
- **pip** — Python package manager
- **Git** — Version control (optional, for tracking changes)

### Required Accounts & API Keys

1. **Google Cloud Account**
   - Create at: https://cloud.google.com
   - Enable Gemini API in Google AI Studio

2. **Gemini API Key**
   - Get at: https://makersuite.google.com/app/apikey
   - Free tier available (up to 60 requests/minute)

### Python Dependencies

```bash
requests>=2.31.0        # HTTP client for fetching homepage
beautifulsoup4>=4.12.0  # HTML parsing & cleaning
google-generativeai>=0.3.0  # Official Gemini SDK
```

---

## 🚀 INSTALLATION & SETUP

### Step 1: Create Virtual Environment

```bash
# Navigate to your project directory
cd ~/Desktop/Nuance/nuancedco-deploy

# Create isolated Python environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate  # Windows
```

### Step 2: Install Dependencies

```bash
pip install --upgrade pip

pip install \
  requests>=2.31.0 \
  beautifulsoup4>=4.12.0 \
  google-generativeai>=0.3.0
```

### Step 3: Verify Installation

```bash
python3 -c "import requests, bs4, google.generativeai; print('✅ All dependencies installed')"
```

### Step 4: Get Your Gemini API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Click "Get API Key"
3. Create new API key (Google AI Studio)
4. Copy the key (looks like: `AIzaSyD...`)

### Step 5: Set Environment Variable

```bash
# Add to shell profile (macOS/Linux)
echo "export GEMINI_API_KEY='YOUR_API_KEY_HERE'" >> ~/.zshrc
source ~/.zshrc

# Verify
echo $GEMINI_API_KEY  # Should print your API key
```

**Windows (PowerShell):**
```powershell
[Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "YOUR_API_KEY_HERE", "User")
```

**Windows (Command Prompt):**
```cmd
setx GEMINI_API_KEY "YOUR_API_KEY_HERE"
```

---

## ⚙️ CONFIGURATION

### Update Homepage URL

Edit `gemini_homepage_indexer.py` and update this line:

```python
class Config:
    HOMEPAGE_URL = "https://nuancedco.com"  # ← Change to YOUR domain
```

Options:
- Production: `https://nuancedco.com`
- Staging: `https://staging.nuancedco.com`
- Local testing: `http://localhost:8000` (with local server running)

### Configure Excluded Content

```python
EXCLUDED_PATHS = [
    "/courses",
    "/course",
    "/enrol",
    "/portal",
    "/admin",
    "/api",
    "/cart",
    "/checkout",
    "/payment",
    "/user",
    "/dashboard",
]
```

Add/remove paths based on your site structure.

### Adjust Content Extraction

```python
REMOVE_TAGS = [
    "script", "style", "meta", "link", "noscript",
    "iframe", "nav", "footer"
]

REMOVE_IDS = [
    "cta", "resources", "testimonials"
]
```

Remove elements that aren't part of core homepage content.

### Gemini Model Selection

```python
GEMINI_MODEL = "gemini-2.5-flash"  # Fast, efficient
# Alternatives:
# "gemini-pro"  # More capable, slower
# "gemini-1.5-pro"  # Latest, experimental
```

---

## 🌐 DEPLOYMENT

### Local Testing (Development)

```bash
# Activate virtual environment
source venv/bin/activate

# Run the indexer
python3 gemini_homepage_indexer.py
```

**Expected Output:**
```
======================================================================
NUANCED CO. — GEMINI HOMEPAGE INDEXER
======================================================================

🔍 Fetching homepage: https://nuancedco.com
✅ Homepage fetched successfully (45821 bytes)

🧹 Extracting text content...
✅ Text extracted (18234 characters)

✅ Gemini initialized (gemini-2.5-flash)

📤 Sending to Gemini (18234 characters)...

📊 Gemini Response:
   Input tokens: 3421
   Output tokens: 287
   Total tokens: 3708

💬 Test Response:
Nuanced Co. is a neurodivergent consultancy...

======================================================================
✅ Indexing complete!
======================================================================
```

### Production Deployment (Server)

#### Option A: Scheduled Cron Job (Reindex Daily)

```bash
# Edit crontab
crontab -e

# Add this line (runs at 2 AM daily)
0 2 * * * cd /path/to/nuancedco-deploy && /path/to/venv/bin/python3 gemini_homepage_indexer.py >> /var/log/gemini_indexer.log 2>&1
```

#### Option B: AWS Lambda (Serverless)

```bash
# Package with dependencies
pip install -r requirements.txt -t lambda_package/
cp gemini_homepage_indexer.py lambda_package/

# Zip and upload to Lambda
cd lambda_package && zip -r ../lambda_function.zip . && cd ..

# Set environment variable in Lambda console
GEMINI_API_KEY = your_api_key_here
```

#### Option C: Docker Container

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY gemini_homepage_indexer.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENV GEMINI_API_KEY=${GEMINI_API_KEY}

CMD ["python3", "gemini_homepage_indexer.py"]
```

```bash
# Build
docker build -t nuanced-gemini-indexer .

# Run
docker run -e GEMINI_API_KEY="your_key" nuanced-gemini-indexer
```

### Deploy robots.txt

1. Place `robots.txt` in your web root:
   ```
   /var/www/html/robots.txt
   # OR
   ~/Desktop/Nuance/nuancedco-deploy/robots.txt
   ```

2. Verify accessibility:
   ```bash
   curl https://nuancedco.com/robots.txt
   ```

3. Wait 24-48 hours for crawler propagation

---

## ✅ TESTING & VERIFICATION

### Test 1: Verify Script Runs

```bash
python3 gemini_homepage_indexer.py
# Should complete without errors
```

### Test 2: Verify Gemini Response

Look for this in output:
```
💬 Test Response:
Nuanced Co. is an adult neurodivergent consultancy...
```

### Test 3: Verify URL Validation (Should Fail)

Temporarily edit the script and test:
```python
# This should fail validation:
fetcher = HomepageFetcher("https://nuancedco.com/courses")
# Output: ❌ Non-homepage path detected: /courses
```

### Test 4: Verify robots.txt

```bash
# Check robots.txt syntax
curl https://nuancedco.com/robots.txt | head -20

# Expected output shows Google-Extended rules
```

### Test 5: Google Search Console

1. Go to: https://search.google.com/search-console
2. Select your property
3. Tools → robots.txt Tester
4. Test URL: `GET /`
   - Should show: ✅ Allowed
5. Test URL: `GET /courses`
   - Should show: ❌ Blocked

### Test 6: Interactive Chat Mode

After script starts, try these prompts:

```
🤖 Ask Gemini about the homepage: What services does Nuanced Co. offer?
✨ [Should answer based on homepage content]

🤖 Ask Gemini about the homepage: How do I enroll in the course?
✨ [Should redirect: "I only have access to our homepage information..."]
```

---

## 🔒 SECURITY BEST PRACTICES

### 1. API Key Management

❌ **DON'T:**
```python
API_KEY = "AIzaSyD..."  # Hard-coded in script
```

✅ **DO:**
```bash
export GEMINI_API_KEY="AIzaSyD..."
# Script reads from environment: os.getenv("GEMINI_API_KEY")
```

### 2. Rotate API Keys Regularly

```bash
# Every 90 days, create a new key at makersuite.google.com
# Update environment variable
# Delete old key from Google Cloud Console
```

### 3. Monitor API Usage

Google AI Studio Dashboard:
- Track requests/minute
- Set up billing alerts
- Monitor quota usage

### 4. Rate Limiting

The script includes built-in limits:
```python
REQUEST_TIMEOUT = 10  # 10-second timeout
MAX_CONTENT_LENGTH = 500000  # 500KB limit
```

### 5. Input Validation

Never trust URL parameters:
```python
# Always validate before fetching
if not URLValidator.is_homepage_only(url, homepage_base):
    return None  # Abort
```

### 6. Content Filtering

Keyword-based safety checks:
```python
excluded_keywords = [
    "checkout", "payment method", "enrol now",
    "course curriculum", "lesson", "module"
]
```

### 7. Logging

For production, log all requests:
```python
import logging
logging.info(f"Indexed homepage at {datetime.now()}")
logging.warning(f"Blocked access to: {attempted_url}")
```

---

## 🛠️ TROUBLESHOOTING

### Issue: "GEMINI_API_KEY not found"

**Solution:**
```bash
# Verify key is set
echo $GEMINI_API_KEY

# If empty, set it again
export GEMINI_API_KEY="your_key"

# Add to ~/.zshrc or ~/.bash_profile for persistence
```

### Issue: "HTTP 403: Access Denied"

**Cause:** robots.txt is blocking the fetch
**Solution:**
```bash
# Verify robots.txt allows your User-Agent
curl -A "Mozilla/5.0" https://nuancedco.com/robots.txt

# Test your domain loads in browser
# Check server error logs: /var/log/apache2/error.log
```

### Issue: "Content exceeds safety limit"

**Cause:** Homepage is > 500KB
**Solution:**
```python
# Increase limit (if necessary)
MAX_CONTENT_LENGTH = 1000000  # 1MB

# OR minimize page size
# - Remove unused CSS/JS
# - Compress images
# - Minify code
```

### Issue: "Gemini returns course content"

**Cause:** System prompt wasn't applied correctly
**Solution:**
```python
# Verify system prompt in index_homepage():
print(system_prompt[:500])  # Debug first 500 chars

# Ensure homepage text doesn't contain excluded keywords
if not validator.check_excluded_content(clean_text):
    print("Warning: Excluded content detected")
```

### Issue: "Timeout after 10 seconds"

**Cause:** Homepage is slow to load
**Solution:**
```python
# Increase timeout
REQUEST_TIMEOUT = 20  # 20 seconds

# OR check server performance
# - Check database queries
# - Enable caching headers
# - Use CDN for static assets
```

---

## 📊 MONITORING & MAINTENANCE

### Weekly Checks

- [ ] Verify script runs without errors
- [ ] Check Gemini API usage dashboard
- [ ] Monitor server logs for blocked requests
- [ ] Test interactive chat mode

### Monthly Tasks

- [ ] Review and update excluded content keywords
- [ ] Check Google Search Console for crawl errors
- [ ] Verify robots.txt is still accessible
- [ ] Update documentation with any changes

### Quarterly Tasks

- [ ] Rotate API keys
- [ ] Review and update system prompt constraints
- [ ] Test with new Gemini model versions
- [ ] Audit homepage for accidental course content

---

## 📚 ADDITIONAL RESOURCES

- **Google Gemini Documentation:** https://ai.google.dev/
- **robots.txt Validator:** https://www.robotstxt.org/
- **BeautifulSoup Documentation:** https://www.crummy.com/software/BeautifulSoup/
- **Google Search Console:** https://search.google.com/search-console

---

## ✨ SUMMARY

You now have a production-ready system for:

1. ✅ **Secure Homepage Access** — Multiple validation layers
2. ✅ **Gemini Integration** — Official google-genai SDK
3. ✅ **Content Protection** — Course content completely excluded
4. ✅ **Easy Deployment** — Local, cloud, or serverless options
5. ✅ **Monitoring** — Built-in logging and validation

**Next Steps:**
1. Update `HOMEPAGE_URL` in the script
2. Set `GEMINI_API_KEY` environment variable
3. Place `robots.txt` in web root
4. Run: `python3 gemini_homepage_indexer.py`
5. Test interactive chat mode

**Questions?** Review the troubleshooting section or check Google's official documentation.

---

**Last Updated:** June 6, 2026  
**Version:** 1.0 (Production Ready)  
**Maintainer:** Senior Software Engineer
