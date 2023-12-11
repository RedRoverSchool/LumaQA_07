import pytest

from data.gear_page_urls import GEAR_PAGE, SPRITE_YOGA_COMPANION_KIT_PAGE, SHOP_FITNESS_PAGE, LUMA_WATER_BOTTLE_PAGE,\
    BAGS_PAGE, FITNESS_EQ_PAGE, WATCHES_PAGE
from locators.gear_page_locators import BannerLocators
from base.seleniumbase import BasePage


@pytest.mark.parametrize('element_locator, expected_result', [
    (BannerLocators.SPRITE_YOGA_COMPANION_KIT_BANNER, True),
    (BannerLocators.LOOSEN_UP_BANNER, True),
    (BannerLocators.LUMA_WATER_BOTTLE_BANNER, True),
    (BannerLocators.BAGS_BANNER, True),
    (BannerLocators.FITNESS_EUQIPMENT_BANNER, True),
    (BannerLocators.WATCHES_BANNER, True),
])
def test_banners_of_page_are_visible(driver, element_locator, expected_result):
    """TC_009.003.001 | Gear page > categories > Visibility of the 'Sprite Yoga Companion Kit' banner"""
    """TC_009.003.002 | Gear page > categories > Visibility of the 'Loosen Up' banner"""
    """TC_009.003.003 | Gear page > categories > Visibility of the 'Luma water bottle' banner"""
    """TC_009.004.001 | Gear page > categories >Visibility of the 'Bags' banner"""
    """TC_009.004.002 | Gear page > categories > Visibility of the 'Fitness Equipment' banner"""
    """TC_009.004.003 | Gear page > categories > Visibility of the 'Watches' banner"""
    page = BasePage(driver,  url=GEAR_PAGE)
    page.open()
    banner = page.is_visible(element_locator).is_displayed()
    assert banner == expected_result, f"{element_locator} - isn`t visible"


@pytest.mark.xfail
def test_sprite_yoga_companion_kit_page_is_open(driver):
    """TC_009.005.001 | Gear page > categories > Verify opening the ‘Sprite Yoga Companion Kit’ page"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    page.is_visible(BannerLocators.SPRITE_YOGA_COMPANION_KIT_BANNER).click()
    current_page = driver.current_url
    assert current_page == SPRITE_YOGA_COMPANION_KIT_PAGE


@pytest.mark.xfail
def test_sprite_yoga_companion_kit_page_is_open_after_click_button(driver):
    """TC_009.005.002 | Gear page > categories > Verify opening the 'Sprite Yoga Companion Kit' page after clicking on the "Shop Yoga Kit" button"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    page.is_visible(BannerLocators.SPRITE_YOGA_COMPANION_KIT_BANNER_BUTTON).click()
    current_page = driver.current_url
    assert current_page == SPRITE_YOGA_COMPANION_KIT_PAGE

def test_shop_fitness_page_is_open(driver):
    """TC_009.005.003 | Gear page > categories > Verify opening the ‘Shop Fitness’ page"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    page.is_visible(BannerLocators.LOOSEN_UP_BANNER).click()
    current_page = driver.current_url
    assert current_page == SHOP_FITNESS_PAGE

def test_luma_bottle_water_page_is_open(driver):
    """TC_009.005.004 | Gear page > categories > Verify opening the ‘Luma water bottle’ page"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    page.is_visible(BannerLocators.LUMA_WATER_BOTTLE_BANNER).click()
    current_page = driver.current_url
    assert current_page == LUMA_WATER_BOTTLE_PAGE

def test_bags_page_is_open(driver):
    """TC_009.006.001 | Gear page > categories >Verify opening the 'Bags' page"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    page.is_visible(BannerLocators.BAGS_BANNER).click()
    current_page = driver.current_url
    assert current_page == BAGS_PAGE

def test_fitness_equipment_page_is_open(driver):
    """TC_009.006.002 | Gear page > categories > Verify opening the 'Fitness Equipment' page"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    page.is_visible(BannerLocators.FITNESS_EUQIPMENT_BANNER).click()
    current_page = driver.current_url
    assert current_page == FITNESS_EQ_PAGE

def test_watches_page_is_open(driver):
    """TC_009.006.003 | Gear page > categories > Verify opening the 'Watches' page"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    page.is_visible(BannerLocators.WATCHES_BANNER).click()
    current_page = driver.current_url
    assert current_page == WATCHES_PAGE


