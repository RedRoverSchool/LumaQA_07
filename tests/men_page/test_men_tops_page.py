from pages.men_category_page.men_tops_page import MenTops
from data.men_page_url import TOPS_MEN_PAGE, CASSIUS_SPARRING_TANK


class TestMenTopsPage:
    def test_greed_is_clickable(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        assert page.check_clickability_grid(), "Is not clickable"

    def test_navigate_product_by_clicking_foto(self, driver):
        """TC_008.004.002| Mens > Tops page > Product item >move to the Product page by clicking on the Product image (acceptance criteria 3)"""
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        page.click_men_tops_product_foto()
        assert driver.current_url == CASSIUS_SPARRING_TANK, "It's not a cassius sparring tank page"

    def test_navigate_product_by_clicking_title(self, driver):
        """TC_008.004.003| Mens > Tops page > Product item >move to the Product page by clicking on the Product title (acceptance criteria 4)"""
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        page.click_men_tops_product_title()
        assert driver.current_url == CASSIUS_SPARRING_TANK, "It's not a cassius sparring tank page"

    def test_grid_is_visible(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        assert page.check_visibility_grid(), "It is not visible"
