from base.seleniumbase import BasePage
from locators.search_results_page_locators import SearchResultsPageLocators


class SearchResultsPage(BasePage):
    locators = SearchResultsPageLocators()

    def get_item_heading(self):
        return self.is_visible(self.locators.ITEM_HEADING)
