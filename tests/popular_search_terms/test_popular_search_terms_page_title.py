import pytest
from data.test_urls_list import TEST_URL_LIST
from locators.base_page_locators import BasePageLocators
from data.popular_search_terms_page_data import HEADING_TEXT
from locators.popular_search_terms_page_locators import POPULAR_SEARCH_TERMS_PAGE_TITLE_LOCATOR

@pytest.mark.long
@pytest.mark.parametrize("any_url", TEST_URL_LIST)
def test_title_of_the_popular_search_terms_page(driver, any_url, any_page_precondition):
    """TC_012.004.002 | Footer > "Search terms" link >
     Redirection > Verify the 'Popular Search Terms' page contains the title 'Popular Search Terms'"""

    search_terms_link = any_page_precondition.is_visible(BasePageLocators.LINK_SEARCH_TERMS)
    search_terms_link.click()
    page_title = any_page_precondition.is_visible(POPULAR_SEARCH_TERMS_PAGE_TITLE_LOCATOR)
    assert page_title.text == HEADING_TEXT

