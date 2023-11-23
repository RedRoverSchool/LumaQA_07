from pages.popular_search_terms.popular_search_terms_page import PopularSearchTermsPage
from data.popular_search_terms_page_data import POPULAR_SEARCH_TERMS_PAGE_URL


class TestVisibilityAndClickabilityOfLinksWithKeywords:

    def test_links_with_keywords_are_visible(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        for keyword_link in page.get_keywords_list():
            assert keyword_link.is_displayed()

    def test_links_with_keywords_are_clickable(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        for keyword_link in page.get_keywords_list():
            assert keyword_link.is_enabled()
