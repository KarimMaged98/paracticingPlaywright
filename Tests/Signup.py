from playwright.sync_api import Playwright, sync_playwright, expect
from Helper import EnumType
from Helper.EnumType import TheEnum
from POM.HomePageObjectModel import HomePage
from jproperties import Properties
import time


def run(playwright: Playwright) -> None:
    # ====Configurations==== #

    # Reading data from config file
    configs = Properties()
    with open('/Users/karimmaged/PycharmProjects/paracticingPlaywright/Config/userData.properties',
              'rb') as config_file:
        configs.load(config_file)

    # Getting current timestamp
    currentTimeStamp = str(time.time())

    # ====User Journey==== #

    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Opening the browser
    context = browser.new_context()
    page = context.new_page()
    # Navigating to the staging portal using enum flag
    page.goto(EnumType.navigation(TheEnum.siteStage))
    # Taking instance of the homepage
    homepage = HomePage(page)

    # Choosing Kuwait operation
    homepage.OPS.click()

    # Open Login page
    homepage.LoginBtn.click()
    expect(homepage.LoginLabel).to_be_visible()

    # Open Sign up page
    homepage.RegisterBtn.click()
    expect(homepage.RegisterLabel).to_be_visible()

    # Fill the form
    homepage.EmailField.click()
    homepage.EmailField.fill(configs.get("email").data + currentTimeStamp[6:10] + configs.get("domain").data)
    homepage.FirstNameField.click()
    homepage.FirstNameField.fill(configs.get("firstName").data)
    homepage.SecondNameField.click()
    homepage.SecondNameField.fill(configs.get("lastName").data)
    homepage.GenderMaleRadioButton.check()
    homepage.PhoneNumberField.click()
    homepage.PhoneNumberField.fill(configs.get("phoneNumber").data + currentTimeStamp[5:10])
    homepage.DatePicker.click()
    homepage.TodayDate.click()
    homepage.PasswordField.click()
    homepage.PasswordField.fill(configs.get("password").data)
    homepage.SubmitBtn.click()

    expect(homepage.SignUpSuccessLabel).to_be_visible()
    print("==== TEST PASSED =====")

    # Closing the browser
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
