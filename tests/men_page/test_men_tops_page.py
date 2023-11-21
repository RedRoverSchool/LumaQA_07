from pages.men_category_page.men_tops_page import MenTops
from data.men_page_url import TOPS_MEN_PAGE
class TestMenTopsPage:
    def test_greed_is_clickable(self, driver):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        assert page.check_clickability_grid(), "Is not clickable"