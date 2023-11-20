from pages.product_page.product_main_info import ProductPage
from data.product_page_data import PRODUCT_PAGE_EXAMPLE

class TestProductPage:

    def test_check_product_name_in_main_info(self, driver):
        """TC_002.005.001"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        text = page.check_product_name_in_main_info()
        assert text == "Breathe-Easy Tank"

    def test_rating_block_is_visible(self, driver):
        """TC_002.005.002"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        assert page.rating_block_is_visible()

    def test_price_block_is_visible(self, driver):
        """TC_002.005.003"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        assert page.price_block_is_visible()

    def test_availability_block_is_displayed(self, driver):
        """TC_002.005.004"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        assert page.availability_block_is_displayed(), "Availability is not displayed"

    def test_clickability_add_to_cart(self, driver,):
        """TC_002.015.002"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        page.choose_size()
        page.choose_color()
        page.click_add_to_cart()

        assert page.counter_number_is_visible(), "'Add to cart' button is not clickability"

