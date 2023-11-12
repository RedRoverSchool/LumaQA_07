from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import BasePage
from pages.login.login_page import LoginPage
from locators.login_page_locators import LoginPageLocators, ForgotPasswordPageLocators
from locators.base_page_locators import BasePageLocators

class ForgotPasswordPage(LoginPage):

    def verify_text_forgot_password(self):
        serch_text = self.is_clickable(ForgotPasswordPageLocators.FORGOT_PASSWORD_TEXT)
        return serch_text.text
