from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # Mobile viewport similar to iPhone SE or generic mobile
        context = browser.new_context(viewport={'width': 375, 'height': 667})
        page = context.new_page()

        # Load the local HTML file
        # We need absolute path
        cwd = os.getcwd()
        url = f"file://{cwd}/index.html"
        print(f"Loading {url}")

        page.goto(url)

        # Wait for fonts and content
        page.wait_for_timeout(1000)

        # Take a screenshot of the header
        print("Taking header screenshot...")
        page.screenshot(path="verification/header_mobile.png", clip={'x': 0, 'y': 0, 'width': 375, 'height': 800})

        # Scroll to portfolio to see Hindi text there
        # Locate the portfolio section
        portfolio = page.locator("#portfolio")
        if portfolio.is_visible():
            portfolio.scroll_into_view_if_needed()
            page.wait_for_timeout(500)
            print("Taking portfolio screenshot...")
            page.screenshot(path="verification/portfolio_mobile.png", clip={'x': 0, 'y': 0, 'width': 375, 'height': 1500})

        browser.close()

if __name__ == "__main__":
    run()
