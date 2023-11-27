import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.footer.footer_page import FooterPage


@pytest.fixture(scope="function")
def footer_page(driver):
    footer_page = FooterPage(driver, MainPage.URL)
    footer_page.open()
    return footer_page


class TestFooterPage:
    def test_check_visibility_advanced_search_link(self, driver, footer_page):
        """
        TC_012.012.001 | Footer > Advanced search link > Visibility
        The test verifies if the advanced search link is visible on the footer
        """
        assert footer_page.check_visibility_advanced_search_link(), \
            "Advanced Search link is not visible"

    def test_check_clickability_advanced_search_link(self, driver, footer_page):
        """
        TC_012.012.002 | Footer > Advanced search link > Clickability
        The test verifies if the advanced search link is clickable
        and redirects to the Advanced Search page
        """
        footer_page.click_advanced_search_link()
        assert "advanced" in driver.current_url.lower(), \
            "Advanced Search link is not clickable or doesn't redirect to the Advanced Search page"
