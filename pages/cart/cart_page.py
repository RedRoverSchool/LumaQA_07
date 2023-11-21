from base.seleniumbase import BasePage
from locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/checkout/cart/"

    def checkout_multiple_addresses_link(self):
        self.is_visible(CartPageLocators.GRAND_TOTAL)
        return self.is_clickable(CartPageLocators.MULTI_ADDRESS_CHECKOUT_LINK)

    def proceed_to_checkout_button(self):
        return self.is_clickable(CartPageLocators.PROCEED_TO_CHECKOUT_BUTTON)




