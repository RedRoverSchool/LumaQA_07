from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import BasePage
from pages.main_page import MainPage
from locators.footer_locators import FooterLocators


class FooterPage(BasePage):
    locators = FooterLocators()
    URL = MainPage.URL

    def check_visibility_advanced_search_link(self):
        return self.is_visible(self.locators.ADVANCED_SEARCH_LINK)
    
