from locators.login_page_locators import LoginPageLocators, ForgotPasswordPageLocators, ResetPageLocators
from selenium.webdriver import Keys
from base.seleniumbase import BasePage
from pages.login.login_page import LoginPage




class ForgotPassPage(BasePage):
    def forgot_password(self):
        return self.is_visible(LoginPageLocators.BUTTON_FORGOT_PASSWORD).click()

    def valid_email_forgot_password(self):
        self.is_visible(ForgotPasswordPageLocators.EMAIL).send_keys('ivanov@yandex.ru')

    def click_button_reset_password(self):
        return self.is_visible(ResetPageLocators.BUTTON_RESET_PASSWORD).click()

    def after_text_reset_email(self):
          return self.is_visible(LoginPageLocators.RESET_PASS_MESS).text

    def not_valid_email_forgot_password(self):
        self.is_visible(ForgotPasswordPageLocators.EMAIL).send_keys('ivanov@')




