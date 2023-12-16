import time

import pytest
from data.advanced_search_url import ADVANCED_SEARCH_GRID_URL, ADVANCED_SEARCH_RESULT_URL, ADVANCED_SEARCH_LIST_URL
from locators.advanced_search_locators import AdvancedSearchLocators
from base.seleniumbase import BasePage


def test_search_results(driver):
    page = BasePage(driver, ADVANCED_SEARCH_RESULT_URL)
    page.open()
    page.find_element_and_click(AdvancedSearchLocators.GRID)
    assert driver.current_url == ADVANCED_SEARCH_GRID_URL
    page.find_element_and_click(AdvancedSearchLocators.LIST)
    assert driver.current_url==ADVANCED_SEARCH_LIST_URL
