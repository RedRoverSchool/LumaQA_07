import allure
import pytest
from pages.advanced_search.advanced_search_results_page import AdvancedSearchResultsPage
from data.advanced_search_url import ADVANCED_SEARCH_URL, ADVANCED_SEARCH_TOP_URL
from locators.advanced_search_locators import AdvancedSearchLocators as locators
from data.advanced_search_results_data import CLOTHES_LIST
import data.advanced_search_data as data
from pages.advanced_search.advanced_search_form_page import AdvancedSearchFormPage


class TestAdvancedSearchResults:

    def test_verify_product_images_on_single_page(self, driver):
        image_check_list = []
        missing_image_list = []
        advanced_search_page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        advanced_search_page.enter_product_name(data.SAMPLE_SINGLE_PAGE_SEARCH_QUERY)
        advanced_search_page.click_search()

        image_check_result = advanced_search_page.are_all_images_present()
        image_check_list.append(image_check_result['confirm'])
        missing_image_list.extend(image_check_result['missing_images'])

        assert all(image_check_list), list(missing_image_list)

    @allure.title("TC_017.007.002 | Advanced Search Results > Verify that all item cards "
                  "in all the Advanced Search result pages contain product image")
    def test_verify_product_images_on_multipage(self, driver):
        image_check_list = []
        missing_image_list = []
        advanced_search_page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        advanced_search_page.enter_product_name(data.SAMPLE_SINGLE_PAGE_SEARCH_QUERY)
        advanced_search_page.click_search()

        if advanced_search_page.is_multipage():
            is_not_last_page = 1
            while is_not_last_page:
                image_check_result = advanced_search_page.are_all_images_present()
                image_check_list.append(image_check_result['confirm'])
                missing_image_list.extend(image_check_result['missing_images'])

                is_not_last_page = advanced_search_page.is_not_last_page()
                if is_not_last_page:
                    advanced_search_page.click_next_page()
        else:
            image_check_result = advanced_search_page.are_all_images_present()
            image_check_list.append(image_check_result['confirm'])
            missing_image_list.extend(image_check_result['missing_images'])

        assert len(image_check_list) > 0, 'No images found'
        assert all(image_check_list), list(missing_image_list)

