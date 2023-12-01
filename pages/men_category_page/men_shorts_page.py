from base.seleniumbase import BasePage
from locators.men_page_locators import MenShortsPageLocators


class MenShortsPage(BasePage):
    locator = MenShortsPageLocators()

    def check_visibility_of_elements(self):
        return self.is_visible_all_elements(MenShortsPageLocators.ITEM_PRODUCT)

    def check_title(self, title):
        return self.is_visible(MenShortsPageLocators.get_position_title(title)).text

    def click_any_product(self, product):
        return self.is_visible(MenShortsPageLocators.get_position_title(product)).click()

    def check_title_on_new_page(self, title):
        return self.is_visible(MenShortsPageLocators.get_title_on_new_page(title)).text
