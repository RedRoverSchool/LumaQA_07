from locators.base_page_locators import BasePageLocators
from pages.main_page import MainPage


def test_popup_window_is_displayed_after_clicking(driver):
    page = MainPage(driver=driver, url=MainPage.URL)
    page.open()
    page.add_clamber_watch_from_gear_catalog_to_cart()
    cart_counter_number = page.is_visible(BasePageLocators.CART_COUNTER_NUMBER).text
    page.is_visible(BasePageLocators.CART_ICON).click()
    block_minicart_item_quantity = page.is_visible(BasePageLocators.BLOCK_MINICART_ITEM_QUANTITY).get_attribute("data-item-qty")

    assert page.is_visible(BasePageLocators.BLOCK_MINICART)
    assert cart_counter_number == block_minicart_item_quantity and cart_counter_number == '1'
