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
        time.sleep(1)
        return self.is_visible(PriceTabLocators.PRICE_TAB)
    

    def find_price_list(self, locator: tuple) -> list[WebElement]:
        return self.driver.find_elements(*locator)
