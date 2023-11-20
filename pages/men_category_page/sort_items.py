from selenium.webdriver.support.select import Select

from base.seleniumbase import BasePage
from locators.sort_items_locators import SortItemsLocators


class SortItemsByProduct(BasePage):

    def sort_select(self):
        return Select(self.is_clickable(SortItemsLocators.SORT_SELECT))

    def sort_direction(self):
        return self.is_visible(SortItemsLocators.DIRECTION_SWITCHER)

    def paging_button_next(self):
        return self.is_clickable(SortItemsLocators.PAGING_BUTTON_NEXT)

    def paging_button_next_visible(self):
        return bool(self.item_count(SortItemsLocators.PAGING_BUTTON_NEXT))

    def name_items(self):
        return self.is_visible_all_elements(SortItemsLocators.NAME_ITEMS)


