from base.seleniumbase import BasePage
from locators.wish_list_locators import WishListLocators


class WishListPage(BasePage):

    def click_share_wish_list_button(self):
        self.find_element_and_click(WishListLocators.SHARE_WISH_LIST_BUTTON)

    def fill_email_field(self, email):
        fill_email_field = self.driver.find_element(*WishListLocators.EMAIL_ADDRESS_TEXT_BOX)
        fill_email_field.send_keys(email)

    def fill_message_field(self, message):
        fill_message_field = self.driver.find_element(*WishListLocators.MESSAGE_FIELD_TEXT_BOX)
        fill_message_field.send_keys(message)
