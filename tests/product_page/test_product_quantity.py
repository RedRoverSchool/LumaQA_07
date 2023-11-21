from data.product_page_data import PRODUCT_PAGE_EXAMPLE
from locators.product_page_locators import ProductPageLocators
from pages.product_page.product_page import ProductPage


class TestPageOfProducts:
    def test_product_quantity_is_displayed(self, driver):
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        element = page.is_visible(ProductPageLocators.PRODUCT_QUANTITY)
        assert element.is_displayed(), 'product quantity is not visible'

