import pytest
import re
from data.whats_new_page import WHATS_NEW_PAGE
from data.women_page_urls import *
from data.men_page_url import *
from data.gear_page_urls import *
from data.training_page import *
from data.sale_page import *
from locators.base_page_locators import BasePageLocators as bpl
from pages.main_page import MainPage
import importlib


""" TC_004.001.001 | Authorization >Anonym user > Accessibility of site pages > Menu sections
    Pre-conditions:
        User is not logged in
        The page Home Page is opened

    Steps:
        Click “What’s New“ menu section
    
    Expected results:
        The What's New page is opened
    
    *Make the same test for all menu items of all menu sections (“Women”, “Men”, “Gear”, “Training”, “Sale”)"""


@pytest.mark.parametrize("locator, assert_page",   [(bpl.LINK_WHATS_NEW, WHATS_NEW_PAGE),
                                                    (bpl.LINK_WOMEN, WOMEN_PAGE),
                                                    (bpl.LINK_WOMEN_TOPS, WOMEN_TOPS_PAGE),
                                                    (bpl.LINK_WOMEN_TOPS_JACKETS, WOMEN_TOPS_JACKETS_PAGE),
                                                    (bpl.LINK_WOMEN_TOPS_HOODIES, WOMEN_TOPS_HOODIES_PAGE),
                                                    (bpl.LINK_WOMEN_TOPS_TEES, WOMEN_TOPS_TEES_PAGE),
                                                    (bpl.LINK_WOMEN_TOPS_BRAS_AND_TANKS, WOMEN_TOPS_BRAS_AND_TANKS_PAGE),
                                                    (bpl.LINK_WOMEN_BOTTOMS, WOMEN_BOTTOMS_PAGE),
                                                    (bpl.LINK_WOMEN_BOTTOMS_PANTS, WOMEN_BOTTOMS_PANTS_PAGE),
                                                    (bpl.LINK_WOMEN_BOTTOMS_SHORTS, WOMEN_BOTTOMS_SHORTS_PAGE),
                                                    (bpl.LINK_MEN, MEN_PAGE),
                                                    (bpl.LINK_MEN_TOPS, TOPS_MEN_PAGE),
                                                    (bpl.LINK_MEN_TOPS_JACKETS, MEN_TOPS_JACKETS_PAGE),
                                                    (bpl.LINK_MEN_TOPS_HOODIES, MEN_TOPS_HOODIES_PAGE),
                                                    (bpl.LINK_MEN_TOPS_TEES, MEN_TOPS_TEES_PAGE),
                                                    (bpl.LINK_MEN_TOPS_TANKS, MEN_TOPS_TANKS_PAGE),
                                                    (bpl.LINK_MEN_BOTTOMS, MEN_BOTTOMS_PAGE),
                                                    (bpl.LINK_MEN_BOTTOMS_PANTS, MEN_BOTTOMS_PANTS_PAGE),
                                                    (bpl.LINK_MEN_BOTTOMS_SHORTS, MEN_BOTTOMS_SHORTS_PAGE),
                                                    (bpl.LINK_GEAR, GEAR_PAGE),
                                                    (bpl.LINK_GEAR_BAGS, BAGS_PAGE),
                                                    (bpl.LINK_GEAR_FITNESS_EQ, FITNESS_EQ_PAGE),
                                                    (bpl.LINK_GEAR_WATCHES, WATCHES_PAGE),
                                                    (bpl.LINK_TRAINING, TRAINING_PAGE),
                                                    (bpl.LINK_TRAINING_VIDEO_DOWNLOAD, TRAINING_VIDEO_DOWNLOAD_PAGE),
                                                    (bpl.LINK_SALE, SALE_PAGE)])
def test_guest_tabs_access(driver, locator, assert_page):
    extracted_string = re.search(r'\.com/(.*?)\.html', assert_page).group(1).split("/")
    menu_section = extracted_string[0]
    page = MainPage(driver, MainPage.URL)
    page.open()
    parent_locator = 'LINK'
    if len(extracted_string) > 1:
        for item in extracted_string[:-1]:
            parent_locator = parent_locator + '_' + item.replace(f"-{menu_section}", "").replace("-", "_").upper()
            config_module = importlib.import_module('locators.base_page_locators').BasePageLocators
            variable_value = getattr(config_module, parent_locator)
            page.hold_mouse_on_element(variable_value)
    page.is_clickable(locator).click()
    assert page.current_url == assert_page
