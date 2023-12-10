from pages.advanced_search.advanced_search_form_page import AdvancedSearchFormPage
from data.advanced_search_url import ADVANCED_SEARCH_URL
from data.advanced_search_data import ERROR_MESSAGE_ON_ADVANCED_SEARCH_PAGE


class TestAdvancedSearchFunctionality:

    def test_verify_find_product_upon_fill_out_one_field_with_valid_data(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        page.enter_product_name(page.QUERY_LIST[0])
        page.click_search()

        assert len(page.get_list_of_item_titles()) > 0

    def test_verify_error_message_appears_if_having_not_typed_in_data(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        page.clear_all_search_fields()
        page.click_search()

        assert page.get_error_massage_text() == ERROR_MESSAGE_ON_ADVANCED_SEARCH_PAGE
