from playwright.sync_api import Playwright, sync_playwright, expect
from Helper import EnumType
from Helper.EnumType import TheEnum


# This test for navigating between different portals using the enum
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto(EnumType.navigation(TheEnum.siteStage))
    expect(page.locator("#IconLogoXEnAr_svg__Layer_1")).to_be_visible()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
