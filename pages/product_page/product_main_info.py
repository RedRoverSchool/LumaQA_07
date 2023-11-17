from base.seleniumbase import BasePage
from locators.product_page_locators import ProductPageLocators

class ProductPage(BasePage):
    locators = ProductPageLocators

    def check_product_name_in_main_info(self):
        text = self.is_visible(self.locators.PRODUCT_NAME)
        return text.text

    def rating_block_is_visible(self):
        rating_block = self.is_visible(self.locators.RATING_BLOCK)
        return rating_block.is_displayed()

    def price_block_is_visible(self):
        price_block = self.is_visible(self.locators.PRICE_BLOCK)
        return price_block.is_displayed()