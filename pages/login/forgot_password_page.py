from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import BasePage
from pages.login.login_page import LoginPage
from locators.login_page_locators import LoginPageLocators, ForgotPasswordPageLocators
from locators.base_page_locators import BasePageLocators


class ForgotPasswordPage(LoginPage):

    def verify_text_forgot_password(self) -> str:
        serch_text = self.is_clickable(ForgotPasswordPageLocators.FORGOT_PASSWORD_TEXT)
        return serch_text.text

    def email_fild_with_not_valid_format(self) -> WebElement:
        return self.is_clickable(ForgotPasswordPageLocators.EMAIL)

    def button_reset_password(self) -> WebElement:
        return self.is_clickable(ForgotPasswordPageLocators.BUTTON_RESET_MY_PASSWORD)

    def error_email_text(self) -> str:
        return self.is_visible(ForgotPasswordPageLocators.EMAIL_ERROR_MESS).text
