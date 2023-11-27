import pytest

from pages.header.header_page import Header
from data.test_urls_list import HEADER_TEST_URLS
from locators.base_page_locators import BasePageLocators
from pages.main_page import MainPage
from data.home_page_url import HOME_PAGE


@pytest.mark.parametrize('URL', HEADER_TEST_URLS)
def test_tc_003_001_001_logo_is_visible(driver, URL):
    page = Header(driver, URL)
    page.open()
    page.check_logo_visibility()


def test_popup_window_is_displayed_after_clicking(driver):
    page = MainPage(driver=driver, url=MainPage.URL)
    page.open()
    page.add_clamber_watch_from_gear_catalog_to_cart()
    cart_counter_number = page.is_visible(BasePageLocators.CART_COUNTER_NUMBER).text
    page.is_visible(BasePageLocators.CART_ICON).click()
    block_minicart_item_quantity = page.is_visible(BasePageLocators.BLOCK_MINICART_ITEM_QUANTITY).get_attribute("data-item-qty")

    assert page.is_visible(BasePageLocators.BLOCK_MINICART)
    assert cart_counter_number == block_minicart_item_quantity and cart_counter_number == '1'


@pytest.mark.parametrize('URL', HEADER_TEST_URLS)
def test_tc_003_001_003_logo_redirects_main_page(driver, URL):
    page = Header(driver, URL)
    page.open()
    page.hold_mouse_on_element_and_click(BasePageLocators.LOGO_TITLE)
    page.check_logo_redirection()

@pytest.mark.parametrize('URL', HEADER_TEST_URLS)
def test_tc_003_002_001_searchbar_visible_all_pages(driver, URL):
    page = Header(driver, URL)
    page.open()
    page.check_header_visibility()