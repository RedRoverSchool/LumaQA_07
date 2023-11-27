import random

from base.seleniumbase import BasePage
from locators.popular_search_terms_page_locators import PopularSearchTermsPageLocators


class PopularSearchTermsPage(BasePage):
    locators = PopularSearchTermsPageLocators()

    def get_heading(self):
        return self.is_visible(self.locators.HEADING)

    def get_keywords_list(self):
        return self.is_visible_all_elements(self.locators.KEYWORDS_LIST)

    def get_random_item_keyword_link(self):
        return random.choice(self.get_keywords_list())
