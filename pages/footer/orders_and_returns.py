from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import BasePage
from locators.orders_and_returns_locators import OrdersAndReturnsPageLocators


class OrdersAndReturnsPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/sales/guest/form/"

    def order_id_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.ORDER_ID_FIELD)

    def get_value_order_id_field(self):
        return self.is_visible(OrdersAndReturnsPageLocators.ORDER_ID_FIELD).get_attribute('value')

    def error_msg_order_id_not_filled(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.ORDER_ID_FIELD_MESSAGE_ERROR)

    def billing_lastname_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.BILLING_LASTNAME_FIELD)

    def get_value_billing_lastname_field(self):
        return self.is_visible(OrdersAndReturnsPageLocators.BILLING_LASTNAME_FIELD).get_attribute('value')

    def error_msg_billing_lastname_not_filled(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.BILLING_LASTNAME_FIELD_MESSAGE_ERROR)

    def email_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.EMAIL_FIELD)

    def get_value_email_field(self):
        return self.is_visible(OrdersAndReturnsPageLocators.EMAIL_FIELD).get_attribute('value')

    def email_field_name(self):
        return self.is_visible(OrdersAndReturnsPageLocators.EMAIL_FIELD_NAME)

    def error_msg_email_not_filled_or_incorrect_type(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.EMAIL_FIELD_MESSAGE_ERROR)

    def find_order_by_dropdown(self) -> WebElement:
        return self.is_clickable(OrdersAndReturnsPageLocators.FIND_ORDER_BY_DROPDOWN)

    def select_find_order_by_email_dropdown(self):
        self.find_order_by_dropdown().click()
        return self.is_clickable(OrdersAndReturnsPageLocators.FIND_ORDER_BY_EMAIL_DROPDOWN).click()

    def billing_postcode_field(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.POSTCODE_FIELD)

    def get_value_postcode_field(self):
        return self.is_visible(OrdersAndReturnsPageLocators.POSTCODE_FIELD).get_attribute('value')

    def billing_postcode_field_name(self):
        return self.is_visible(OrdersAndReturnsPageLocators.POSTCODE_FIELD_NAME)

    def error_msg_billing_postcode_not_filled(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.POSTCODE_FIELD_MESSAGE_ERROR)

    def error_msg_incorrect_data(self) -> WebElement:
        return self.is_visible(OrdersAndReturnsPageLocators.INCORRECT_DATA_MESSAGE)

    def continue_button(self):
        return self.is_clickable(OrdersAndReturnsPageLocators.CONTINUE_BUTTON)

    def go_to_continue_button(self):
        self.hold_mouse_on_element(OrdersAndReturnsPageLocators.CONTINUE_BUTTON)
        return self.is_clickable(OrdersAndReturnsPageLocators.CONTINUE_BUTTON)

    def order_status(self):
        return self.is_visible(OrdersAndReturnsPageLocators.ORDER_STATUS)

    def text_order_number_on_view_order_page(self):
        return self.is_visible(OrdersAndReturnsPageLocators.ORDER_NUMBER_ON_VIEW_ORDER_PAGE)

    def select_find_order_by_postcode_dropdown(self):
        self.find_order_by_dropdown().click()
        return self.is_clickable(OrdersAndReturnsPageLocators.FIND_ORDER_BY_POSTCODE_DROPDOWN).click()

    def fill_all_field_with_email(self, order_id, billing_lastname, email):
        self.clear_and_send_keys(self.order_id_field(), order_id)
        self.clear_and_send_keys(self.billing_lastname_field(), billing_lastname)
        self.clear_and_send_keys(self.email_field(), email)

    def fill_all_field_with_postcode(self, order_id, billing_lastname, postcode):
        self.clear_and_send_keys(self.order_id_field(), order_id)
        self.clear_and_send_keys(self.billing_lastname_field(), billing_lastname)
        self.select_find_order_by_postcode_dropdown()
        self.billing_postcode_field_name()
        self.clear_and_send_keys(self.billing_postcode_field(), postcode)

    def find_order_by_email(self, order_id, billing_lastname, postcode):
        self.fill_all_field_with_email(order_id, billing_lastname, postcode)
        self.continue_button().click()

    def find_order_by_postcode(self, order_id, billing_lastname, postcode):
        self.fill_all_field_with_postcode(order_id, billing_lastname, postcode)
        self.continue_button().click()
