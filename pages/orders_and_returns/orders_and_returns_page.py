from base.seleniumbase import BasePage
from locators.orders_and_returns_locators import OrdersAndReturnsPageLocators as ORPL
from data.footer_urls import ORDERS_AND_RETURNS_PAGE
from selenium.webdriver.support.ui import Select


class OrdersAndReturnsPage(BasePage):
    URL = ORDERS_AND_RETURNS_PAGE

    def get_find_order_by_default_value(self):
        """The method checks the default value of the 'Find Order By' field is 'email'"""
        find_order_by_default = self.is_clickable(ORPL.FIND_ORDER_BY_DROPDOWN).get_attribute("value")
        assert find_order_by_default == "email"

    def select_zip_code(self):
        """The method selects 'ZIP code' as the search criterion"""
        order_by_dropdown = self.is_clickable(ORPL.FIND_ORDER_BY_DROPDOWN)
        dropdown = Select(order_by_dropdown)
        dropdown.select_by_visible_text("ZIP Code")

    def is_search_field_name_visible(self):
        """The method verifies if 'Search field' name is visible"""
        return self.is_visible(ORPL.POSTCODE_FIELD_NAME)

    def get_search_field_name_text(self):
        """The method gets the search field name"""
        return self.is_search_field_name_visible().text
