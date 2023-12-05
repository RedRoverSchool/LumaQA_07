import pytest
from data.men_page_url import MEN_TOPS_JACKETS_PAGE, MEN_TOPS_JACKETS_EXPECTED_URLS
from pages.men_category_page.men_tops_page import MenTops


class TestImageRedirect:
    @pytest.mark.parametrize('position, expected_url', MEN_TOPS_JACKETS_EXPECTED_URLS)
    def test_image_click(self, driver, position, expected_url):
        page = MenTops(driver, MEN_TOPS_JACKETS_PAGE)
        page.open()

        page.click_image(position)
        page.wait_url(expected_url)

        assert page.current_url == expected_url
