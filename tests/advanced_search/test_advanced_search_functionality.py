from pages.advanced_search.advanced_search_form_page import AdvancedSearchFormPage
from data.advanced_search_url import ADVANCED_SEARCH_URL


class TestAdvancedSearchFunctionality:

    def test_verify_find_product_upon_fill_out_one_field_with_valid_data(self, driver):
        page = AdvancedSearchFormPage(driver, ADVANCED_SEARCH_URL)
        page.open()

        page.enter_product_name(page.QUERY_LIST[0])
        page.click_search()

        assert len(page.get_list_of_item_titles()) > 0
