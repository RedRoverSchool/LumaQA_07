import pytest

from pages.header.header_page import Header
from data.test_urls_list import HEADER_TEST_URLS
from locators.base_page_locators import BasePageLocators
from pages.gear_page.gear_page import GearPage


@pytest.mark.parametrize('URL', HEADER_TEST_URLS)
def test_tc_003_001_001_logo_is_visible(driver, URL):
    page = Header(driver, URL)
    page.open()
    page.check_logo_visibility()


def test_popup_window_is_displayed_after_clicking(driver):
    page = GearPage(driver)
    page.open()
    page.add_clamber_watch_from_gear_catalog_to_cart()
    page.is_visible(BasePageLocators.CART_ICON).click()

    assert page.is_visible(BasePageLocators.BLOCK_MINICART)


def test_popup_window_and_cart_counter_are_displayed_after_clicking(driver):
    page = GearPage(driver)
    page.open()
    page.add_clamber_watch_from_gear_catalog_to_cart(quantity=2)
    page.add_endurance_watch_from_gear_catalog_to_cart()
    cart_counter_number = page.is_visible(BasePageLocators.CART_COUNTER_NUMBER).text
    page.is_visible(BasePageLocators.CART_ICON).click()
    block_minicart_item_quantity = page.is_visible(BasePageLocators.BLOCK_MINICART_ITEM_QUANTITY).text
    expected_items_number = "3"

    assert cart_counter_number == expected_items_number
    assert block_minicart_item_quantity == expected_items_number


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
