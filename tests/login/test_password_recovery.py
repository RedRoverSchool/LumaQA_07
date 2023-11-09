from pages.login.password_recovery import ResetPage
from locators.login_page_locators import ResetPageLocators
import pytest
import time


def test_password_reset(driver):
    page = ResetPage(driver, url='https://magento.softwaretestingboard.com/customer/account/login')
    page.open()
    page.button_forgot_password().click()
    page.email().send_keys('sve3363@gmail.com')
    page.button_reset_password().click()
    assert page.success_message() == ('If there is an account associated with sve3363@gmail.com you'
                                      ' will receive an email with a link to reset your password.')


@pytest.mark.parametrize('email_pull', ["abc@abc", "abc@abc.", "@abc.com", "@.", pytest.param("Aa!#$%^&*@google.com", marks=pytest.mark.xfail)])
def test_password_reset_not_valid_email_pull(driver, email_pull):
    page = ResetPage(driver, url=ResetPageLocators.FORGOT_PASS_URL)
    page.open()
    page.email().send_keys(email_pull)
    time.sleep(1)  # без time sleep нестабильное и разное поведение сайта
    page.button_reset_password().click()
    assert page.error_message() == 'Please enter a valid email address (Ex: johndoe@domain.com).'


def test_password_reset_not_valid_email(driver):
    page = ResetPage(driver, url=ResetPageLocators.FORGOT_PASS_URL)
    page.open()
    page.email().send_keys("abc")
    time.sleep(1)  # без time sleep нестабильное поведение сайта
    page.button_reset_password().click()
    assert page.error_message() == 'Please enter a valid email address (Ex: johndoe@domain.com).'


def test_password_reset_no_email_filled(driver):
    page = ResetPage(driver, url=ResetPageLocators.FORGOT_PASS_URL)
    page.open()
    time.sleep(1) # без time sleep нестабильное поведение сайта
    page.button_reset_password().click()
    assert page.error_message() == 'This is a required field.'


def test_password_reset_not_valid_cyrillic_email(driver):
    page = ResetPage(driver, url=ResetPageLocators.FORGOT_PASS_URL)
    page.open()
    page.email().send_keys("@почта.рф")
    time.sleep(1)  # без time sleep нестабильное поведение сайта
    page.button_reset_password().click()
    assert page.error_message() == 'Please enter a valid email address (Ex: johndoe@domain.com).'


def test_password_reset_valid_cyrillic_email(driver):
    page = ResetPage(driver, url=ResetPageLocators.FORGOT_PASS_URL)
    page.open()
    page.email().send_keys("привет@почта.рф")
    time.sleep(1)  # без time sleep нестабильное поведение сайта
    page.button_reset_password().click()
    assert page.error_alert_message() == 'The email address is incorrect. Verify the email address and try again.'


def test_password_reset_valid_long_email(driver):
    page = ResetPage(driver, url=ResetPageLocators.FORGOT_PASS_URL)
    page.open()
    page.email().send_keys(ResetPageLocators.LONG_EMAIL)
    time.sleep(1)  # без time sleep нестабильное поведение сайта
    page.button_reset_password().click()
    assert page.error_alert_message() == 'The email address is incorrect. Verify the email address and try again.'
