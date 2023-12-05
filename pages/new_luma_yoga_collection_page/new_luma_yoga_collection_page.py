import time
from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage
from locators.new_luma_yoga_collection_locators import PriceTabLocators 
from selenium.webdriver.remote.webelement import WebElement



class NewLumaYogaCollectionPage(BasePage):

    def __init__(self, driver):
        super().__init__(
            url='https://magento.softwaretestingboard.com/collections/yoga-new.html',
            driver=driver
        )
    def find_price_tab(self) -> WebElement:
        return self.is_visible(locator=PriceTabLocators.PRICE_TAB,timeout=20)
    

    def find_price_list(self, locator: tuple) -> list[WebElement]:
        return self.driver.find_elements(*locator)
    
    def find_sidebar(self) -> WebElement:
        return self.is_visible(locator=PriceTabLocators.SIDEBAR_MAIN)
    

    def find_price_level_after_filter(self) -> str:
        side_bar = self.find_sidebar()
        return side_bar.find_element(*PriceTabLocators.PRICE_LEVEL_AFTER_FILTER).text
    
    def find_title_now_shoping_by(self) -> str:
        side_bar = self.find_sidebar()
        return side_bar.find_element(*PriceTabLocators.NOW_SHOPPING_BY_TITLE).text