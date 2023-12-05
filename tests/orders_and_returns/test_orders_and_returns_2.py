import allure
from pages.orders_and_returns.orders_and_returns_page import OrdersAndReturnsPage


class TestOrdersAndReturnsPage:

    @allure.title("TC_012.008.001 | 'Orders and Returns' > "
                  "Verify finding criterion is 'Billing ZIP code' upon choosing 'ZIP code' in 'Find Order By' field")
    def test_finding_criterion_is_billing_zip_code(self, driver):
        page = OrdersAndReturnsPage(driver, OrdersAndReturnsPage.URL)
        page.open()
        page.get_find_order_by_default_value()
        page.select_zip_code()
        page.is_search_field_name_visible()

        assert page.get_search_field_name_text() == "Billing ZIP Code", "The search field name is different"
