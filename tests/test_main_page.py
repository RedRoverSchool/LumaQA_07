import time
import pytest
from pages.main_page import MainPage
from locators.base_page_locators import BasePageLocators
from pages.erin_recommends.erin_recommends import ErinRecommendsPage
from data.men_page_url import MEN_PAGE, TOPS_MEN_PAGE
from pages.performance_fabrics.performance_fabrics import PerformanceFabricsPage
from pages.eco_friendly.eco_friendly import EcoFriendlyPage
from data.performance_fabrics_url import PERFORMANCE_FABRICS_URL
from data.home_page_url import HOME_PAGE

class TestMainPage:
    def test_verify_visibility_the_title(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        assert page.check_visibility_the_title(), "The title not found"

    def test_visibility_of_erin_recommends_widget(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        assert page.check_visibility_of_erin_recommends_widget(), "widget not found"

    def test_clickability_of_erin_recommends_widget(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        assert page.check_clickability_of_erin_recommends_widget(), "widget not clicked"

    def test_main_page_erin_recommends_is_clickable(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.scroll_down_to_shop_erin_recom()
        page.is_clickable(BasePageLocators.SHOP_ERIN_RECOMMENDS).click()
        assert driver.current_url == ErinRecommendsPage.URL

    def test_redirect_men_page_by_clicking_men_btn(self, driver):
        """TC_008.001.001 | Main page > Men page > user able to select Men catalog on the Main page"""
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.men_btn_catalog().click()

        assert driver.current_url == MEN_PAGE

    def test_select_tops_from_men_dropdown_menu(self, driver):
        """TC_008.002.001 | Men Page > Select item Tops from Men BTN dropdown menu"""
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.select_tops_from_mens_dropdown_menu()
        assert page.visibility_of_men_tops_secondary_dropdown_menu(), "element is not visible"

    def test_select_bottoms_from_men_dropdown_menu(self, driver):
        """TC_008.002.002| Men Page > Select item Bottoms from Men BTN dropdown menu"""
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.select_bottoms_from_mens_dropdown_menu()
        assert page.visibility_of_men_bottoms_secondary_dropdown_menu(), "element is not visible"

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

    def test_main_page_eco_friendly_is_clickable(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.scroll_down_to_shop_eco_friendly()
        page.is_clickable(BasePageLocators.SHOP_ECO_FRIENDLY).click()
        assert driver.current_url == EcoFriendlyPage.URL

    def test_correct_switch_to_shop_performance(self, driver):
        "TC_001.003.002"
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.is_clickable(BasePageLocators.BLOCK_5).click()
        assert driver.current_url == PERFORMANCE_FABRICS_URL

    def test_main_page_eco_friendly_is_visible(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.scroll_down_to_shop_eco_friendly()
        assert page.is_visible(BasePageLocators.SHOP_ECO_FRIENDLY), "element is not visible"

    @pytest.mark.parametrize('link_1', BasePageLocators.LIST_MENU_BAR)
    def test_elements_of_menu_bar_is_visible_and_clickable(self, driver, link_1):
        page = MainPage(driver, HOME_PAGE)
        page.open()
        page.check_visible_of_menu_bar(link_1)
