from pages.login.forgot_password_page import ForgotPasswordPage
# from pages.login.forgot_password_page import ForgotPasswordPage
from locators.login_page_locators import ResetPageLocators, LoginPageLocators, ForgotPasswordPageLocators
import pytest

def test_link_forgot_password(driver):
    page = ForgotPasswordPage (driver, url=LoginPageLocators.URL)
    page.open()
    page.button_forgot_password().click()
    text = page.verify_text_forgot_password()
    assert text == ForgotPasswordPageLocators.TEXT, f'Expected result: {text}, but got: {ForgotPasswordPageLocators.TEXT}'
