from base.seleniumbase import BasePage
from selenium.webdriver import ActionChains
from locators.performance_sportswear_locators import PerformanceSportsWearPageLocators




class PerformanceSportsWearPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/collections/performance-new.html'

    def hold_on_element(self):
        ActionChains(self.driver).move_to_element(
            self.is_visible(PerformanceSportsWearPageLocators.Element_of_Card)).perform()

    def find_button_add_wish(self):
        return self.is_visible(PerformanceSportsWearPageLocators.Button_Add_to_Wish).click()

    def go_to_page_customer(self):
        return self.is_visible(PerformanceSportsWearPageLocators.Page_Customer_Login).text

    def find_button_add_compare(self):
        return self.is_visible(PerformanceSportsWearPageLocators.Button_Add_to_Compare).click()
    def go_to_page_compare(self):
        return self.is_visible(PerformanceSportsWearPageLocators.Page_Checkbox_Compare).text

    def find_button_add_cart(self):
         return self.is_visible(PerformanceSportsWearPageLocators.Button_Add_to_Cart).click()


    def go_to_page_add_cart(self):
        return self.is_visible(PerformanceSportsWearPageLocators.Name_Product_After).text


