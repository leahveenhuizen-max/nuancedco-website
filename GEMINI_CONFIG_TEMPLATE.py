#!/usr/bin/env python3
"""
GEMINI API CONFIGURATION TEMPLATE
Copy this file and customize for your organization

USAGE:
1. Copy this template: cp GEMINI_CONFIG_TEMPLATE.py config_custom.py
2. Edit config_custom.py with your values
3. Import in your script: from config_custom import Config
"""

# ─────────────────────────────────────────────────────────────────────────
# WEBSITE CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────

WEBSITE_DOMAIN = "https://nuancedco.com"  # ← UPDATE: Your website domain
HOMEPAGE_URL = f"{WEBSITE_DOMAIN}"  # Homepage only
ALLOWED_PATHS = ["/", "/index.html", "/index", ""]  # Strict scope


# ─────────────────────────────────────────────────────────────────────────
# EXCLUDED CONTENT (Course, Payment, Admin)
# ─────────────────────────────────────────────────────────────────────────

EXCLUDED_PATHS = [
    # Course/Learning
    "/courses",
    "/course",
    "/course.html",
    "/lessons",
    "/modules",
    "/class",
    "/training",
    "/workshop",

    # Enrollment/Payment
    "/enrol",
    "/enroll",
    "/enrollment",
    "/signup",
    "/register",
    "/checkout",
    "/cart",
    "/payment",
    "/billing",
    "/invoice",
    "/receipt",

    # User Accounts
    "/user",
    "/account",
    "/profile",
    "/dashboard",
    "/login",
    "/logout",
    "/password",

    # Admin/System
    "/admin",
    "/api",
    "/api-docs",
    "/backend",
    "/settings",
    "/config",
    "/database",
    "/logs",

    # Security
    "/.env",
    "/.git",
    "/.htaccess",
    "/wp-admin",
    "/wp-login.php",
    "/xmlrpc.php",
]

EXCLUDED_KEYWORDS = [
    # Payment/Financial
    "checkout", "payment method", "credit card", "billing",
    "invoice", "receipt", "transaction", "purchase",

    # Enrollment/Course
    "enrol now", "sign up", "course curriculum",
    "lesson", "module", "chapter", "assignment",
    "quiz", "exam", "grade", "certificate",

    # User Data
    "username", "password", "email address",
    "phone number", "address", "billing info",
]


# ─────────────────────────────────────────────────────────────────────────
# GEMINI CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────

# Model Selection
GEMINI_MODEL = "gemini-2.5-flash"  # Fast and efficient
# Alternatives:
#   "gemini-pro"       # More capable, slower
#   "gemini-1.5-pro"   # Latest experimental model

# API Key (from environment variable)
GEMINI_API_KEY_ENV = "GEMINI_API_KEY"

# Gemini System Prompt (constraints for model)
GEMINI_SYSTEM_PROMPT = """You are an AI assistant for {company_name}.

IMPORTANT CONSTRAINTS:
- You ONLY have access to the main homepage content provided below
- You MUST NOT reference, discuss, or provide information about:
  * Course curriculum, modules, lessons, or assignments
  * Enrollment, signup, checkout, or payment information
  * User accounts, dashboards, or personal data
  * Any content or functionality outside the homepage

- If asked about excluded topics, respond professionally:
  "I only have access to our homepage information. For details about [topic],
   please visit our website directly or contact us."

- Keep responses concise (2-3 sentences) and friendly
- Use the person's name if provided
- Maintain brand voice and tone

HOMEPAGE CONTENT (Your only knowledge source):
---
{homepage_content}
---

Answer based ONLY on the content above."""


# ─────────────────────────────────────────────────────────────────────────
# HTTP REQUEST CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

REQUEST_TIMEOUT = 10  # seconds
MAX_CONTENT_LENGTH = 500000  # bytes (500KB)

# Retry configuration
MAX_RETRIES = 3
RETRY_DELAY = 2  # seconds between retries


# ─────────────────────────────────────────────────────────────────────────
# HTML PARSING CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────

# Tags to remove during extraction
REMOVE_TAGS = [
    "script",      # JavaScript
    "style",       # CSS
    "meta",        # Metadata
    "link",        # Resource links
    "noscript",    # NoScript fallback
    "iframe",      # Embedded frames
    "nav",         # Navigation (usually secondary)
    "footer",      # Footer (usually secondary)
    "header",      # Header (optional)
    "aside",       # Sidebars (optional)
]

# Element IDs to remove
REMOVE_IDS = [
    "nav",
    "footer",
    "cta",
    "resources",
    "testimonials",
    "related",
    "sidebar",
]

# Element classes to remove
REMOVE_CLASSES = [
    "cookie-banner",
    "modal",
    "popup",
    "advertisement",
    "sidebar",
]

# Content extraction settings
PRESERVE_SEMANTIC_TAGS = True  # Keep <strong>, <em>, etc.
COLLAPSE_WHITESPACE = True     # Convert multiple spaces to single space


# ─────────────────────────────────────────────────────────────────────────
# LOGGING CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────

LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = None  # Set to path for file logging, None for stdout only
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Enable detailed request logging
DEBUG_HTTP_REQUESTS = False  # Set to True to log raw HTTP requests
DEBUG_GEMINI_PROMPTS = False  # Set to True to log full prompts sent to Gemini


# ─────────────────────────────────────────────────────────────────────────
# DEPLOYMENT CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────

# Environment (development, staging, production)
ENVIRONMENT = "development"

# Cache settings
USE_CACHE = False  # Cache homepage content?
CACHE_TTL = 3600  # Cache for 1 hour (seconds)
CACHE_DIR = "./cache"

# Rate limiting
ENABLE_RATE_LIMIT = True
REQUESTS_PER_MINUTE = 60


# ─────────────────────────────────────────────────────────────────────────
# MONITORING & ALERTS
# ─────────────────────────────────────────────────────────────────────────

# Enable error notifications
ENABLE_ERROR_ALERTS = False
ERROR_EMAIL = "admin@nuancedco.com"

# Track API usage
TRACK_API_USAGE = True
USAGE_LOG_FILE = "./logs/gemini_usage.log"

# Alert thresholds
ALERT_ON_FAILED_REQUESTS = True
ALERT_ON_EXCLUDED_CONTENT_FOUND = True
ALERT_ON_HIGH_LATENCY = True
LATENCY_THRESHOLD_MS = 5000  # 5 seconds


# ─────────────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────

def get_system_prompt(company_name="Your Company", homepage_content=""):
    """Generate formatted system prompt with company name and content."""
    return GEMINI_SYSTEM_PROMPT.format(
        company_name=company_name,
        homepage_content=homepage_content
    )

def get_config_summary():
    """Print human-readable config summary."""
    return f"""
    ╔════════════════════════════════════════════════════════════════╗
    ║          GEMINI CONFIGURATION SUMMARY                         ║
    ╠════════════════════════════════════════════════════════════════╣
    ║ Domain:              {WEBSITE_DOMAIN}
    ║ Homepage URL:        {HOMEPAGE_URL}
    ║ Gemini Model:        {GEMINI_MODEL}
    ║ Environment:         {ENVIRONMENT}
    ║ Max Content Length:  {MAX_CONTENT_LENGTH} bytes
    ║ Request Timeout:     {REQUEST_TIMEOUT}s
    ║ Excluded Paths:      {len(EXCLUDED_PATHS)} paths
    ║ Excluded Keywords:   {len(EXCLUDED_KEYWORDS)} keywords
    ╚════════════════════════════════════════════════════════════════╝
    """


# ─────────────────────────────────────────────────────────────────────────
# EXAMPLE USAGE IN MAIN SCRIPT
# ─────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Print configuration
    print(get_config_summary())

    # Validate configuration
    print("\n✅ Configuration loaded successfully!")
    print(f"   Model: {GEMINI_MODEL}")
    print(f"   Domain: {WEBSITE_DOMAIN}")
    print(f"   Excluded paths: {len(EXCLUDED_PATHS)}")
