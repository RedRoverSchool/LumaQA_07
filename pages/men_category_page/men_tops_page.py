from base.seleniumbase import BasePage
from locators.men_page_locators import MenPageLocators
from locators.men_tops_page_locators import MenTopsPageLocators


class MenTops(BasePage):
    def check_clickability_grid(self):
        return self.is_clickable(MenPageLocators.MEN_TOPS_GRID)

    def click_men_tops_product_foto(self):
        return self.is_clickable(MenTopsPageLocators.TOP_MEN_PRODUCT_FOTO).click()

    def click_men_tops_product_title(self):
        return self.is_clickable(MenTopsPageLocators.TOP_MEN_PRODUCT_TITLE).click()