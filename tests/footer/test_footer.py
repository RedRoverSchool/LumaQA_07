import pytest
import allure

from pages.main_page import MainPage
from pages.footer.footer_page import FooterPage
from data.footer_data import FOOTER_LINKS_TEXTS


@pytest.fixture(scope="function")
def footer_page(driver):
    footer_page = FooterPage(driver, MainPage.URL)
    footer_page.open()
    return footer_page


class TestFooterPage:
    @allure.title('TC_012.012.001 | Footer > Advanced search link > Visibility')
    def test_check_visibility_advanced_search_link(self, driver, footer_page):
        """
        The test verifies if the advanced search link is visible on the footer
        """
        assert footer_page.check_visibility_advanced_search_link(), \
            "Advanced Search link is not visible"

    @allure.title('TC_012.012.002 | Footer > Advanced search link > Clickability')
    def test_check_clickability_advanced_search_link(self, driver, footer_page):
        """
        The test verifies if the advanced search link is clickable
        and redirects to the Advanced Search page
        """
        footer_page.click_advanced_search_link()
        assert "advanced" in driver.current_url.lower(), \
            "Advanced Search link is not clickable or doesn't redirect to the Advanced Search page"

    @allure.title('TC_012.012.003 | Footer > Advanced search link > Non-Clickability on Advanced Search Page')
    def test_check_advanced_search_link_disabled_on_advanced_search_page(self, driver, footer_page):
        """
        The test verifies if the advanced search link, after clicking on it, is not clickable on Advanced Search page
        e.g. doesn't have href attribute but is wrapped in a <strong> tag instead
        """
        footer_page.click_advanced_search_link()
        strong_element = footer_page.check_visibility_footer_diabled_link()
        assert strong_element.text == FOOTER_LINKS_TEXTS["ADVANCED_SEARCH"] \
               and strong_element.get_attribute('href') is None, \
            "Advanced Search link is clickable: its url is still present"
