import pytest
from data.men_page_url import MEN_BOTTOMS_SHORTS_PAGE
from pages.men_category_page.men_shorts_page import MenShortsPage
from data.men_page_url import MEN_SHORTS_CARDS


class TestMenShortsPage:

    @pytest.mark.parametrize('title, expected_url', MEN_SHORTS_CARDS)
    def test_visibility_and_selectability_of_one_of_the_products(self, driver, title, expected_url):
        shorts_page = MenShortsPage(driver, MEN_BOTTOMS_SHORTS_PAGE)
        shorts_page.open()
        title_before = shorts_page.check_title(title)
        shorts_page.click_any_product(title)
        title_after_redirection = shorts_page.check_title_on_new_page(title)
        assert shorts_page.check_visibility_of_elements(), 'There are not all products on the page'
        assert title_before == title_after_redirection, 'Wrong title'
        assert shorts_page.current_url == expected_url, 'Wrong URL'
