from pages.main_page import MainPage
from pages.cart_page import CartPage
from locators.base_page_locators import BasePageLocators as bpl
from locators.item_page_locators import ItemPageLocators as ipl
from locators.order_and_payment_locators import OrdersAndPaymentPageLocators as opl


""" TC_004.001.003 | Authorization >Anonym user > Changing item in the cart
    Pre-conditions:
        User is not logged in
        Shopping cart is empty
        The page Home Page is opened
    
    Steps:
        Click “Shop New Yoga” button in “New Luma Yoga Collection” widget
        Hover over “Echo Fit Compression Short” product card
        Choose “28” in “size” rdiobutton on the item’s card
        Choose “black” in “color” rdiobutton on the item’s card
        Click “Add to cart” button
        Click “Cart” button
        Click “View and Edit Cart”
        Click “Edit item parameters” button
        Change “Size” to “29”
        Change “Color” to “Blue”
        Click “Update Cart” button
        Click “Update Shopping Cart” button
    
    Expected results:
    Shopping Cart page is opened
    “Echo Fit Compression Short” with changed Size and Color is visible"""


def test_guest_change_item_in_cart(driver):
    page = MainPage(driver, MainPage.URL)
    page.open()
    page.is_clickable(bpl.SHOP_NEW_YOGA).click()
    page.is_clickable(ipl.LINK_EFCS_SIZE_28).click()
    page.is_clickable(ipl.LINK_EFCS_SIZE_BLACK).click()
    page.is_clickable(ipl.LINK_EFCS_ADD_TO_CART).click()
    page.is_visible(bpl.MSG_SUCCESS)
    page.is_clickable(opl.SHOPPING_CART_BUTTON).click()
    page.is_clickable(opl.VIEW_AND_EDIT_CART).click()
    page.is_clickable(opl.CART_EDIT_ITEM).click()
    page.is_clickable(ipl.LINK_EFCS_SIZE_29).click()
    page.is_clickable(ipl.LINK_EFCS_SIZE_BLUE).click()
    page.is_clickable(opl.UPDATE_CART_BUTTON).click()
    page.is_visible(bpl.MSG_SUCCESS)
    item_options = page.is_visible(opl.CART_ITEM_OPTIONS).text.split("\n")
    assert page.current_url == CartPage.URL, 'Wrong redirection after adding item to cart'
    assert page.is_visible(opl.CART_ITEM_TITLE).text == 'Echo Fit Compression Short', 'Wrong title of item in the cart'
    assert item_options[1] == '29', 'Wrong size of item in the cart'
    assert item_options[3] == 'Blue', 'Wrong color of item in the cart'