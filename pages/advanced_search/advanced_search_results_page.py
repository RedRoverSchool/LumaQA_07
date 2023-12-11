from base.seleniumbase import BasePage
from locators.advanced_search_results_locators import AdvancedSearchResultsLocators as locator


class AdvancedSearchResultsPage(BasePage):

    def get_error_message(self):
        return f'{self.is_visible(locator.ERROR_MESSAGE_ON_ADVANCED_SEARCH_RESULTS_PAGE).text.strip().split(". ")[0]}.'
