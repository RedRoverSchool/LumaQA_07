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

    @allure.title("TC_012.013.001 | Footer > 'Advanced Search' link > Redirection > "
                  "Verify the opened page URL upon clicking on the appropriate link")
    def test_verify_url_upon_redirection(self, driver):
        page = FooterPage(driver, MainPage.URL)
        page.open()
        page.click_advanced_search_link()

        assert "advanced" in page.current_url, "Current page URL is different"

    @allure.title("TC_012.013.002 | Footer > 'Advanced Search' link > Redirection > "
                  "Verify the opened page title upon clicking on the appropriate link")
    def test_verify_title_upon_redirection(self, driver):
        page = FooterPage(driver, MainPage.URL)
        page.open()
        page.click_advanced_search_link()

        assert page.get_page_title() == "Advanced Search", "Current page title is different"

    @allure.title("TC_012.010.001 | Footer > Self > Set of links > Verify first footer block contains 4 links")
    def test_first_footer_block_contains_four_links(self, driver):
        page = FooterPage(driver, MainPage.URL)
        page.open()
        page.have_first_footer_block_links_href()

        assert page.get_first_footer_links_block_length() == 4, "The 1st links block size is not 4"

    @allure.title("TC_012.010.002 | Footer > Self > Set of links > Verify second footer block contains 4 links")
    def test_second_footer_block_contains_four_links(self, driver):
        page = FooterPage(driver, MainPage.URL)
        page.open()
        page.have_second_footer_block_links_href()

        assert page.get_second_footer_links_block_length() == 4, "The 2nd links block size is not 4"
