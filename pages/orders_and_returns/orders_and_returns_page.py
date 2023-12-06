from base.seleniumbase import BasePage
from locators.orders_and_returns_locators import OrdersAndReturnsPageLocators as ORPL
from data.footer_urls import ORDERS_AND_RETURNS_PAGE
from selenium.webdriver.support.ui import Select


class OrdersAndReturnsPage(BasePage):
    URL = ORDERS_AND_RETURNS_PAGE

    def is_find_order_by_default_value_equal_to_email(self):
        """The method checks the default value of the 'Find Order By' field is 'email'"""
        find_order_by_value = self.is_visible(ORPL.FIND_ORDER_BY_DROPDOWN).get_attribute("value")
        assert find_order_by_value == "email"

    def select_zip_code(self):
        """The method selects 'ZIP code' as the search criterion"""
        order_by_dropdown = self.is_visible(ORPL.FIND_ORDER_BY_DROPDOWN)
        dropdown = Select(order_by_dropdown)
        dropdown.select_by_visible_text("ZIP Code")

    def is_search_field_name_for_zip_code_visible(self):
        """The method verifies if 'Search field' name for Zip code is visible"""
        return self.is_visible(ORPL.POSTCODE_FIELD_NAME)

    def get_search_field_name_text_zip_code(self):
        """The method gets the search field name upon choosing 'ZIP Code'"""
        return self.is_search_field_name_for_zip_code_visible().text

    def is_find_order_by_value_equal_to_zip(self):
        """The method verifies if the 'Find order by' field value is 'zip'"""
        find_order_by_value = self.is_visible(ORPL.FIND_ORDER_BY_DROPDOWN).get_attribute("value")
        assert find_order_by_value == "zip"

    def select_email(self):
        """The method selects 'Email' as the search criterion"""
        order_by_dropdown = self.find_element(ORPL.FIND_ORDER_BY_DROPDOWN)
        dropdown = Select(order_by_dropdown)
        dropdown.select_by_visible_text("Email")

    def is_search_field_name_for_email_visible(self):
        """The method verifies if 'Search field' name for Email is visible"""
        return self.is_visible(ORPL.EMAIL_FIELD_NAME)

    def get_search_field_name_text_email(self):
        """The method gets the search field name upon choosing 'Email'"""
        return self.is_search_field_name_for_email_visible().text
