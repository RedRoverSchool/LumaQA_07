import time

from pages.men_page import MenPage
from data.men_page_url import MEN_PAGE, TOPS_MEN_PAGE, BOTTOMS_MEN_PAGE, JACKETS_MEN_PAGE


class TestMenPage:
    def test_redirect_to_tops_men_page_from_tops_category(self, driver):
        page = MenPage(driver, MEN_PAGE)
        page.open()
        page.select_tops_from_sidebar_menu()
        assert driver.current_url == TOPS_MEN_PAGE

    def test_redirect_to_tops_men_page_from_men_dropdown_btn(self, driver):
        page = MenPage(driver, MEN_PAGE)
        page.open()
        page.select_tops_from_men_dropdown()
        assert driver.current_url == TOPS_MEN_PAGE

    def test_redirect_to_jackets_page_from_tops(self, driver):
        page = MenPage(driver, url=MenPage.URL)
        page.open()
        page.select_tops_from_sidebar_menu()
        page.select_jackets_from_tops_dropdown()
        assert driver.current_url == JACKETS_MEN_PAGE

    def test_redirect_to_bottoms_men_page_from_men_dropdown_btn(self, driver):
        page = MenPage(driver, MEN_PAGE)
        page.open()
        page.select_bottoms_from_men_dropdown()
        assert driver.current_url == BOTTOMS_MEN_PAGE

