from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.base_page_locators import BasePageLocators


class LoginPage(BasePage):
    def email(self) -> WebElement:
        return self.is_visible(LoginPageLocators.EMAIL)

    def password(self) -> WebElement:
        return self.is_visible(LoginPageLocators.PASSWORD)

    def button_sign_in(self) -> WebElement:
        return self.is_clickable(LoginPageLocators.BUTTON_SIGN_IN)

    def button_forgot_password(self) -> WebElement:
        return self.is_clickable(LoginPageLocators.BUTTON_FORGOT_PASSWORD)
