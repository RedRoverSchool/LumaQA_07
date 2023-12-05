
import pytest
from data.advanced_search_url import ADVANCED_SEARCH_URL
from locators.advanced_search_locators import AdvancedSearchLocators
from base.seleniumbase import BasePage

def test_advanced_fields(driver):
    page=BasePage(driver,ADVANCED_SEARCH_URL)
    page.open()
    assert page.is_visible(AdvancedSearchLocators.Product_Name).text=='Product Name'
    assert page.is_visible(AdvancedSearchLocators.SKU).text=='SKU'
    assert page.is_visible(AdvancedSearchLocators.Description).text=='Description'
    assert page.is_visible(AdvancedSearchLocators.ShortDescription).text=='Short Description'
    assert page.is_visible(AdvancedSearchLocators.Price).text=='Price'
    assert page.is_visible(AdvancedSearchLocators.USD).text=='USD'






