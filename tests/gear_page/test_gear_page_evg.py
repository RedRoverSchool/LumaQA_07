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

@pytest.mark.parametrize('locator, expected_page_url', [
    pytest.param(BannerLocators.SPRITE_YOGA_COMPANION_KIT_BANNER, SPRITE_YOGA_COMPANION_KIT_PAGE, marks=pytest.mark.xfail(reason="some bug")),
    pytest.param(BannerLocators.SPRITE_YOGA_COMPANION_KIT_BANNER_BUTTON, SPRITE_YOGA_COMPANION_KIT_PAGE, marks=pytest.mark.xfail(reason="some bug")),
    (BannerLocators.LOOSEN_UP_BANNER, SHOP_FITNESS_PAGE),
    (BannerLocators.LUMA_WATER_BOTTLE_BANNER, LUMA_WATER_BOTTLE_PAGE),
    (BannerLocators.BAGS_BANNER, BAGS_PAGE),
    (BannerLocators.FITNESS_EUQIPMENT_BANNER, FITNESS_EQ_PAGE),
    (BannerLocators.WATCHES_BANNER, WATCHES_PAGE),
])
def test_opening_pages_after_banners_clicking(driver, locator, expected_page_url):
    """TC_009.005.001 | Gear page > categories > Verify opening the ‘Sprite Yoga Companion Kit’ page"""
    """TC_009.005.002 | Gear page > categories > Verify opening the 'Sprite Yoga Companion Kit' page after clicking on the "Shop Yoga Kit" button"""
    """TC_009.005.003 | Gear page > categories > Verify opening the ‘Shop Fitness’ page"""
    """TC_009.005.004 | Gear page > categories > Verify opening the ‘Luma water bottle’ page"""
    """TC_009.006.001 | Gear page > categories >Verify opening the 'Bags' page"""
    """TC_009.006.002 | Gear page > categories > Verify opening the 'Fitness Equipment' page"""
    """TC_009.006.003 | Gear page > categories > Verify opening the 'Watches' page"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    page.is_clickable(locator).click()
    assert page.current_url == expected_page_url, f"The expected page - {expected_page_url} isn`t open"



