from base.seleniumbase import BasePage
from locators.product_page_locators import ProductPageLocators

class ProductPage(BasePage):
    locators = ProductPageLocators

    def check_product_name_in_main_info(self):
        text = self.visible(self.locators.PRODUCT_NAME)
        return text.text
