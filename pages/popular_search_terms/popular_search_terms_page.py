from base.seleniumbase import BasePage
from locators.popular_search_terms_page_locators import PopularSearchTermsPageLocators


class PopularSearchTermsPage(BasePage):
    locators = PopularSearchTermsPageLocators()

    def get_heading(self):
        return self.is_visible(self.locators.HEADING)

    def get_keywords_list(self):
        return self.is_visible_all_elements(self.locators.KEYWORDS_LIST)

    def click_on_hoodie_item_keyword_link(self):
        return self.is_clickable(self.locators.HOODIE_ITEM_KEYWORDS_LINK).click()
