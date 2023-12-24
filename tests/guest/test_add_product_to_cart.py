from pages.main_page import MainPage
from pages.cart_page import CartPage
from locators.base_page_locators import BasePageLocators as bpl
from locators.item_page_locators import ItemPageLocators as ipl
from locators.order_and_payment_locators import OrdersAndPaymentPageLocators as opl


""" TC_004.001.002 | Authorization >Anonym user > Adding item to the cart
    Pre-conditions:
        User is not logged in
        Shopping cart is empty
        The page Home Page is opened

    Steps:
        Click “Shop New Yoga” button in “New Luma Yoga Collection” widget
        Hover over “Echo Fit Compression Short” product card
        Choose “28” in “size” radiobutton on the item’s card
        Choose “black” in “color” radiobutton on the item’s card
        Click “Add to cart” button
        Click “Cart” button
        Click “View and Edit Cart”

    Expected results:
        Shopping Cart page is opened
        “Echo Fit Compression Short” with chosen Size and Color is visible"""


def test_guest_add_item(driver):
    page = MainPage(driver, MainPage.URL)
    page.open()
    page.is_clickable(bpl.SHOP_NEW_YOGA).click()
    page.is_clickable(ipl.LINK_EFCS_SIZE_28).click()
    page.is_clickable(ipl.LINK_EFCS_SIZE_BLACK).click()
    add_to_cart_button = page.is_clickable(ipl.LINK_EFCS_ADD_TO_CART)
    page.move_to_element_and_click(add_to_cart_button)
    page.is_visible(bpl.MSG_SUCCESS)
    page.is_clickable(opl.SHOPPING_CART_BUTTON).click()
    page.is_clickable(opl.VIEW_AND_EDIT_CART).click()
    item_options = page.is_visible(opl.CART_ITEM_OPTIONS).text.split("\n")
    assert page.current_url == CartPage.URL, 'Wrong redirection after adding item to cart'
    assert page.is_visible(opl.CART_ITEM_TITLE).text == 'Echo Fit Compression Short', 'Wrong title of item in the cart'
    assert item_options[1] == '28', 'Wrong size of item in the cart'
    assert item_options[3] == 'Black', 'Wrong color of item in the cart'