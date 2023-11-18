import pytest
from selenium.common import TimeoutException

from data.product_page_data import PRODUCT_PAGE_URL_LIST, MIN_TIMEOUT, TIMEOUT
from locators.product_page_locators import ProductPageLocators
from pages.product_page.product_page import ProductPage


@pytest.mark.parametrize("url", PRODUCT_PAGE_URL_LIST)
def test_product_page_body_structure(driver, url):
    """
    TC_002.003.003 | Product page > DOM > Body structure

    Precondition:
    A guest user on any product page (link as example).
    
    Steps:
    Verify that the product page body contains the following elements:
        1. div class="product-info-main"
        2. div class="product media"
        3. div class="product info detailed"
    And one of (depends on product type but without logic):
        - div class="block related"
        - div class="upsell"
    
    Expected result:
    Any product page body DOM contains all numbered elements and one of the bulleted elements.
    """
    product_page = ProductPage(driver, url)
    product_page.open()
    assert product_page.is_visible(ProductPageLocators.MAIN_INFO, TIMEOUT)
    assert product_page.is_visible(ProductPageLocators.PICTURES, TIMEOUT)
    assert product_page.is_visible(ProductPageLocators.DETAILED_INFO, TIMEOUT)

    # Since I didn't find the distribution logic with related and liked products, I just check if one of them exists
    related_products_visible = None
    liked_products_visible = None
    try:
        related_products_visible = product_page.is_visible(ProductPageLocators.RELATED_PRODUCTS, MIN_TIMEOUT)
    except TimeoutException:
        pass
    try:
        liked_products_visible = product_page.is_visible(ProductPageLocators.LIKED_PRODUCTS, MIN_TIMEOUT)
    except TimeoutException:
        pass

    assert related_products_visible or liked_products_visible


