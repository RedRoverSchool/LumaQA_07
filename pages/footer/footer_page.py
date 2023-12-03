from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By


class FooterPage(BasePage):
    locators = BasePageLocators()

    def check_visibility_advanced_search_link(self):
        """This method verifies if the advanced search link is visible on the footer"""
        return self.is_visible(self.locators.LINK_ADVANCED_SEARCH)

    def check_clickability_advanced_search_link(self):
        """This method verifies if the advanced search link is clickable"""
        return self.is_clickable(self.locators.LINK_ADVANCED_SEARCH)

    def click_advanced_search_link(self):
        """This method clicks on the advanced search link"""
        self.check_clickability_advanced_search_link().click()


    def check_visibility_footer_diabled_link(self):
        """This method heck if an element with <strong> tag in footer is visible"""
        return self.is_visible(self.locators.LINK_DISABLED)

    def chech_visibility_footer_sign_in_link(self):
        return self.is_visible(BasePageLocators.LINK_HEADER_SIGN_IN).click()
