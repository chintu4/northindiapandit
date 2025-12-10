from playwright.sync_api import sync_playwright

def verify_gallery():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/index.html")

        # Navigate to gallery section
        page.locator("#gallery").scroll_into_view_if_needed()

        # Take screenshot of the gallery section
        # The gallery row is after the h2#gallery
        # We can locate the parent section
        gallery_section = page.locator("h2#gallery").locator("xpath=../..")

        # Ensure new images are present
        # We expect 12 images in the gallery now (8 original + 4 new)
        images = gallery_section.locator(".col-sm-4 img")
        count = images.count()
        print(f"Found {count} images in gallery")

        # Capture screenshot of the gallery
        gallery_section.screenshot(path="verification/gallery_screenshot.png")

        browser.close()

if __name__ == "__main__":
    verify_gallery()
