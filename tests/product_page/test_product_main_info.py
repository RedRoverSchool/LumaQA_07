from pages.product_page.product_main_info import ProductPage
from data.product_page_data import PRODUCT_PAGE_EXAMPLE

class TestProductPage:

    def test_check_product_name_in_main_info(self, driver):
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        text = page.check_product_name_in_main_info()
        assert text == "Breathe-Easy Tank"
