import time
from pages.account.sign_in import ForgotPage
import pytest


def test_link_forgot_password(driver):
    #
    page = ForgotPage(driver, url=ForgotPage.URL_LOGIN)
    page.open()
    page.forgot_password().click()
    text = page.verify_text_forgot_password()
    assert text == ForgotPage.SUCCESS_FORGOT_PASS, f'Expected result: {ForgotPage.SUCCESS_FORGOT_PASS}, but got: {text}'


@pytest.mark.parametrize('test_email', ["test@com", "test@tescom", "test.com", 'test@'])
def test_email_not_valid_format(driver, test_email):
    page = ForgotPage(driver, url=ForgotPage.URL)
    page.open()
    page.email = test_email
    page.reset_password().click()
    text = page.wrong_email()
    assert text == ForgotPage.WRONG_EMAIL, f'Expected result: {ForgotPage.WRONG_EMAIL}, but got: {text}'

@pytest.mark.parametrize('test_email', ["test@test.com", "testpro@tes.com"])
def test_email_valid_format(driver, test_email):
    page = ForgotPage(driver, url=ForgotPage.URL)
    page.open()
    page.email = test_email
    page.reset_password().click()
    message = page.success_reset()
    assert message == ForgotPage.SUCCESS % test_email, (f'Expected result: {ForgotPage.SUCCESS % test_email}, '
                                                        f'but got: {message}')
    assert page.current_url == ForgotPage.URL_DONE, "Unexpected page URL"



