import pytest
from locators.base_page_locators import BasePageLocators
from data.test_urls_list import TEST_URL_LIST



class TestFooterElementsVisibleClickable:
    PARAMETERS = [
        "visibility",
        "clickability",
    ]
    
    @pytest.mark.long
    @pytest.mark.parametrize("param", PARAMETERS)
    @pytest.mark.parametrize("any_url", TEST_URL_LIST)
    def test_check_visibility_or_clickability_of_the_title_write_for_us(
        self, param, any_url, driver,any_page_precondition
    ):
        """
        TC_012.001.001 | Footer > "Write for us" link > Verify visibility of the link for the page for writing an article
        TC_012.001.002 | Footer > "Write for us" link > Verify clickability of the link for the page for writing an article
            Steps:
                1. Open any page on The Site.
                2. Locate the Footer section.
                3. Verify the presence of/ability to click on  the title "Write For Us" in the Footer.
            Expected results:
                The title "Write For Us" is visible/clickable in the footer of current page of The Site.
        """

        expected_link = "https://softwaretestingboard.com/write-for-us/"

        any_page = any_page_precondition
        any_page.verify_visability_or_clickability_of_the_element_in_location(
            param=param,
            element_value=f"The link to the '{expected_link}'",
            element_locator=BasePageLocators.LINK_WRITE_FOR_US,
            location="the footer",
        )

    @pytest.mark.long
    @pytest.mark.parametrize("any_url", TEST_URL_LIST)
    def test_check_visibility_of_the_copyright(self, any_url, driver,any_page_precondition):
        """
        TC_012.011.001 | Footer > Self > Verify Copyright statement in the footer
            Steps:
                1. Open any page on the website.
                2. Locate the Footer section.
                3. Verify the presence of the copyright statement in the Footer.
            Expected results:
                The copyright information is visible in the footer of current page of the website.
        """

        any_page = any_page_precondition
        any_page.verify_visability_or_clickability_of_the_element_in_location(
            param="visibility",
            element_value="The copyright information",
            element_locator=BasePageLocators.COPYRIGHT_INFO,
            location="the footer",
        )

    @pytest.mark.long
    @pytest.mark.parametrize("any_url", TEST_URL_LIST)
    def test_text_verification_of_the_copyright(self, any_url, driver,any_page_precondition):
        """
        TC_012.011.002 | Footer > Self > Text verification of Copyright information
            Precondition:
                User on any page of the website and the copyright information is visible in the Footer.
            Steps:
                Verify the text of the copyright information in the Footer.
            Expected results:
                The copyright information should have a text “Copyright © 2013-present Magento, Inc. All rights reserved.”
                opyright information is visible in the footer of current page of the website.
        """

        expected_text = "Copyright © 2013-present Magento, Inc. All rights reserved."
        any_page = any_page_precondition
        copyright_info = any_page.is_visible(locator=BasePageLocators.COPYRIGHT_INFO)
        assert (
            copyright_info.text == expected_text
        ), f"""
            The copiright information from this page {any_url} = '{copyright_info.text}' and mismatch to the expected text ('{expected_text}')"""


    @pytest.mark.long
    @pytest.mark.parametrize("param", PARAMETERS)
    @pytest.mark.parametrize("any_url", TEST_URL_LIST)
    def test_check_visibility_or_clickability_of_the_search_terms_title(
        self, param, any_url, driver, any_page_precondition
    ):
        """
        TC_012.003.001 | Footer > "Search terms" link > Visibility and clickability > Visibility of the 'Search Terms' link
        TC_012.003.002 | Footer > "Search terms" link > Visibility and clickability > Verify The 'Search Terms' link is clickable
        TC_012.004.001 | Footer > "Search terms" link > Redirection > Verify opening the 'Popular Search Terms' page
        """

        expected_link = "https://magento.softwaretestingboard.com/search/term/popular/"

        any_page = any_page_precondition
        any_page.verify_visability_or_clickability_of_the_element_in_location(
            param=param,
            element_value=f"The link to the '{expected_link}'",
            element_locator=BasePageLocators.LINK_SEARCH_TERMS,
            location="the footer",
        )
