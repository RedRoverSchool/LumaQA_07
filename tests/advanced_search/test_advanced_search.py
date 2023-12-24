import allure
import pytest
from pages.advanced_search.advanced_search_results_page import AdvancedSearchResultsPage
from data.advanced_search_url import ADVANCED_SEARCH_URL, ADVANCED_SEARCH_TOP_URL
from locators.advanced_search_locators import AdvancedSearchLocators as locators
from data.advanced_search_results_data import CLOTHES_LIST
from data.advanced_search_data import SAMPLE_SEARCH_QUERY
from pages.advanced_search.advanced_search_form_page import AdvancedSearchFormPage



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

    @allure.title("TC_016.004.003 | Verify the background color of the 'Search' button is #1979c3 ")
    def test_search_button_background_color(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        assert page.get_search_button_hex_background_color() == "#1979c3", \
            "Search button hex background color is not #1979c3"

    def test_modify_your_search(self, driver):
        advanced_search_page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        advanced_search_page.open()
        advanced_search_page.enter_product_name('top')
        advanced_search_page.click_search()
        assert advanced_search_page.is_visible(locators.MODIFY_YOUR_SEARCH), 'modify your search is not visible'
        assert advanced_search_page.clickable(locators.MODIFY_YOUR_SEARCH), 'modify your search is not clickable'

    @pytest.mark.parametrize('query', CLOTHES_LIST)
    def test_enable_size_buttons(self, driver, query):
        page = AdvancedSearchResultsPage(driver, ADVANCED_SEARCH_URL)
        page.open()
        page.enter_product_name(query)
        page.click_search()
        assert page.size_buttons_clickable(), 'size options are not clickable'

    def test_modify_your_search_redirection_advanced_search_form(self, driver):
        advanced_search_page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        advanced_search_page.open()
        advanced_search_page.enter_product_name(SAMPLE_SEARCH_QUERY)
        advanced_search_page.click_search()
        advanced_search_page.is_visible(locators.MODIFY_YOUR_SEARCH)
        advanced_search_page.clickable(locators.MODIFY_YOUR_SEARCH).click()
        assert driver.current_url == ADVANCED_SEARCH_TOP_URL

    def test_verify_product_images_on_page(self, driver):
        image_check_list = []
        missing_image_list = []
        advanced_search_page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        advanced_search_page.open()
        advanced_search_page.enter_product_name(SAMPLE_SEARCH_QUERY)
        advanced_search_page.click_search()
        image_elements = driver.find_elements(*locators.PRODUCT_ITEM_IMAGES)

        for image in image_elements:
            image_check_list.append(advanced_search_page.is_image_displayed(image))
            if not advanced_search_page.is_image_displayed(image):
                missing_image_list.append(image.get_attribute(('src')))

        assert all(image_check_list), list(missing_image_list)

    @allure.title("TC_016.002.002 | Advanced Search > Fields visibility > Verify 6 search fields: "
                  "Product Name, SKU, Description, Short Description, min Price and max Price, are visible")
    def test_six_search_fields_are_visible(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        assert page.are_six_search_fields_visible(), "6 search fields are not visible"
