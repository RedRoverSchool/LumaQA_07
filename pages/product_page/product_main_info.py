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

    def availability_block_is_displayed(self):
        availability_block = self.is_visible(self.locators.AVAILABILITY_BLOCK)
        return availability_block.is_displayed()

    def choose_size(self):
        size = self.is_clickable(self.locators.PRODUCT_SIZE)
        return size.click()

    def choose_color(self):
        color = self.is_clickable(self.locators.PRODUCT_COLOR)
        return color.click()

    def click_add_to_cart(self):
        click_add_to_cart = self.is_clickable(self.locators.BUTTON_ADD_TO_CART)
        return click_add_to_cart.click()

    def counter_number_is_visible(self):
        counter_number_is_visible = self.is_visible(self.locators.COUNTER_NUMBER)
        return counter_number_is_visible.is_displayed()