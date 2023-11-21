from data.product_page_data import PRODUCT_PAGE_EXAMPLE
from locators.product_page_locators import ProductPageLocators
from pages.product_page.product_page import ProductPage


class TestPageOfProducts:
    def test_add_to_block_is_visible(self, driver):
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        element = page.is_visible(ProductPageLocators.ADD_TO_BLOCK)
        assert element.is_displayed(), 'heart sigh not visible'
