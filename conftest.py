import pytest
import os

from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    # Headless si se pasa --headless o no hay display disponible
    headless = os.getenv("HEADLESS", "false").lower() == "true" \
        or os.environ.get("DISPLAY") is None
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        page.goto("https://www.saucedemo.com/")
        yield page
        context.close()
        browser.close()