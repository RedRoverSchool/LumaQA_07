from pages.login.login_page import LoginPage
from selenium.webdriver.remote.webelement import WebElement
from locators.login_page_locators import ResetPageLocators


class ResetPage(LoginPage):
    def email(self) -> WebElement:
        return self.is_visible(ResetPageLocators.EMAIL)

    def button_reset_password(self) -> WebElement:
        return self.is_clickable(ResetPageLocators.BUTTON_RESET_PASSWORD)

    def success_message(self) -> str:
        return self.is_visible(ResetPageLocators.SUCCESS_MESSAGE).text

    def error_message(self) -> str:
        return self.is_visible(ResetPageLocators.ERROR_MESSAGE).text

    def error_alert_message(self) -> str:
        return self.is_visible(ResetPageLocators.ERROR_ALERT).text
