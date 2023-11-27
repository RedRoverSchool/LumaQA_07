import pytest
from data.men_page_url import TOPS_MEN_PAGE, MEN_TOPS_CARDS
from pages.men_category_page.men_tops_page import MenTops

class TestAddToCard:
    @pytest.mark.parametrize('position, expected_url', MEN_TOPS_CARDS)
    def test_click_on_Add_to_Cart(self, driver, position, expected_url):
        page = MenTops(driver, TOPS_MEN_PAGE)
        page.open()
        current_url = page.driver.current_url

        page.hover_to_cart(position)
        page.check_button(position)
        page.wait_url(expected_url)

        assert current_url != expected_url
