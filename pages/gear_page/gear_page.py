from base.seleniumbase import BasePage
from data.gear_page_urls import GEAR_PAGE
from selenium.webdriver.remote.webelement import WebElement
from pages.gear_page import category_page
from locators.gear_page_locators import GearPageLocators


class GearPage(BasePage):
    def __init__(self, driver):
        super().__init__(url=GEAR_PAGE, driver=driver)

    def find_sidebar(self) -> WebElement:
        return self.is_visible(locator=GearPageLocators.SIDEBAR_MAIN)

    def find_element_in_sidebar(self, locator: tuple) -> WebElement:
        sidebar = self.find_sidebar()
        return self.find_visible_element_in_sidebar(sidebar, *locator)

    def find_elements_in_sidebar(self, locator: tuple) -> list[WebElement]:
        sidebar = self.find_sidebar()
        return self.find_visible_elements_in_sidebar(sidebar, locator)

    def find_visible_element_in_sidebar(
        self, sidebar: WebElement, *locator
    ) -> WebElement:
        return sidebar.find_element(*locator)

    def find_visible_elements_in_sidebar(
        self, sidebar: WebElement, locator: tuple
    ) -> list[WebElement]:
        return sidebar.find_elements(*locator)

    def find_category_counter_and_url(
        self, category_xpath: tuple, counter_xpath: tuple
    ):
        category = self.is_visible(locator=category_xpath)
        category_counter = self.is_visible(locator=counter_xpath).text
        return category, category.text, category_counter, category.get_attribute("href")

    def rederect_to_the_current_category_page(
        self, category: WebElement, category_url: str
    ) -> WebElement:
        category.click()
        self.redirect(url=category_url)
        return category_page.CategoryPage(driver=self.driver, url=category_url)
