import pytest
from selenium.webdriver.remote.webelement import WebElement
from LumaQA_07.base.seleniumbase import BasePage
from LumaQA_07.locators.login_page_locators import LoginPageLocators
from LumaQA_07.locators.base_page_locators import BasePageLocators



class LoginPage(BasePage):
    def email(self) -> WebElement:
        return self.is_visible(LoginPageLocators.EMAIL)

    def password(self) -> WebElement:
        return self.is_visible(LoginPageLocators.PASSWORD)

    def button_sign_in(self) -> WebElement:
        return self.is_clickable(LoginPageLocators.BUTTON_SIGN_IN)

    def button_forgot_password(self) -> WebElement:
        return self.is_clickable(LoginPageLocators.BUTTON_FORGOT_PASSWORD)

    def sign_in(self):
        self.email().send_keys('testTestpro@gmail.com')
        self.password().send_keys('Zaqxsw100')
        self.button_sign_in().click()
        assert self.header().text == 'My Account', "Не удалось войти"


class MyAccountPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/customer/account/'

    def check_visibility_of_sale_section(self):
        return self.is_visible(BasePageLocators.SALE_SECTION)

    def check_clickability_of_sale_section(self):
        return self.is_clickable(BasePageLocators.SALE_SECTION)

