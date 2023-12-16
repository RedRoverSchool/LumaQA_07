import pytest
from pages.advanced_search.advanced_search_form_page import AdvancedSearchFormPage
from data.advanced_search_url import ADVANCED_SEARCH_URL
from locators.advanced_search_locators import AdvancedSearchLocators as locators


class TestAdvancedSearch:

    @pytest.mark.parametrize('query', AdvancedSearchFormPage.QUERY_LIST)
    def test_advanced_search_results(self, driver, query):
        advanced_search_page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        advanced_search_page.open()
        advanced_search_page.enter_product_name(query)
        advanced_search_page.click_search()
        current_page_url = driver.current_url
        assert current_page_url != ADVANCED_SEARCH_URL
        try:
            title_list = advanced_search_page.get_list_of_item_titles()
            checklist = []
            for title in title_list:
                checklist.append(query in title.lower())
            for title in title_list:
                assert query in title.lower()
            assert all(checklist)
        except:
            error_message = advanced_search_page.the_presence_of_element_located(locators.ERROR_MESSAGE, 1)
            assert error_message.is_displayed(), 'No error message displayed'

    def test_verify_search_button_is_clickable(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()
        assert page.button_clickable(), 'The button is not clickable'


    def test_verify_search_button_is_visible(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()
        assert page.button_visible(), 'The button is not visible'

    @pytest.mark.parametrize('query', AdvancedSearchFormPage.CLOTHES_LIST)
    def test_verify_clothes_items_have_size_and_color_options(self, driver, query):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()
        page.enter_product_name(query)
        page.click_search()
        try:
            assert page.visibility_of_size_options(), 'The size options are not visible'
            assert page.visibility_of_color_options(), 'The color options are not visible'
        except:
            error_message = page.the_presence_of_element_located(locators.ERROR_MESSAGE, 1)
            assert error_message.is_displayed(), 'No error message displayed'
