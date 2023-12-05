from selenium.webdriver.support.select import Select

from base.seleniumbase import BasePage
from locators.wish_list_locators import WishListLocators


class MyWishListPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/wishlist/"

    def all_to_cart(self):
        return self.is_clickable(WishListLocators.BUTTON_ALL_TO_CART)

    def pagination(self):
        return self.is_visible(WishListLocators.PAGINATION)

    def select_show_items_limiter(self):
        return Select(self.is_clickable(WishListLocators.SELECT_SHOW_ITEMS_QTY))


