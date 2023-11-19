from base.seleniumbase import BasePage
from locators.women_page_locators import WomenPageLocators


class WomenPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def click_tops_link(self):
        tops_link_locator = WomenPageLocators.TOP_WOMEN
        self.is_clickable(tops_link_locator).click()
