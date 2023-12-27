import allure
from pages.advanced_search.advanced_search_form_page import AdvancedSearchFormPage
from pages.advanced_search.advanced_search_results_page import AdvancedSearchResultsPage
from data.advanced_search_url import ADVANCED_SEARCH_URL
from data.advanced_search_results_data import get_advanced_search_results_url
from data.advanced_search_data import MAX_PRICE


class TestAdvancedSearchResultsPage:
    @allure.title("TC_017.004.001 | Advanced Search Results > "
                  "Verify the User sees 24 items on the page upon selecting 'Show 24 per page' dropdown option")
    def test_24_items_on_page(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()
        page.enter_max_price(MAX_PRICE)
        page.click_search()

        page = AdvancedSearchResultsPage(driver, get_advanced_search_results_url(price_to=MAX_PRICE))
        page.open()
        page.select_items_quantity_per_page_is_24()

        assert page.get_items_on_the_page_quantity() == 24, "Items quantity is not equal to 24"
