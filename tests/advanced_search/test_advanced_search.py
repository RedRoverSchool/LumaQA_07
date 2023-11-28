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

