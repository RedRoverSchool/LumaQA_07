import pytest

from pages.header.header_page import Header
from data.test_urls_list import HEADER_TEST_URLS



@pytest.mark.parametrize('URL', HEADER_TEST_URLS)
def test_tc_003_001_001_logo_is_visible(driver, URL):
    page = Header(driver, URL)
    page.open()
    page.check_logo_visibility()


