import time
from pages.main_page import MainPage
from locators.base_page_locators import BasePageLocators as bpl
from locators.item_page_locators import ItemPageLocators as ipl
from locators.order_and_payment_locators import OrdersAndPaymentPageLocators as opl
from pages.checkout_page import CheckoutPage
from locators.checkout_page_locators import CheckoutPageLocators as cpl


""" TC_004.001.004 | Authorization >Anonym user > Making order and payment > Positive
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
        Click “Proceed to Checkout”
        Type 123@gmail.com in “Email Address” field
        Type “Bob” in “First Name” field
        Type “Ivanov” in “Last Name” field
        Type “Street 5” in “Street Address” field
        Type “Minsk” in “City” field
        Select “Alabama” in “State/Province” dropdown menu
        Type “12345” in “Zip/Postal Code” field
        Select “United States” in “Country” dropdown menu
        Type “123” in “Phone number” field
        Choose “$5.00” in “Shipping Methods” radiobutton
        Click “Next” button
        Click “Place Order” button
        
    Expected results:
        “Thank you for your purchase!“ message is displayed"""


def test_guest_add_item(driver):
    page = CheckoutPage(driver, MainPage.URL)
    page.open()
    page.is_clickable(bpl.SHOP_NEW_YOGA).click()
    page.is_clickable(ipl.LINK_EFCS_SIZE_28).click()
    page.is_clickable(ipl.LINK_EFCS_SIZE_BLACK).click()
    page.is_clickable(ipl.LINK_EFCS_ADD_TO_CART).click()
    page.is_visible(bpl.MSG_SUCCESS)
    page.is_clickable(opl.SHOPPING_CART_BUTTON).click()
    time.sleep(0.3)
    page.is_clickable(opl.PROCEED_TO_CHECKOUT).click()
    page.full_guest_place_order_us_address_flat_shipping("Alabama", "123@gmail.com", "Bob", "Ivanov", "Street 5", "Minsk", "12345",
                                                    "123")
    time.sleep(10)
    assert page.is_visible(cpl.SUCCESS_PLACE_ORDER_MESSAGE).text == 'Thank you for your purchase!'

