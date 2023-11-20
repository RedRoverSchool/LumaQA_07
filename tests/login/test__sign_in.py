import time

from data.fake_data import FakeData
from locators.login_page_locators import LoginPageLocators
from pages.account.create_account import CreateAccountPage
from pages.account.my_account import MyAccountPage
from pages.account.sign_in import SignInPage, ForgotPage
from pages.login.login_page import LoginPage
from pages.login.logout_page import LogoutPage


def test_sign_in(driver):
    page = LoginPage(driver, LoginPageLocators.URL)
    page.open()
    page.sign_in()
    assert page.header().text == 'My Account', 'Не удалось войти'


class TestX(FakeData):
    def test_correct_credentials_login(self, driver):
        page = CreateAccountPage(driver)
        password_current = page.password
        email_current = page.email
        LogoutPage(driver)
        page = SignInPage(driver)
        page.email = email_current
        page.password_one = password_current
        page.sign_in().click()
        assert page.current_url == MyAccountPage.URL, "Login with correct credentials failed"

    def test_bad_credentials_login(self, driver):
        page = CreateAccountPage(driver)
        password_current = page.password
        email_current = page.email
        LogoutPage(driver)
        page = SignInPage(driver)
        page.email = email_current
        page.password_one = password_current[:-1]
        page.sign_in().click()
        assert page.current_url == SignInPage.URL, "Unexpected page URL"
        assert page.message_error == SignInPage.ERROR, "Successful login with bad credentials"

    def test_reset_password(self, driver):
        email_current = CreateAccountPage(driver).email
        LogoutPage(driver)
        page = ForgotPage(driver)
        page.email = email_current
        page.reset_password().click()
        assert page.current_url == ForgotPage.URL_DONE, "Unexpected page URL"
        assert page.message_success == ForgotPage.SUCCESS % email_current, "Message not as expected"
