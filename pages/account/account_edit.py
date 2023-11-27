from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage


class AccountEditPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/customer/account/edit/"

    FIRST_NAME = (By.CSS_SELECTOR, "input#firstname")
    LAST_NAME = (By.CSS_SELECTOR, "input#lastname")
    CHANGE_EMAIL = (By.CSS_SELECTOR, "input#change-email")
    CHANGE_PASSWORD = (By.CSS_SELECTOR, "input#change-password")
    EMAIL = (By.CSS_SELECTOR, "input#email")
    PASSWORD_CURRENT = (By.CSS_SELECTOR, "input#current-password")

    PASSWORD = (By.CSS_SELECTOR, "input#password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input#password-confirmation")
    MESSAGE_CHANGE_PASSWORD_ERROR = (By.CSS_SELECTOR, '#password-error')
    MESSAGE_CONFIRM_CHANGE_PASSWORD_ERROR = (By.CSS_SELECTOR, '#password-confirmation-error')
    MESSAGE_CURRENT_PASSWORD_ERROR = (By.CSS_SELECTOR, '#current-password-error')

    SAVE = (By.CSS_SELECTOR, "button.save")

    SUCCESS = "You saved the account information."
    ERROR_EMAIL_IN_USE = "A customer with the same email address already exists in an associated website."

    CHANGE_PASSWORD_ERROR = 'This is a required field.'

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url

    @property
    def first_name(self):
        return self.is_visible(self.FIRST_NAME)

    @first_name.setter
    def first_name(self, val: str):
        self.clear_and_send_keys(self.first_name, val)

    @property
    def last_name(self):
        return self.is_visible(self.LAST_NAME)

    @last_name.setter
    def last_name(self, val: str):
        self.clear_and_send_keys(self.last_name, val)

    def change_email(self):
        return self.is_clickable(self.CHANGE_EMAIL)

    def change_password(self):
        return self.is_clickable(self.CHANGE_PASSWORD)

    @property
    def email(self):
        return self.is_visible(self.EMAIL)

    @email.setter
    def email(self, val: str):
        self.clear_and_send_keys(self.email, val)

    @property
    def password_current(self):
        return self.is_visible(self.PASSWORD_CURRENT)

    @password_current.setter
    def password_current(self, val: str):
        self.clear_and_send_keys(self.password_current, val)

    @property
    def password(self):
        return self.is_visible(self.PASSWORD)

    @password.setter
    def password(self, val: str):
        self.clear_and_send_keys(self.password, val)

    @property
    def password_confirm(self):
        return self.is_visible(self.PASSWORD_CONFIRM)

    @password_confirm.setter
    def password_confirm(self, val: str):
        self.clear_and_send_keys(self.password_confirm, val)

    def save(self):
        return self.is_clickable(self.SAVE)

    def message_change_password_error(self):
        password_error_msg = self.driver.find_element(*AccountEditPage.MESSAGE_CHANGE_PASSWORD_ERROR).text
        return password_error_msg

    def message_confirm_change_password_error(self):
        confirm_pass_error_msg = self.driver.find_element(*AccountEditPage.MESSAGE_CONFIRM_CHANGE_PASSWORD_ERROR).text
        return confirm_pass_error_msg

    def message_current_password_error(self):
        confirm_pass_error_msg = self.driver.find_element(*AccountEditPage.MESSAGE_CURRENT_PASSWORD_ERROR).text
        return confirm_pass_error_msg
