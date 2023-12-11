import allure
from pages.men_page import MenPage, MenJacketsPage
from data.men_page_url import MEN_PAGE, TOPS_MEN_PAGE, MEN_BOTTOMS_PAGE, MEN_TOPS_JACKETS_PAGE


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
        assert driver.current_url == MEN_TOPS_JACKETS_PAGE

    def test_redirect_to_bottoms_men_page_from_men_dropdown_btn(self, driver):
        page = MenPage(driver, MEN_PAGE)
        page.open()
        page.select_bottoms_from_men_dropdown()
        assert driver.current_url == MEN_BOTTOMS_PAGE

    def test_redirect_to_tops_men_page_from_bottoms_category(self, driver):
        page = MenPage(driver, MEN_PAGE)
        page.open()
        page.select_bottoms_from_sidebar_menu()
        assert driver.current_url == MEN_BOTTOMS_PAGE


class TestMenJacketsPage:
    @allure.title('TC_008.011.005 | Jackets page >Verify inner-buttons are visable')
    def test_verify_inner_buttons_are_visable(self, driver):
        page = MenJacketsPage(driver, MEN_TOPS_JACKETS_PAGE)
        page.open()
        page.random_choice_item()
        inner_buttons = page.check_all_button()
        assert inner_buttons.is_displayed(), 'Buttons NOT DISPLAYED'

    @allure.title("TC_008.011.002 | Jackets page >Verify redirected to Item Page")
    def test_verify_redirected_to_item_page(self, driver, men_jacket_page, random_item):
        url_before_click = driver.current_url
        men_jacket_page.hold_mouse_on_element_and_click(random_item)
        url_after_click = driver.current_url
        assert url_after_click != url_before_click, 'NOT REDIRECT'

