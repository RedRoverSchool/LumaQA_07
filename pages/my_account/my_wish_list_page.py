from base.seleniumbase import BasePage
from locators.wish_list_locators import WishListLocators


class MyWishListPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/wishlist/"

    def all_to_cart(self):
        return self.is_clickable(WishListLocators.BUTTON_ALL_TO_CART)

