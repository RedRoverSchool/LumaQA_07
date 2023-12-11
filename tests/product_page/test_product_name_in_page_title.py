import pytest
from data.product_page_data import PRODUCT_PAGE_URL_LIST, TIMEOUT
from locators.product_page_locators import ProductPageLocators
from pages.product_page.product_page import ProductPage


@pytest.mark.parametrize("url", PRODUCT_PAGE_URL_LIST)
def test_product_name_in_page_title(driver, url):
    """
    TC_002.001.003 | Product page > Title > Product name in the page title
    Precondition:
    A guest user on any product page (link as example).
    Steps:
    1.	Verify that current product name is displayed on the page title.
    Expected result:
    Current product name is displayed in the page title.
    """
    product_page = ProductPage(driver, url)
    product_page.open()
    product_name = product_page.is_visible(ProductPageLocators.PRODUCT_NAME, TIMEOUT)
    assert product_name.text == product_page.page_title()
