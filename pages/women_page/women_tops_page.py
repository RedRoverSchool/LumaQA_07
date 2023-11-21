from base.seleniumbase import BasePage
from locators.women_top_page_locators import WomenTopsPageLocators
from locators.product_page_locators import ProductPageLocators


class WomenTopPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def get_products(self):
        product_elements = self.driver.find_elements(*WomenTopsPageLocators.TOP_WOMEN_PRODUCTS)
        return product_elements

    def click_first_product(self):
        product_elements = self.get_products()
        if product_elements:
            clickable_element = product_elements[0]
            clickable_element.click()

    def related(self):
        related_heading_element = self.driver.find_element(*ProductPageLocators.RELATED_PRODUCTS_HEADING)
        return related_heading_element.text


