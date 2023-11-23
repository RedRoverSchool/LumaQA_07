import pytest
from pages.login.password_forgot import ForgotPassPage
from pages.login.login_page import LoginPage




def test_password_forgot(driver):
    page = ForgotPassPage(driver, 'https://magento.softwaretestingboard.com/customer/account/login/')
    page.open()
    page.forgot_password()
    assert "Forgot Your Password?" in driver.page_source


def test_valid_email_password_forgot(driver):
    page = ForgotPassPage(driver, 'https://magento.softwaretestingboard.com/customer/account/login/')
    page.open()
    page.forgot_password()
    page.valid_email_forgot_password()
    page.click_button_reset_password()
    page.after_text_reset_email()
    assert 'If there is an account associated with ivanov@yandex.ru you will receive'
    'an email with a link to reset your password.'==page.after_text_reset_email()

def test_not_valid_email_password_forgot(driver):
    page = ForgotPassPage(driver, 'https://magento.softwaretestingboard.com/customer/account/forgotpassword/')
    page.open()
    page.not_valid_email_forgot_password()
    page.click_button_reset_password()
    assert 'Please enter a valid email address (Ex: johndoe@domain.com).' in driver.page_source




