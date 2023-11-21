import pytest
from data.product_page_data import PRODUCT_PAGE_URL_LIST, TIMEOUT
from pages.product_page.product_page import ProductPage
from locators.item_page_locators import ColorSizeBlockLocators


@pytest.mark.parametrize("url", PRODUCT_PAGE_URL_LIST)
def test_color_choice(driver, url):
    """TC_002.013.001"""
    product_page = ProductPage(driver, url)
    product_page.open()

    first_color_button = product_page.the_presence_of_element_located(ColorSizeBlockLocators.COLOR, TIMEOUT)
    first_color_button.click()
    assert first_color_button.get_attribute('aria-checked') == 'true'
    selected_color = product_page.the_presence_of_element_located(ColorSizeBlockLocators.SELECTED_COLOR, TIMEOUT)
    assert selected_color.text == first_color_button.get_attribute('aria-label')
