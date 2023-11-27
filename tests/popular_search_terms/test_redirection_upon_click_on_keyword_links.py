import urllib.parse

from pages.popular_search_terms.popular_search_terms_page import PopularSearchTermsPage
from pages.search_results_page.search_results_page import SearchResultsPage
from data.popular_search_terms_page_data import POPULAR_SEARCH_TERMS_PAGE_URL
from data.search_results_page_data import SEARCH_RESULT_PAGE_URL_FOR_ANY_ITEM, TEXT_SEARCH_RESULT_FOR


class TestRedirectionUponClickOnKeywordLinks:

    @staticmethod
    def encode_string_to_URL_code(string):
        return urllib.parse.quote_plus(string)

    def test_verify_redirection_to_the_correct_page(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        random_keyword_link = page.get_random_item_keyword_link()
        random_keyword_name = random_keyword_link.text.strip()
        random_keyword_link.click()

        assert (page.current_url == SEARCH_RESULT_PAGE_URL_FOR_ANY_ITEM
                + self.encode_string_to_URL_code(random_keyword_name))

    def test_verify_redirection_to_the_page_with_correct_title(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        random_keyword_link = page.get_random_item_keyword_link()
        random_keyword_name = random_keyword_link.text.strip()
        random_keyword_link.click()

        assert driver.title == f"{TEXT_SEARCH_RESULT_FOR}'{random_keyword_name}'"

    def test_verify_redirection_to_the_page_with_correct_heading(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        random_keyword_link = page.get_random_item_keyword_link()
        random_keyword_name = random_keyword_link.text.strip()
        random_keyword_link.click()

        page = SearchResultsPage(driver, SEARCH_RESULT_PAGE_URL_FOR_ANY_ITEM
                                 + self.encode_string_to_URL_code(random_keyword_name))
        page.open()

        assert page.get_item_heading().text == f"{TEXT_SEARCH_RESULT_FOR}'{random_keyword_name}'"
