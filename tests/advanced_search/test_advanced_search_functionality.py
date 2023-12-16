import re

from pages.advanced_search.advanced_search_form_page import AdvancedSearchFormPage
from data.advanced_search_url import ADVANCED_SEARCH_URL
from data.advanced_search_data import *
from data.advanced_search_results_data import *
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

    def test_verify_title_of_the_page_after_clicking_on_search_button(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        page.clear_all_search_fields()
        page.enter_product_name(VALID_PRODUCT_NAME)
        page.click_search()

        page = AdvancedSearchResultsPage(driver, get_advanced_search_results_url(product_name=VALID_PRODUCT_NAME))
        page.open()

        assert driver.title == PAGE_TITLE

    def test_verify_title_of_the_page_after_pressing_on_enter_key(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        page.clear_all_search_fields()
        page.enter_product_name(VALID_PRODUCT_NAME)
        page.press_enter_key()

        page = AdvancedSearchResultsPage(driver, get_advanced_search_results_url(product_name=VALID_PRODUCT_NAME))
        page.open()

        assert driver.title == PAGE_TITLE

    def test_verify_data_search_results_match_to_entered_valid_data(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        page.clear_all_search_fields()
        page.enter_product_name(VALID_PRODUCT_NAME)
        page.click_search()

        page = AdvancedSearchResultsPage(driver, get_advanced_search_results_url(product_name=VALID_PRODUCT_NAME))
        page.open()

        numbers_of_items = len(page.get_list_of_product_names())

        assert (page.get_message_how_many_items_found() ==
                str(numbers_of_items) + message_items_were_found(numbers_of_items))
        assert (page.get_message_number_of_items() == str(numbers_of_items) + message_number_of_items(numbers_of_items))
        assert [(VALID_PRODUCT_NAME in item) for item in page.get_list_of_product_names()]

    def test_verify_search_fields_become_highlighted_upon_clicking_on_it(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        for field in page.get_search_fields_list():
            field.click()
            field_shadow_style = field.value_of_css_property('box-shadow')
            rgb_color_list = re.findall(r'([^()]+)\)', field_shadow_style)[0].split(', ')
            rgb_color_tuple = tuple(int(x) for x in rgb_color_list)

            assert page.convert_color_rgb_to_hex(rgb_color_tuple) == FIELD_HIGHLIGHT_COLOR_HEX
