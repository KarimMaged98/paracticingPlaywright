import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(playwright: Playwright):
    # Browser configurations #
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width": 1728, "height": 1117})

    yield page
    page.close()
