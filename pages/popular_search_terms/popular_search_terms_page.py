from base.seleniumbase import BasePage
from locators.popular_search_terms_page_locators import PopularSearchTermsPageLocators


class PopularSearchTermsPage(BasePage):
    locators = PopularSearchTermsPageLocators()

    def get_heading(self):
        return self.is_visible(self.locators.HEADING)


