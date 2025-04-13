
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import re

BASE_URL = "https://lifesynergyretreat.com"
OUTPUT_DIR = "docs"
visited = set()
MAX_DEPTH = 2

os.makedirs(OUTPUT_DIR, exist_ok=True)

def is_internal_link(link):
    return link.startswith("/") or BASE_URL in link

def sanitize_url(url):
    parsed = urlparse(url)
    return parsed.scheme + "://" + parsed.netloc + parsed.path

def slugify(url):
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return "homepage"
    return re.sub(r"[^a-zA-Z0-9_-]", "_", path)

async def scrape_page(playwright, url, depth):
    if depth > MAX_DEPTH or url in visited:
        return

    visited.add(url)
    browser = await playwright.chromium.launch(headless=True)
    page = await browser.new_page()
    try:
        await page.goto(url, timeout=15000)
        content = await page.content()
    except Exception as e:
        print(f"Failed to load {url}: {e}")
        await browser.close()
        return

    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text(separator="\n", strip=True)

    # Save page content
    filename = slugify(url) + ".txt"
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"===== {url} =====\n\n{text}")
    print(f"✅ Saved: {filepath}")

    # Get internal links
    links = set()
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if is_internal_link(href):
            full_url = urljoin(BASE_URL, href)
            links.add(sanitize_url(full_url))

    await browser.close()

    # Recursively scrape linked pages
    for link in links:
        await scrape_page(playwright, link, depth + 1)

async def main():
    async with async_playwright() as playwright:
        await scrape_page(playwright, BASE_URL, depth=0)

    print(f"✅ Full site scrape complete. Files saved to ./{OUTPUT_DIR}/")

if __name__ == "__main__":
    asyncio.run(main())
