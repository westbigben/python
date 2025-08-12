"""Playwright example — attempt to launch a browser and print page title (falls back gracefully)."""
import sys
from pathlib import Path

def main():
    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print('Playwright not installed or browsers not available. Skipping Playwright demo. Error:', e)
        return

    print('Playwright demo — launching headless browser...')
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('https://example.com', timeout=10000)
        print('Page title:', page.title())
        browser.close()

if __name__ == '__main__':
    main()
