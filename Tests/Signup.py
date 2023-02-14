from playwright.sync_api import Playwright, sync_playwright, expect
from Helper import EnumType
from Helper.EnumType import TheEnum
from POM.HomePageObjectModel import HomePage


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto(EnumType.navigation(TheEnum.siteStage))
    homepage = HomePage(page)
    homepage.OPS.click()
    homepage.LoginBtn.click()
    homepage.RegisterBtn.click()
    homepage.EmailField.click()
    homepage.EmailField.fill("test2@test.test")
    homepage.FirstNameField.click()
    homepage.FirstNameField.fill("test")
    homepage.SecondNameField.click()
    homepage.SecondNameField.fill("test")
    homepage.GenderMaleRadioButton.check()
    homepage.PhoneNumberField.click()
    homepage.PhoneNumberField.fill("909090909")
    homepage.DatePicker.click()
    homepage.TodayDate.click()
    homepage.PasswordField.click()
    homepage.PasswordField.fill("testtest")
    homepage.SubmitBtn.click()
    expect(homepage.MyAccountLabel).to_be_visible()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
