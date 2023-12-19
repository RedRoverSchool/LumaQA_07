import pytest
import re
from data.footer_urls import *
from data.whats_new_page import WHATS_NEW_PAGE
from locators.base_page_locators import BasePageLocators as bpl
from pages.main_page import MainPage
import importlib


""" TC_004.001.007 | Authorization >Anonym user > Accessibility of site pages > Footer
    Pre-conditions:
        User is not logged in
        The page Home Page is opened

    Steps:

        Click “What’s New“ menu section
    
    Expected results:
        The What's New page is opened
        *Make the same test for all items of footer (“Write for us”, “Subscribe to our mailing list”, 
        “Contact us”, “Hire a Software Testing/QA Company”, “Search Terms”, “Privacy and Cookie Policy”, 
        “Advanced Search” and “Orders and Returns”)."""


@pytest.mark.parametrize("locator, assert_page", [(bpl.LINK_WHATS_NEW, WHATS_NEW_PAGE),
                                                  (bpl.LINK_WRITE_FOR_US, WRITE_FOR_US_PAGE),
                                                  (bpl.LINK_SUBSCRIBE_TO_OUR_MAILING_LIST, SUBSCRIBE_TO_OUR_MAILING_LIST_PAGE),
                                                  (bpl.LINK_CONTACT_US, CONTACT_US_PAGE),
                                                  (bpl.LINK_HIRE, HIRE_PAGE),
                                                  (bpl.LINK_SEARCH_TERMS, SEARCH_TERMS_PAGE),
                                                  (bpl.LINK_PRIVACY_AND_COOKIE_POLICY, PRIVACY_AND_COOKIE_POLICY_PAGE),
                                                  (bpl.LINK_ADVANCED_SEARCH, ADVANCED_SEARCH_PAGE),
                                                  (bpl.LINK_ORDERS_AND_RETURNS, ORDERS_AND_RETURNS_PAGE)])
def test_guest_tabs_access(driver, locator, assert_page):
    page = MainPage(driver, MainPage.URL)
    page.open()
    page.is_visible(locator).click()
    assert page.current_url == assert_page
