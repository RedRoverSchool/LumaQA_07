from pages.main_page import MainPage
from locators.base_page_locators import BasePageLocators
from pages.erin_recommends.erin_recommends import ErinRecommendsPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


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