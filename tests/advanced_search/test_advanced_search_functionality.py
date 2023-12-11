from pages.advanced_search.advanced_search_form_page import AdvancedSearchFormPage
from data.advanced_search_url import ADVANCED_SEARCH_URL
from data.advanced_search_data import ERROR_MESSAGE_ON_ADVANCED_SEARCH_PAGE, INVALID_PRODUCT_NAME, VALID_PRODUCT_NAME
from data.advanced_search_results_data import (get_advanced_search_results_url,
                                               ERROR_MESSAGE_ON_ADVANCED_SEARCH_RESULTS_PAGE)
from pages.advanced_search.advanced_search_results_page import AdvancedSearchResultsPage


class TestAdvancedSearchFunctionality:

    def test_verify_find_product_upon_fill_out_one_field_with_valid_data(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        page.clear_all_search_fields()
        page.enter_product_name(VALID_PRODUCT_NAME)
        page.click_search()

        page = AdvancedSearchResultsPage(driver, get_advanced_search_results_url(product_name=VALID_PRODUCT_NAME))
        page.open()

        assert len(page.get_list_of_product_names()) > 0

    def test_verify_error_message_appears_if_having_not_typed_in_data(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        page.clear_all_search_fields()
        page.click_search()

        assert page.get_error_message() == ERROR_MESSAGE_ON_ADVANCED_SEARCH_PAGE

    def test_verify_error_message_appears_if_having_typed_in_invalid_data(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        page.clear_all_search_fields()
        page.enter_product_name(INVALID_PRODUCT_NAME)
        page.click_search()

        page = AdvancedSearchResultsPage(driver, get_advanced_search_results_url(product_name=INVALID_PRODUCT_NAME))
        page.open()

        assert page.get_error_message() == ERROR_MESSAGE_ON_ADVANCED_SEARCH_RESULTS_PAGE
