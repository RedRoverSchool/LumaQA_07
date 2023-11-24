import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.footer.footer_page import FooterPage


@pytest.fixture(scope="function")
def footer_page(driver):
    footer_page = FooterPage(driver, FooterPage.URL)
    footer_page.open()
    return footer_page


class TestFooterPage:
    def test_check_visibility_advanced_search_link(self, driver, footer_page):
        """Check Advanced Search link is visible """
        assert footer_page.check_visibility_advanced_search_link(), \
            "Advanced Search link is not visible"
