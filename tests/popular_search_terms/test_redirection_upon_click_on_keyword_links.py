from pages.popular_search_terms.popular_search_terms_page import PopularSearchTermsPage
from data.popular_search_terms_page_data import POPULAR_SEARCH_TERMS_PAGE_URL
from data.search_results_page_data import HOODIE_ITEM_SEARCH_RESULT_URL


class TestRedirectionUponClickOnKeywordLinks:

    def test_verify_redirection_to_the_correct_page(self,driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        page.click_on_hoodie_item_keyword_link()

        assert page.current_url == HOODIE_ITEM_SEARCH_RESULT_URL
