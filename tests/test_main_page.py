from pages.main_page import MainPage
from locators.base_page_locators import BasePageLocators
from pages.erin_recommends.erin_recommends import ErinRecommendsPage
from data.men_page_url import MEN_PAGE
from pages.performance_fabrics.performance_fabrics import PerformanceFabricsPage


class TestMainPage:
    def test_verify_visibility_the_title(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.check_visibility_the_title()

    def test_visibility_of_erin_recommends_widget(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.check_visibility_of_erin_recommends_widget()

    def test_clickability_of_erin_recommends_widget(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.check_clickability_of_erin_recommends_widget()

    def test_main_page_erin_recommends_is_clickable(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.scroll_down_to_shop_erin_recom()
        page.is_clickable(BasePageLocators.SHOP_ERIN_RECOMMENDS).click()
        assert driver.current_url == ErinRecommendsPage.URL

    def test_redirect_men_page_by_clicking_men_btn(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.men_btn_catalog().click()

        assert driver.current_url == MEN_PAGE

    def test_main_page_erin_recommends_visible(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.scroll_down_to_shop_erin_recom()
        page.is_visible(BasePageLocators.ERIN_SECTION)
        assert page.is_visible(BasePageLocators.ERIN_SECTION), "element is not visible"

    def test_main_page_shop_performance_is_clickable(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.scroll_down_to_shop_performance()
        page.is_clickable(BasePageLocators.SHOP_PERFORMANCE).click()
        assert driver.current_url == PerformanceFabricsPage.URL

    def test_presence_of_image_boxes(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        results = page.check_images_boxes_on_page()
        assert all(results), "Not all blocks are present on the page"
