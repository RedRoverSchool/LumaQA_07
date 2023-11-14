import time

from pages.men_page import MenPage
from data.men_page_url import TOPS_MEN_PAGE


class TestMenPage:
    def test_redirect_to_tops_men_page_from_tops_category(self, driver):
        page = MenPage(driver, url=MenPage.URL)
        page.open()
        page.select_tops_from_sidebar_menu()
        assert driver.current_url == TOPS_MEN_PAGE

    def test_redirect_to_tops_men_page_from_men_dropdown_btn(self, driver):
        page = MenPage(driver, url=MenPage.URL)
        page.open()
        page.select_tops_from_men_dropdown()
        assert driver.current_url == TOPS_MEN_PAGE
