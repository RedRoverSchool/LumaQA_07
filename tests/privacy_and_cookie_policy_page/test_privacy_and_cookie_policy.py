import pytest
from base.seleniumbase import BasePage
from data.privacy_and_cookie_policy_page_urls import PRIVACY_AND_COOKIE_POLICY_PAGE, LIST_OF_COOKIES_WE_COLLECT_SECTION
from data.contact_us_page_urls import CONTACT_US_PAGE
from data.privacy_and_cookie_policy_page_fonts import PrivacyCookiePolicyFonts
from locators.privacy_and_cookie_policy_page_locators import PrivacyCookiePolicyPageLocators, PrivacyCookiePolicyAnchorLinksLocators
import language_tool_python

@pytest.mark.parametrize('locator, css_value, expected_result', [
    (PrivacyCookiePolicyPageLocators.YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_CONTENT_LOCATOR, 'font-family', PrivacyCookiePolicyFonts.TEXT_FONT_FAMILY),
    (PrivacyCookiePolicyPageLocators.YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_HEADER_LOCATOR, 'font-size', PrivacyCookiePolicyFonts.HEADER_TEXT_FONT_SIZE),
    (PrivacyCookiePolicyPageLocators.YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_CONTENT_LOCATOR, 'font-size', PrivacyCookiePolicyFonts.TEXT_FONT_SIZE),
    (PrivacyCookiePolicyPageLocators.LIST_OF_COOKIE_FILES_WE_COLLECT_LINK_IN_TEXT_BLOCK, 'color', 'rgba(0, 107, 180, 1)'),
    (PrivacyCookiePolicyPageLocators.CONTACT_US_LINK_LOCATOR, 'color', 'rgba(0, 107, 180, 1)')
])
def test_privacy_cookie_policy_value_of_elements(driver, locator, css_value, expected_result):
    """TC_012.007.001 | Footer > "Privacy and Cookie Policy" > Content >
     The Font family of the text block titled 'Your Choices Regarding Use Of The Information We Collect'"""

    """TC_012.007.002 | Footer > "Privacy and Cookie Policy" > Content >
     The Font-size of the title 'Your Choices Regarding Use Of The Information We Collect'"""

    """TC_012.007.003 | Footer > "Privacy and Cookie Policy" > Content >
     The Font-size of the text of the block titled 'Your Choices Regarding Use Of The Information We Collect'"""

    """TC_012.014.001 | Footer > "Privacy and Cookie Policy" > Navigation within text >
    Visability of the "List of cookies we collect" text in the section "The Information We Collect."""

    """TC_012.015.001 | Footer > Privacy and Cookie Policy Page > Contact us link >
     Visibility of the "Contact Us" text in the "Questions for Luma?" section"""

    page = BasePage(driver, url=PRIVACY_AND_COOKIE_POLICY_PAGE)
    page.open()
    font_size = page.is_visible(locator).value_of_css_property(css_value)
    assert font_size == expected_result

def test_text_block_for_typos_titled_your_choices_regarding_use_of_the_information_we_collect(driver):
    """TC_012.007.004 | Footer > "Privacy and Cookie Policy" > Content > Verify the text block and title for typos
    titled ‘Your Choices Regarding Use Of The Information We Collect’"""
    page = BasePage(driver, url=PRIVACY_AND_COOKIE_POLICY_PAGE)
    page.open()
    text_header = page.get_text(PrivacyCookiePolicyPageLocators.YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_HEADER_LOCATOR)
    text_block = page.get_text(PrivacyCookiePolicyPageLocators.YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_CONTENT_LOCATOR)
    tool = language_tool_python.LanguageTool('en-US')
    matches_header = tool.check(text_header)
    matches_block = tool.check(text_block)
    assert len(matches_header) == 0 and len(matches_block) == 0, f"Grammar mistakes have been found in the header: {matches_header}, and in the text block: {matches_block}"

def test_text_block_format_titled_list_of_cookie_files_we_collect(driver):
    """TC_012.007.005 | Footer > "Privacy and Cookie Policy" > Content >
     Verify the text of the block ‘List of cookie files we collect’ is presented in a tabular format"""
    page = BasePage(driver, url=PRIVACY_AND_COOKIE_POLICY_PAGE)
    page.open()
    element_format = page.is_visible(locator=PrivacyCookiePolicyPageLocators.LIST_OF_COOKIE_FILES_WE_COLLECT_CONTENT_LOCATOR).tag_name
    assert element_format == 'table', f"The text of the block is NOT presented in a tabular format"

@pytest.mark.parametrize('locator, expected_page_url', [
    (PrivacyCookiePolicyPageLocators.LIST_OF_COOKIE_FILES_WE_COLLECT_LINK_IN_TEXT_BLOCK, LIST_OF_COOKIES_WE_COLLECT_SECTION),
    (PrivacyCookiePolicyPageLocators.CONTACT_US_LINK_LOCATOR, CONTACT_US_PAGE)])
def test_opening_pages_after_links_clicking(driver, locator, expected_page_url):
    """TC_012.014.002 | Footer > "Privacy and Cookie Policy" > Navigation within text >
     Verify redirection of the "List of cookies we collect" section"""
    """TC_012.015.002 | Footer > "Privacy and Cookie Policy" > Navigation within text >
     Verify opening the contact page"""
    page = BasePage(driver, url=PRIVACY_AND_COOKIE_POLICY_PAGE)
    page.open()
    page.is_clickable(locator).click()
    assert page.current_url == expected_page_url, f"The expected page {expected_page_url} isn`t open"

@pytest.mark.parametrize('anchor_link_locator', [
    (PrivacyCookiePolicyAnchorLinksLocators.LUMA_SECURITY),
    (PrivacyCookiePolicyAnchorLinksLocators.LUMA_PRIVACY_POLICY),
    (PrivacyCookiePolicyAnchorLinksLocators.THE_INFORMATION_WE_COLLECT),
    (PrivacyCookiePolicyAnchorLinksLocators.HOW_WE_USE_THE_INFORMATION_WE_COLLECT),
    (PrivacyCookiePolicyAnchorLinksLocators.SECURITY),
    (PrivacyCookiePolicyAnchorLinksLocators.OTHERS_WITH_WHOM_WE_SHARE_YOUR_INFORMATION),
    (PrivacyCookiePolicyAnchorLinksLocators.YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT),
    (PrivacyCookiePolicyAnchorLinksLocators.YOUR_CALIFORNIA_PRIVACY_RIGHTS),
    (PrivacyCookiePolicyAnchorLinksLocators.COOKIES_WEB_BEACONS_AND_HOW_WE_USE_THEM),
    (PrivacyCookiePolicyAnchorLinksLocators.LIST_OF_COOKIES_WE_COLLECT),
    (PrivacyCookiePolicyAnchorLinksLocators.ONLINE_ACCOUNT_REGISTRATION),
    (PrivacyCookiePolicyAnchorLinksLocators.EMAILS),
    (PrivacyCookiePolicyAnchorLinksLocators.ACCEPTANCE),
    (PrivacyCookiePolicyAnchorLinksLocators.QUESTIONS_FOR_LUMA)])
def test_anchor_links_in_the_left_navbar_are_displayed(driver, anchor_link_locator):
    """TC_012.005.001 | Footer > "Privacy and Cookie Policy" > Visibility and clickability >
    Visability of the anchor links"""
    page = BasePage(driver, url=PRIVACY_AND_COOKIE_POLICY_PAGE)
    page.open()
    assert page.is_visible(anchor_link_locator), f"{anchor_link_locator} - isn`t visible"

@pytest.mark.parametrize('anchor_link_locator', [
    (PrivacyCookiePolicyAnchorLinksLocators.LUMA_SECURITY),
    (PrivacyCookiePolicyAnchorLinksLocators.LUMA_PRIVACY_POLICY),
    (PrivacyCookiePolicyAnchorLinksLocators.THE_INFORMATION_WE_COLLECT),
    (PrivacyCookiePolicyAnchorLinksLocators.HOW_WE_USE_THE_INFORMATION_WE_COLLECT),
    (PrivacyCookiePolicyAnchorLinksLocators.SECURITY),
    (PrivacyCookiePolicyAnchorLinksLocators.OTHERS_WITH_WHOM_WE_SHARE_YOUR_INFORMATION),
    (PrivacyCookiePolicyAnchorLinksLocators.YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT),
    (PrivacyCookiePolicyAnchorLinksLocators.YOUR_CALIFORNIA_PRIVACY_RIGHTS),
    (PrivacyCookiePolicyAnchorLinksLocators.COOKIES_WEB_BEACONS_AND_HOW_WE_USE_THEM),
    (PrivacyCookiePolicyAnchorLinksLocators.LIST_OF_COOKIES_WE_COLLECT),
    (PrivacyCookiePolicyAnchorLinksLocators.ONLINE_ACCOUNT_REGISTRATION),
    (PrivacyCookiePolicyAnchorLinksLocators.EMAILS),
    (PrivacyCookiePolicyAnchorLinksLocators.ACCEPTANCE),
    (PrivacyCookiePolicyAnchorLinksLocators.QUESTIONS_FOR_LUMA)])
def test_anchor_links_in_the_left_navbar_are_clickable(driver, anchor_link_locator):
    """TC_012.005.001 | Footer > "Privacy and Cookie Policy" > Visibility and clickability >
    Visability of the anchor links"""
    page = BasePage(driver, url=PRIVACY_AND_COOKIE_POLICY_PAGE)
    page.open()
    assert page.is_clickable(anchor_link_locator), f"{anchor_link_locator} - isn`t clickable"


