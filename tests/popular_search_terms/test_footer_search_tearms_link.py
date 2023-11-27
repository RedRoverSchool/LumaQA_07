from base.seleniumbase import BasePage
from data.popular_search_terms_page_data import POPULAR_SEARCH_TERMS_PAGE_URL
from locators.popular_search_terms_page_locators import PopularSearchTermsPageFooterLocators
def test_search_terms_link_is_not_clickable(driver):
    """TC_012.003.003 | Footer > "Search terms" link > Visibility and clickability >
     Verify The 'Search Terms' link is not clickable on the 'Popular Search Terms' page"""
    page = BasePage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
    page.open()
    assert not page.is_clickable(PopularSearchTermsPageFooterLocators.FOOTER_SEARCH_TERMS_LINK), "The 'Search Terms' link is clickable when it should not be"

