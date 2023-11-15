from pages.popular_search_terms.popular_search_terms_page import PopularSearchTermsPage
from data.popular_search_terms_page_data import POPULAR_SEARCH_TERMS_PAGE_URL, HEADING_TEXT


class TestContentPopularSearchTermsPage:

    def test_verify_heading_on_popular_search_terms_page(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        assert driver.current_url == POPULAR_SEARCH_TERMS_PAGE_URL
        assert page.get_heading().text == HEADING_TEXT, 'Heading is invisible'





