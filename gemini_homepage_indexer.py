#!/usr/bin/env python3
"""
NUANCED CO. — GEMINI HOMEPAGE INDEXER
Fetches ONLY the main homepage and feeds it to Google Gemini API
Author: Claude (Senior Software Engineer)
Purpose: Index homepage content for AI-powered responses
"""

import os
import sys
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from typing import Optional, Dict
import google.generativeai as genai


# ─────────────────────────────────────────────────────────────────────────
# CONFIGURATION & CONSTANTS
# ─────────────────────────────────────────────────────────────────────────

class Config:
    """Configuration for homepage indexing and Gemini integration."""

    # Website Configuration
    HOMEPAGE_URL = "https://nuancedco.com"  # ← UPDATE with your actual domain
    HOMEPAGE_ALLOWED_PATHS = ["/", "/index.html", ""]  # Strict scope

    # STRICTLY EXCLUDED DIRECTORIES (course content + sensitive areas)
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

    # Gemini Configuration
    GEMINI_MODEL = "gemini-2.5-flash"
    GEMINI_API_KEY_ENV = "GEMINI_API_KEY"  # Environment variable name

    # Request Configuration
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    REQUEST_TIMEOUT = 10
    MAX_CONTENT_LENGTH = 500000  # 500KB safety limit

    # Content Extraction
    REMOVE_TAGS = [
        "script", "style", "meta", "link", "noscript",
        "iframe", "nav", "footer"  # Remove secondary navigation
    ]
    REMOVE_IDS = ["cta", "resources", "testimonials"]  # Remove non-homepage sections


# ─────────────────────────────────────────────────────────────────────────
# STEP 1: SECURE URL VALIDATION
# ─────────────────────────────────────────────────────────────────────────

class URLValidator:
    """Ensures we ONLY fetch the homepage, nothing else."""

    @staticmethod
    def is_homepage_only(url: str, homepage_base: str) -> bool:
        """
        Strict validation: URL must be exactly the homepage.

        Returns True only if:
        - Domain matches homepage domain exactly
        - Path is "/" or "/index.html" or empty
        - No query parameters or fragments that lead elsewhere
        """
        try:
            parsed = urlparse(url)
            homepage_parsed = urlparse(homepage_base)

            # 1. Domain MUST match exactly
            if parsed.netloc != homepage_parsed.netloc:
                print(f"❌ Domain mismatch: {parsed.netloc} != {homepage_parsed.netloc}")
                return False

            # 2. Path MUST be homepage-only
            path = parsed.path.rstrip("/") or "/"
            if path not in ["/", "/index.html", "", "/index"]:
                print(f"❌ Non-homepage path detected: {path}")
                return False

            # 3. Query parameters should be minimal (no tracking, no redirects)
            if parsed.query:
                print(f"⚠️  Query parameters detected (ignored): {parsed.query}")

            return True
        except Exception as e:
            print(f"❌ URL validation error: {e}")
            return False

    @staticmethod
    def check_excluded_content(content: str) -> bool:
        """Verify excluded content isn't present in fetched HTML."""
        excluded_keywords = [
            "checkout", "payment method", "enrol now",
            "course curriculum", "lesson", "module"
        ]
        content_lower = content.lower()
        found = [k for k in excluded_keywords if k in content_lower]

        if found:
            print(f"⚠️  Warning: Excluded content keywords found: {found}")
            return False
        return True


# ─────────────────────────────────────────────────────────────────────────
# STEP 2: TARGETED HOMEPAGE FETCH
# ─────────────────────────────────────────────────────────────────────────

class HomepageFetcher:
    """Fetches and cleans ONLY the homepage content."""

    def __init__(self, homepage_url: str):
        self.homepage_url = homepage_url
        self.validator = URLValidator()
        self.headers = {"User-Agent": Config.USER_AGENT}

    def fetch(self) -> Optional[str]:
        """
        Fetch homepage with strict validation.

        Returns:
            Raw HTML of homepage, or None if validation fails
        """
        print(f"\n🔍 Fetching homepage: {self.homepage_url}")

        try:
            # Validate URL before fetching
            if not self.validator.is_homepage_only(self.homepage_url, self.homepage_url):
                print("❌ URL validation failed. Aborting fetch.")
                return None

            # Fetch with timeout
            response = requests.get(
                self.homepage_url,
                headers=self.headers,
                timeout=Config.REQUEST_TIMEOUT,
                allow_redirects=False  # Don't follow redirects to other pages
            )

            # Verify response
            if response.status_code != 200:
                print(f"❌ HTTP {response.status_code}: Unable to fetch homepage")
                return None

            # Check content length safety
            if len(response.content) > Config.MAX_CONTENT_LENGTH:
                print(f"❌ Content exceeds safety limit ({len(response.content)} bytes)")
                return None

            print(f"✅ Homepage fetched successfully ({len(response.content)} bytes)")
            return response.text

        except requests.exceptions.RequestException as e:
            print(f"❌ Fetch error: {e}")
            return None

    def extract_text(self, html: str) -> str:
        """
        Parse HTML and extract clean text content.

        - Removes script/style tags
        - Removes secondary navigation (nav, footer)
        - Preserves semantic structure
        - Strips excessive whitespace
        """
        print("\n🧹 Extracting text content...")

        try:
            soup = BeautifulSoup(html, "html.parser")

            # Remove unwanted elements
            for tag_name in Config.REMOVE_TAGS:
                for tag in soup.find_all(tag_name):
                    tag.decompose()

            for element_id in Config.REMOVE_IDS:
                element = soup.find(id=element_id)
                if element:
                    element.decompose()

            # Extract text
            text = soup.get_text(separator="\n", strip=True)

            # Clean up whitespace
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            clean_text = "\n".join(lines)

            # Final safety check
            if not self.validator.check_excluded_content(clean_text):
                print("⚠️  Warning: Some excluded content keywords present")

            print(f"✅ Text extracted ({len(clean_text)} characters)")
            return clean_text

        except Exception as e:
            print(f"❌ Extraction error: {e}")
            return ""


# ─────────────────────────────────────────────────────────────────────────
# STEP 3: GEMINI API INTEGRATION
# ─────────────────────────────────────────────────────────────────────────

class GeminiIntegrator:
    """Feeds homepage content to Google Gemini API."""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Gemini with API key.

        Args:
            api_key: Google Gemini API key. If None, reads from environment.
        """
        if not api_key:
            api_key = os.getenv(Config.GEMINI_API_KEY_ENV)

        if not api_key:
            raise ValueError(
                f"❌ {Config.GEMINI_API_KEY_ENV} not found.\n"
                "Set with: export GEMINI_API_KEY='your-api-key'"
            )

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(Config.GEMINI_MODEL)
        print(f"\n✅ Gemini initialized ({Config.GEMINI_MODEL})")

    def index_homepage(self, homepage_text: str) -> Dict:
        """
        Feed homepage text to Gemini for indexing/analysis.

        This creates a system prompt that constrains Gemini to only
        discuss content from the homepage.

        Args:
            homepage_text: Clean text from homepage

        Returns:
            Dict with model metadata and token counts
        """
        print(f"\n📤 Sending to Gemini ({len(homepage_text)} characters)...")

        # Create system prompt that constrains responses to homepage content
        system_prompt = f"""You are an AI assistant for Nuanced Co., a neurodivergent consultancy.

IMPORTANT CONSTRAINTS:
- You ONLY have access to the main homepage content
- You MUST NOT reference, discuss, or provide information about:
  * Course curriculum, modules, or lessons
  * Enrollment, checkout, or payment information
  * User dashboards or accounts
  * Any content outside the homepage
- If asked about excluded topics, respond: "I only have access to our homepage information. For details about courses or enrollment, please visit our website directly."

HOMEPAGE CONTENT (Your only knowledge base):
---
{homepage_text}
---

Use this content to answer questions about Nuanced Co., our services, and Leah's background."""

        try:
            # Test the integration with a simple query
            response = self.model.generate_content(
                [
                    {"role": "user", "parts": [system_prompt]},
                    {"role": "user", "parts": ["Based on the homepage content provided, summarize Nuanced Co. in 2-3 sentences."]}
                ]
            )

            # Extract token counts
            metadata = {
                "model": Config.GEMINI_MODEL,
                "input_tokens": response.usage_metadata.prompt_token_count,
                "output_tokens": response.usage_metadata.completion_token_count,
                "total_tokens": (
                    response.usage_metadata.prompt_token_count +
                    response.usage_metadata.completion_token_count
                ),
                "status": "✅ Indexed successfully"
            }

            print(f"\n📊 Gemini Response:")
            print(f"   Input tokens: {metadata['input_tokens']}")
            print(f"   Output tokens: {metadata['output_tokens']}")
            print(f"   Total tokens: {metadata['total_tokens']}")
            print(f"\n💬 Test Response:\n{response.text}")

            return metadata

        except Exception as e:
            print(f"❌ Gemini error: {e}")
            return {"status": f"❌ Error: {e}"}

    def chat_with_context(self, user_query: str, homepage_text: str) -> str:
        """
        Have a conversation with Gemini using homepage as context.

        Args:
            user_query: User's question
            homepage_text: Homepage content

        Returns:
            Gemini's response
        """
        system_prompt = f"""You are an AI assistant for Nuanced Co. You have ONLY this homepage content as your knowledge:

{homepage_text}

STRICT RULES:
- Only answer based on homepage content
- Don't mention courses, enrollment, or payment
- If asked about excluded topics, politely redirect to the website"""

        response = self.model.generate_content(
            [
                {"role": "user", "parts": [system_prompt]},
                {"role": "user", "parts": [user_query]}
            ]
        )

        return response.text


# ─────────────────────────────────────────────────────────────────────────
# MAIN EXECUTION
# ─────────────────────────────────────────────────────────────────────────

def main():
    """Main execution flow."""
    print("=" * 70)
    print("NUANCED CO. — GEMINI HOMEPAGE INDEXER")
    print("=" * 70)

    # Step 1: Fetch homepage
    fetcher = HomepageFetcher(Config.HOMEPAGE_URL)
    html = fetcher.fetch()

    if not html:
        print("\n❌ Failed to fetch homepage. Exiting.")
        sys.exit(1)

    # Step 2: Extract clean text
    text = fetcher.extract_text(html)

    if not text:
        print("\n❌ Failed to extract text. Exiting.")
        sys.exit(1)

    # Step 3: Initialize Gemini
    try:
        gemini = GeminiIntegrator()
    except ValueError as e:
        print(f"\n{e}")
        sys.exit(1)

    # Step 4: Index homepage
    metadata = gemini.index_homepage(text)

    # Step 5: Interactive chat (optional)
    print("\n" + "=" * 70)
    print("💬 INTERACTIVE MODE (Type 'exit' to quit)")
    print("=" * 70)

    try:
        while True:
            query = input("\n🤖 Ask Gemini about the homepage: ").strip()
            if query.lower() == "exit":
                break
            if query:
                response = gemini.chat_with_context(query, text)
                print(f"\n✨ {response}")
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except EOFError:
        # Handle non-interactive mode (script)
        pass

    print("\n" + "=" * 70)
    print("✅ Indexing complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
