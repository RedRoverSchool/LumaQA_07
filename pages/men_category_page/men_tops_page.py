from base.seleniumbase import BasePage
from locators.men_page_locators import MenPageLocators


class MenTops(BasePage):
    def check_clickability_grid(self):
        return self.is_clickable(MenPageLocators.MEN_TOPS_GRID)
