from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage
from pages.gear_page.urls import GEAR_PAGE


class GearPage(BasePage):
    # page with categories

    def __init__(self, driver):
        super().__init__(url=GEAR_PAGE,driver=driver)


   
