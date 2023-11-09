import pytest
from pages.gear_page.gear_page import GearPage

@pytest.fixture(scope="function")
def gear_page_precondition(driver):
    gear_page = GearPage(driver=driver)
    gear_page.open()
    return gear_page
