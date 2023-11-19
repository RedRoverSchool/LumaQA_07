from pages.women_page.women_page import WomenPage
from locators.women_page_locators import WomenPageLocators
from locators.women_top_page_locators import WomenTopsPageLocators
from pages.women_page.women_tops_page import WomenTopPage


class TestWomenPage:
    def test_click_tops_link(self, driver):
        women_page = WomenPage(driver, "https://magento.softwaretestingboard.com/women.html")
        women_page.open()
        element = women_page.is_visible(WomenPageLocators.PAGE_NAME)
        assert element.is_displayed(), 'Page name is not visible'

    def test_click_tops_link(self, driver):
        women_page = WomenPage(driver, "https://magento.softwaretestingboard.com/women.html")
        women_page.open()
        women_page.click_tops_link()
        women_top_page = WomenTopPage(driver, "https://magento.softwaretestingboard.com/women/tops-women.html")
        women_top_page_element = women_top_page.is_visible(WomenTopsPageLocators.PAGE_NAME)
        expected_text = "Tops"
        actual_text = women_top_page_element.text

        assert expected_text in actual_text, f"Expected page name to include '{expected_text}', but found '{actual_text}'"


class TestWomenTopsPage:
    def test_click_first_product(self, driver):
        women_page = WomenPage(driver, "https://magento.softwaretestingboard.com/women.html")
        women_page.open()
        women_page.click_tops_link()
        women_top_page = WomenTopPage(driver, "https://magento.softwaretestingboard.com/women/tops-women.html")
        women_top_page.click_first_product()
        related_products_text = women_top_page.related()

        assert related_products_text == "Related Products", f"Expected text 'Related Products', but found '{related_products_text}'"


