import random
from base.seleniumbase import BasePage
from locators.sale_page_locators import SalePageLocators, ItemsLocators


class SalePage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/sale.html'

    def check_visibility_of_Shop_Womens_Deals(self):
        return self.is_visible(SalePageLocators.SHOP_WOMENS_DEALS)

    def check_clickability_of_Shop_Womens_Deals(self):
        return self.is_clickable(SalePageLocators.SHOP_WOMENS_DEALS)

    def check_visibility_of_Shop_Mens_Deals(self):
        return self.is_visible(SalePageLocators.SHOP_MENS_DEALS)

    def check_clickability_of_Shop_Mens_Deals(self):
        return self.is_clickable(SalePageLocators.SHOP_MENS_DEALS)

    def check_visibility_of_Shop_Luma_Gear(self):
        return self.is_visible(SalePageLocators.SHOP_LUMA_GEAR)

    def check_clickability_of_Shop_Luma_Gear(self):
        return self.is_clickable(SalePageLocators.SHOP_LUMA_GEAR)

    def check_visibility_of_Tees_on_sale(self):
        return self.is_visible(SalePageLocators.TEES_ON_SALE)

    def check_clickability_of_Tees_on_sale(self):
        return self.is_clickable(SalePageLocators.TEES_ON_SALE)


class TeesPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/women/tops-women/tees-women.html'

    def check_visibility_products_list(self):
        return self.is_visible(SalePageLocators.PRODUCTS_LIST)

    def check_clickability_products_list(self):
        return self.is_clickable(SalePageLocators.PRODUCTS_LIST)

    def check_visibility_add_to_card(self):
        return self.is_visible(SalePageLocators.ADD_TO_CARD)

    def check_clickability_add_to_card(self):
        return self.is_clickable(SalePageLocators.ADD_TO_CARD)

    # todo 3 pass functions
    def check_visibility_cart_prodact(self):
        pass

    def check_visibility_PRODUCTS_LIST(self):
        pass

    def check_clickability_PRODUCTS_LIST(self):
        pass


class ItemsPage(BasePage):
    locators = ItemsLocators()

    def click_random_item(self):
        item_list = self.is_visible_all_elements(self.locators.ITEMS_LIST)
        item = item_list[random.randint(1, 11)]
        # todo random item click
        # self.go_to_element(item)
        item.click()


class TeesPageProdact(BasePage):
    URL = 'https://magento.softwaretestingboard.com/tiffany-fitness-tee.html'

    def check_visibility_basket(self):
        return self.is_visible(SalePageLocators.BASKET)

    def check_clickability_basket(self):
        return self.is_clickable(SalePageLocators.BASKET)

    def check_visibility_proceed_to_checkout(self):
        return self.is_visible(SalePageLocators.PROCEED_TO_CHECKOUT)

    def check_clickability_proceed_to_checkout(self):
        return self.is_clickable(SalePageLocators.PROCEED_TO_CHECKOUT)
