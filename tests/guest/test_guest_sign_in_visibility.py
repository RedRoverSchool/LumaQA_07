from locators.base_page_locators import BasePageLocators as bpl
from pages.main_page import MainPage


""" TC_004.001.006 | Authorization >Anonym user > Signing in > Visibility
    Pre-conditions:
        User is not logged in
        The page Home Page is opened

    Expected results:
        "Sign in" link is visible"""


def test_guest_tabs_access(driver):
    page = MainPage(driver, MainPage.URL)
    page.open()
    assert page.is_visible(bpl.LINK_HEADER_SIGN_IN)
