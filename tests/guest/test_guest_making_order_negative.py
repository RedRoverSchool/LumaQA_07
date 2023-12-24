import time
from pages.main_page import MainPage
from locators.base_page_locators import BasePageLocators as bpl
from locators.item_page_locators import ItemPageLocators as ipl
from locators.order_and_payment_locators import OrdersAndPaymentPageLocators as opl
from pages.checkout_page import CheckoutPage
from locators.checkout_page_locators import CheckoutPageLocators as cpl


""" TC_004.001.005 | Authorization >Anonym user > Making order and payment > Negative:
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
    Type 123 in “Email Address” field
    Type “ ” in “First Name” field
    Type “ ” in “Last Name” field
    Type “ ” in “Street Address” field
    Type “ ” in “City” field
    Type “ ” in “Zip/Postal Code” field
    Type “ ” in “Phone number” field
    Click “Next” button
    
    Expected results:
        Shopping Cart page is opened
        “Please enter a valid email address (Ex: johndoe@domain.com).“ alert under “Email Address” field is displayed
        “This is a required field.“ alert under “First Name” field is displayed
        “This is a required field.“ alert under “Last Name” field is displayed
        “This is a required field.“ alert under “Street Address” field is displayed
        “This is a required field.“ alert under “City” field is displayed
        “This is a required field.“ alert under “Zip/Postal Code” field is displayed
        “This is a required field.“ alert under “Phone Number” field is displayed
        “The shipping method is missing. Select the shipping method and try again.“ alert under “Shipping Methods” radiobuttonis displayed"""


def test_guest_add_item(driver):
    page = CheckoutPage(driver, MainPage.URL)
    page.open()
    page.is_clickable(bpl.SHOP_NEW_YOGA).click()
    page.is_clickable(ipl.LINK_EFCS_SIZE_28).click()
    page.is_clickable(ipl.LINK_EFCS_SIZE_BLACK).click()
    add_to_cart_button = page.is_clickable(ipl.LINK_EFCS_ADD_TO_CART)
    page.move_to_element_and_click(add_to_cart_button)
    page.is_visible(bpl.MSG_SUCCESS)
    page.is_clickable(opl.SHOPPING_CART_BUTTON).click()
    time.sleep(0.3)
    page.is_clickable(opl.PROCEED_TO_CHECKOUT).click()
    page.fill_invalid_data_as_guest_us_shipping()
    page.is_clickable(cpl.CHECKOUT_STEP_2_NEXT_BUTTON).click()
    assert page.is_visible(cpl.EMAIL_FIELD_ERROR).text == 'Please enter a valid email address (Ex: johndoe@domain.com).'
    assert page.is_visible(cpl.FIRST_NAME_FIELD_ERROR).text == 'This is a required field.'
    assert page.is_visible(cpl.LAST_NAME_FIELD_ERROR).text == 'This is a required field.'
    assert page.is_visible(cpl.STREET_1_FIELD_ERROR).text == 'This is a required field.'
    assert page.is_visible(cpl.CITY_FIELD_ERROR).text == 'This is a required field.'
    assert page.is_visible(cpl.POSTCODE_FIELD_ERROR).text == 'This is a required field.'
    assert page.is_visible(cpl.POSTCODE_FIELD_ALERT).text == 'Provided Zip/Postal Code seems to be invalid. Example: 12345-6789; 12345. If you believe it is the right one you can ignore this notice.'
    assert page.is_visible(cpl.PHONE_NUMBER_FIELD_ERROR).text == 'This is a required field.'
    assert page.is_visible(cpl.SHIPPING_METHOD_ALERT).text == 'The shipping method is missing. Select the shipping method and try again.'

