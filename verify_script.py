from playwright.sync_api import sync_playwright
import os
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Load local file
        page.goto("file://" + os.path.abspath("index.html"))

        # Wait for content to load
        page.wait_for_selector("footer")

        # Verify Address
        address_element = page.locator(".contact-infos .item").filter(has_text="Location")
        address_text = address_element.inner_text()
        print(f"Found address text: {address_text}")

        if "Kondapur, Hyderabad" in address_text:
            print("Address verification PASSED")
        else:
            print("Address verification FAILED")

        # Screenshot Contact
        page.locator("#contact").screenshot(path="contact_verification.png")

        # Screenshot Gallery
        page.locator("#gallery").scroll_into_view_if_needed()
        # Take screenshot of the gallery grid row
        page.locator(".row").nth(2).screenshot(path="gallery_verification.png")

        browser.close()

if __name__ == "__main__":
    run()
