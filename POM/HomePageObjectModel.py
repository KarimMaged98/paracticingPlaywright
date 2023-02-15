from datetime import date


class HomePage:

    def __init__(self, page):
        self.OPS = page.get_by_role("link", name="Kuwait Kuwait")
        self.LoginBtn = page.get_by_test_id("TestId__HeaderLoginLink")
        self.LoginLabel = page.get_by_role("heading", name="Login")
        self.RegisterBtn = page.get_by_role("link", name="Create Account")
        self.RegisterLabel = page.get_by_role("heading", name="Create Account")
        self.EmailField = page.get_by_label("Email*")
        self.FirstNameField = page.get_by_label("First Name*")
        self.SecondNameField = page.get_by_label("Last Name*")
        self.GenderMaleRadioButton = page.get_by_label("Male", exact=True)
        self.GenderFemaleRadioButton = page.get_by_label("Female", exact=True)
        self.PhoneNumberField = page.get_by_test_id("TestId__PhoneNumber").get_by_test_id("TestId__InputField")
        self.DatePicker = page.get_by_test_id("TestId__DatePicker").get_by_test_id("TestId__InputField")
        today = date.today()
        self.TodayDate = page.get_by_role("button", name=today.strftime("%B %d, %Y"))
        self.PasswordField = page.get_by_label("Password*")
        self.SubmitBtn = page.get_by_test_id("TestId__SignupButton")
        self.MyAccountLabel = page.get_by_role("heading", name="My Account")




