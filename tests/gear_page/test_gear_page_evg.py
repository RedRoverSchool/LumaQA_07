from data.gear_page_urls import GEAR_PAGE, SPRITE_YOGA_COMPANION_KIT_PAGE
from locators.gear_page_locators import BannerLocators
from base.seleniumbase import BasePage

def test_sprite_yoga_companion_kit_is_visible(driver):
    """TC_009.003.001 | Gear page > categories > Visibility of the 'Sprite Yoga Companion Kit' banner"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    assert page.is_visible(BannerLocators.SPRITE_YOGA_COMPANION_KIT_BANNER)

def test_loosen_up_is_visible(driver):
    """TC_009.003.002 | Gear page > categories > Visibility of the 'Loosen Up' banner"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    assert page.is_visible(BannerLocators.LOOSEN_UP_BANNER)

def test_luma_water_bottle_is_visible(driver):
    """TC_009.003.003 | Gear page > categories > Visibility of the 'Luma water bottle' banner"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    assert page.is_visible(BannerLocators.LUMA_WATER_BOTTLE_BANNER)
    
def test_bags_is_visible(driver):
    """TC_009.004.001 | Gear page > categories >Visibility of the 'Bags' banner"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    assert page.is_visible(BannerLocators.BAGS_BANNER)

def test_fitness_equipment_is_visible(driver):
    """TC_009.004.002 | Gear page > categories > Visibility of the 'Fitness Equipment' banner"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    assert page.is_visible(BannerLocators.FITNESS_EUQIPMENT_BANNER)

def test_watches_is_visible(driver):
    """TC_009.004.003 | Gear page > categories > Visibility of the 'Watches' banner"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    assert page.is_visible(BannerLocators.WATCHES_BANNER)

def test_sprite_yoga_companion_kit_page_is_open(driver):
    """TC_009.005.001 | Gear page > categories > Verify opening the ‘Sprite Yoga Companion Kit’ page"""
    page = BasePage(driver, url=GEAR_PAGE)
    page.open()
    page.is_visible(BannerLocators.SPRITE_YOGA_COMPANION_KIT_BANNER).click()
    current_page = driver.current_url
    assert current_page == SPRITE_YOGA_COMPANION_KIT_PAGE
