import pytest

import allure

from pages.men_category_page.men_tops_page import MenTops
from data.men_page_url import TOPS_MEN_PAGE, MEN_TOPS_CARDS, CASSIUS_SPARRING_TANK
from data.men_page_url import MEN_TOPS_HOODIES_PAGE


class TestMenTopsPage:
    def test_greed_is_clickable(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        assert page.check_clickability_grid(), "Is not clickable"

    @pytest.mark.parametrize('position, relevant_page', MEN_TOPS_CARDS)
    def test_navigate_product_by_clicking_foto(self, driver, position, relevant_page):
        """TC_008.004.002| Mens > Tops page > Product item >
        move to the Product page by clicking on the Product image (acceptance criteria 3)"""
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        page.click_men_tops_product_foto(position)
        assert driver.current_url == relevant_page, "Selected product is not relevant to open page"

    @pytest.mark.parametrize('position, relevant_page', MEN_TOPS_CARDS)
    def test_navigate_product_by_clicking_title(self, driver, position, relevant_page):
        """TC_008.004.003| Mens > Tops page > Product item >
        move to the Product page by clicking on the Product title (acceptance criteria 4)"""
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        page.click_men_tops_product_title(position)
        assert driver.current_url == relevant_page, "Selected product is not relevant to open page"

    @pytest.mark.parametrize('position, relevant_page', MEN_TOPS_CARDS)
    def test_navigate_product_by_clicking_add_to_card(self, driver, position, relevant_page):
        """TC_008.004.004| Mens > Tops page > Product item >
        move to the Product page by clicking on the BTN “Add to Cart“ (acceptance criteria 5)"""
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        page.go_to_men_tops_product(position)
        page.click_add_button(position)
        assert page.wait_url_redirection(relevant_page), "Selected product is not relevant to open page"

    def test_grid_is_visible(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        assert page.check_visibility_grid(), "It is not visible"

    @allure.title('TC_008.005.003 | Tops page > Products >Verify a mode-switcher "list" is Visible')
    def test_verify_a_mode_list_is_visible(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        assert page.mode_list_is_visible(), 'Mode-switcher list NOT Visible'

    @allure.title('TC_008.005.004 | Tops page > Products >Verify a mode-switcher "list" is Clicable')
    def test_verify_a_mode_list_is_clicable(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        assert page.mode_list_is_clickable(), 'Mode-switcher list NOT Clicable'

    @allure.title('TC_008.005.005 | Tops page > Products >Verify view modes change')
    def test_verify_view_modes_change(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        view_before, after_filter = page.list_page_view()
        assert view_before != after_filter, 'View did NOT change after click the filter'

    @allure.title('TC_008.013.001|Tops Page> Verify the link HoodiesSweatshirts redirects to a correct page')
    def test_verify_redirect_link_hoodies_sweatshirts(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        page.click_link_hoodies_sweatshirts()
        assert driver.current_url == MEN_TOPS_HOODIES_PAGE, 'Page NOT REDIRECT'
