from playwright.sync_api import sync_playwright
import time

def verify_text_transition():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000")

        # Initial state
        page.wait_for_selector("#call-btn-text")
        print("Initial text:", page.locator("#call-btn-text").text_content())
        page.screenshot(path="verification/step1_initial.png")

        # Wait for transition start (approx 3 seconds)
        # We want to capture the fade-out state (opacity should be 0)
        # The transition duration is 0.5s.
        # The JS waits 3000ms, then adds .text-hidden.
        # We can poll the class or opacity.

        print("Waiting for transition class...")
        try:
            # Wait for the .text-hidden class to appear
            page.wait_for_selector(".text-hidden", timeout=5000)
            print("Transition started (class added)")
            # Take screenshot during fade out
            page.screenshot(path="verification/step2_fading_out.png")

            # Verify opacity is 0 (or close to it if capturing mid-transition)
            # Actually, wait_for_selector waits until it is attached.
            # CSS transition takes 0.5s.
            time.sleep(0.2) # mid-transition or fully hidden
            page.screenshot(path="verification/step3_hidden.png")

        except Exception as e:
            print("Error waiting for transition:", e)

        # Wait for text update and fade in
        # The JS removes .text-hidden after 500ms
        try:
            page.wait_for_selector("#call-btn-text:not(.text-hidden)", timeout=2000)
            print("Transition finished (class removed)")
            time.sleep(0.6) # Wait for fade in transition to complete
            print("New text:", page.locator("#call-btn-text").text_content())
            page.screenshot(path="verification/step4_final.png")
        except Exception as e:
            print("Error waiting for fade in:", e)

        browser.close()

if __name__ == "__main__":
    verify_text_transition()
