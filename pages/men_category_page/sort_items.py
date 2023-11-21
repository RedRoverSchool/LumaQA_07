from selenium.webdriver.support.select import Select

from base.seleniumbase import BasePage
from locators.sort_items_locators import SortItemsLocators, ShowItemsPerPageLocators


class SortItemsByProduct(BasePage):

    URL_SORTED_BY_NAME = "https://magento.softwaretestingboard.com/men/tops-men.html?product_list_order=name"

    def sort_select(self):
        return Select(self.is_clickable(SortItemsLocators.SORT_SELECT))

    def sort_direction(self):
        return self.is_clickable(SortItemsLocators.DIRECTION_SWITCHER)

    def paging_button_next(self):
        return self.is_clickable(SortItemsLocators.PAGING_BUTTON_NEXT)

    def paging_button_next_visible(self):
        return bool(self.item_count(SortItemsLocators.PAGING_BUTTON_NEXT))

    def name_items(self):
        return self.is_visible_all_elements(SortItemsLocators.NAME_ITEMS)

    def price_items(self):
        return self.is_visible_all_elements(SortItemsLocators.PRICE_ITEMS)

    def paging_one_page(self):
        return self.is_clickable(SortItemsLocators.PAGING_ONE_PAGE)


class ShowItemsPerPage(BasePage):

    def modes_grid_active(self):
        return self.is_visible(ShowItemsPerPageLocators.MODES_GRID_ACTIVE)

    def modes_list(self):
        return self.is_clickable(ShowItemsPerPageLocators.MODES_LIST)

    def modes_list_active(self):
        return self.is_visible(ShowItemsPerPageLocators.MODES_LIST_ACTIVE)

    def select_show_items(self):
        return Select(self.is_clickable(ShowItemsPerPageLocators.SELECT_SHOW_ITEMS_QTY))

    def name_items(self):
        return self.is_visible_all_elements(SortItemsLocators.NAME_ITEMS)





