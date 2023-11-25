from pages.popular_search_terms.popular_search_terms_page import PopularSearchTermsPage
from pages.search_results_page.search_results_page import SearchResultsPage
from data.popular_search_terms_page_data import POPULAR_SEARCH_TERMS_PAGE_URL
from data.search_results_page_data import (HOODIE_ITEM_SEARCH_RESULT_URL, HOODIE_ITEM_SEARCH_RESULT_TITLE,
                                           HOODIE_ITEM_SEARCH_RESULT_HEADING)


class TestRedirectionUponClickOnKeywordLinks:

    def test_verify_redirection_to_the_correct_page(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        page.click_on_hoodie_item_keyword_link()

        assert page.current_url == HOODIE_ITEM_SEARCH_RESULT_URL

    def test_verify_redirection_to_the_page_with_correct_title(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        page.click_on_hoodie_item_keyword_link()

        assert driver.title == HOODIE_ITEM_SEARCH_RESULT_TITLE

    def test_verify_redirection_to_the_page_with_correct_heading(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        page.click_on_hoodie_item_keyword_link()

        page = SearchResultsPage(driver, HOODIE_ITEM_SEARCH_RESULT_URL)

        assert page.get_hoodie_item_heading().text == HOODIE_ITEM_SEARCH_RESULT_HEADING
