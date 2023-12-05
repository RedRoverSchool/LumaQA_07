from base.seleniumbase import BasePage
from data.gear_page_urls import GEAR_PAGE
from selenium.webdriver.remote.webelement import WebElement
from locators.base_page_locators import BasePageLocators
from pages.gear_page import category_page
from locators.gear_page_locators import GearPageLocators
from pages.gear_page.items import GearWatchEndurance, GearItem, GearWatchClamber


class GearPage(BasePage):
    def __init__(self, driver):
        super().__init__(url=GEAR_PAGE, driver=driver)

    def find_sidebar(self) -> WebElement:
        return self.is_visible(locator=GearPageLocators.SIDEBAR_MAIN)

    def find_element_in_sidebar(self, locator: tuple) -> WebElement:
        sidebar = self.find_sidebar()
        return sidebar.find_element(*locator)

    def find_elements_in_sidebar(self, locator: tuple) -> list[WebElement]:
        sidebar = self.find_sidebar()
        return [item for item in sidebar.find_elements(*locator) if item.is_displayed()]

    def find_category_counter_and_url(
        self, category_xpath: tuple, counter_xpath: tuple
    ):
        category = self.is_visible(locator=category_xpath)
        category_counter = self.is_visible(locator=counter_xpath).text
        return category, category.text, category_counter, category.get_attribute("href")

    def rederect_to_the_current_category_page(
        self, category: WebElement, category_url: str, category_name: str
    ) -> WebElement:
        category.click()
        self.redirect(url=category_url)
        assert (
                self.driver.current_url == category_url
            ), f"We reached wrong url - {self.driver.current_url}, but expected - {category_url}"
        assert (
                self.driver.title.split(" - ")[0] == category_name
            ), f"We reach {self.driver.title}, but Expected to be at {category_name} page"
        return category_page.CategoryPage(driver=self.driver, url=category_url)
    
    def find_shop_by_title_in_the_side_bar(self) -> str:
        shop_by_title = self.find_element_in_sidebar(locator=GearPageLocators.SHOP_BY_TITLE).text
        category_title = self.find_element_in_sidebar(locator=GearPageLocators.CATEGORY_TITLE).text
        return f"{shop_by_title} {category_title}"    


    def add_clamber_watch_from_gear_catalog_to_cart(self, quantity=1):
        self.add_gear_item_to_cart(GearWatchClamber(), quantity)

    def add_endurance_watch_from_gear_catalog_to_cart(self, quantity=1):
        self.add_gear_item_to_cart(GearWatchEndurance(), quantity)

    def add_gear_item_to_cart(self, item: GearItem, quantity: int):
        for _ in range(quantity):
            self.hold_mouse_on_element(item.nav_locator)
            self.is_clickable(item.nav_list_item_locator).click()
            self.hold_mouse_on_element(item.item_locator)
            self.is_clickable(item.add_to_cart_locator).click()
            self.is_visible(BasePageLocators.MSG_SUCCESS)
