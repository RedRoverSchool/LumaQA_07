from base.seleniumbase import BasePage
from locators.advanced_search_results_locators import AdvancedSearchResultsLocators as locator


class AdvancedSearchResultsPage(BasePage):

    def get_error_message(self):
        return f'{self.is_visible(locator.ERROR_MESSAGE_ON_ADVANCED_SEARCH_RESULTS_PAGE).text.strip().split(". ")[0]}.'

    def get_list_of_product_names(self):
        return [name.text for name in self.is_visible_all_elements(locator.PRODUCT_CARD_NAMES)]

    def get_message_how_many_items_found(self):
        return self.is_visible(locator.MESSAGE_HOW_MANY_ITEMS_FOUND).text.strip()

    def get_message_number_of_items(self):
        return self.is_visible(locator.MESSAGE_NUMBER_OF_ITEMS).text.strip()
