import allure
from pages.orders_and_returns.orders_and_returns_page import OrdersAndReturnsPage


class TestOrdersAndReturnsPage:

    @allure.title("TC_012.008.001 | 'Orders and Returns' > "
                  "Verify finding criterion is 'Billing ZIP code' upon choosing 'ZIP code' in 'Find Order By' field")
    def test_finding_criterion_is_billing_zip_code(self, driver):
        page = OrdersAndReturnsPage(driver, OrdersAndReturnsPage.URL)
        page.open()
        page.is_find_order_by_default_value_equal_to_email()
        page.select_zip_code()
        page.is_search_field_name_for_zip_code_visible()

        assert page.get_search_field_name_text_zip_code() == "Billing ZIP Code", "The search field name is different"

    @allure.title("TC_012.008.002 | 'Orders and Returns' > "
                  "Verify the finding criterion is 'Email' upon choosing 'Email' in 'Find Order By' field")
    def test_finding_criterion_is_email(self, driver):
        page = OrdersAndReturnsPage(driver, OrdersAndReturnsPage.URL)
        page.open()
        page.select_zip_code()
        page.is_find_order_by_value_equal_to_zip()
        page.select_email()

        assert page.get_search_field_name_text_email() == "Email", "The search field name is different"

    @allure.title("TC_012.008.003 | “Orders and Returns” "
                  "> Visibility and clickability > Verify the 'Continue' button is visible and clickable")
    def test_continue_button_is_visible_and_clickable(self, driver):
        page = OrdersAndReturnsPage(driver, OrdersAndReturnsPage.URL)
        page.open()

        assert page.is_continue_button_visible(), "'Continue' button is not visible"
        assert page.is_continue_button_clickable(), "'Continue' button is not clickable"
