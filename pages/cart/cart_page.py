from base.seleniumbase import BasePage
from locators.cart_page_locators import CartPageLocators
from locators.checkout_page_locators import CheckoutPageLocators


class CartPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/checkout/cart/"

    def checkout_multiple_addresses_link(self):
        self.is_visible(CartPageLocators.GRAND_TOTAL)
        return self.is_clickable(CartPageLocators.MULTI_ADDRESS_CHECKOUT_LINK)

    def wait_shipping_addresses_overlay_closed(self):
        self.is_invisible(CheckoutPageLocators.SHIPPING_ADDRESSES_OVERLAY)

    def wait_shipping_methods_overlay_closed(self):
        self.is_invisible(CheckoutPageLocators.SHIPPING_METHODS_OVERLAY)

    def click_proceed_to_checkout_button(self):
        self.is_visible(CartPageLocators.GRAND_TOTAL)
        self.is_clickable(CartPageLocators.PROCEED_TO_CHECKOUT_BUTTON).click()
        self.wait_shipping_addresses_overlay_closed()
        self.wait_shipping_methods_overlay_closed()

    def button_edit_item(self):
        return self.is_clickable(CartPageLocators.BUTTON_EDIT_ITEM)

    def item_options(self):
        return self.is_visible(CartPageLocators.ITEM_OPTIONS)


class UpdateItem(BasePage):

    def size_29(self):
        return self.is_clickable(CartPageLocators.SIZE_UPDATE_29)

    def color_blue(self):
        return self.is_clickable(CartPageLocators.COLOR_BLUE)

    def update_cart(self):
        return self.is_clickable(CartPageLocators.BUTTON_UPDATE_CART)


class AddItemToCart(BasePage):
    def add_to_cart(self):
        return self.is_clickable(CartPageLocators.BUTTON_ADD_TO_CART)

    def color_grey_item(self):
        return self.is_clickable(CartPageLocators.COLOR_GREY)

    def size_28(self):
        return self.is_clickable(CartPageLocators.SIZE_28)





