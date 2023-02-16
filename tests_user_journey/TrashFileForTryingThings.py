import time

import pytest

currentTimeStamp = str(time.time())
print(currentTimeStamp)
print(currentTimeStamp[6:10])


# This is an example for parametrizing the test with test data
@pytest.skip
@pytest.mark.parametrize("email", ["symon.storozhenko@gmail.com",
                                   pytest.param("fakeemail", marks=pytest.mark.xfail),
                                   pytest.param("symon.storozhenko@gmail", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("passwrd", ["test123",
                                     pytest.param("fakepasswrd", marks=pytest.mark.xfail),
                                     "test123"])
def test_user_can_login(page, email, passwrd) -> None:
    # page.click("[data-testid='siteMembers.container'] input[type='email']")
    # page.fill("[data-testid='siteMembers.container'] input[type='email']", "symon.storozhenko@gmail.com")
    page.fill('input:below(:text("Email"))', email)
    page.press("[data-testid='siteMembers.container'] >> input[type='email']", "Tab")
    page.fill("input[type='password']", passwrd)
