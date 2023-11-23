from selenium.webdriver import ActionChains

from base.seleniumbase import BasePage
from locators.lumas_latest_page_locators import LumasPageLocators


class LumasPage(BasePage):
    def find_lumas(self):
        return self.is_visible(LumasPageLocators.Lumas_Latest)

    def find_lumas_just(self):
        return self.is_visible(LumasPageLocators.Just_in_Time).text

    def find_elements_lumas(self):
        item_list = self.is_visible_all_elements(LumasPageLocators.Item_List)
        # for item in item_list:
        #     print(item.text)

    def hold_mou_on_elementse_img(self):
        ActionChains(self.driver).move_to_element(self.is_visible(LumasPageLocators.IMG)).perform()

    def find_add_button_cart(self):
        return self.is_visible(LumasPageLocators.Add_to_Cart).text

    def find_add_wish(self):
        return self.is_visible(LumasPageLocators.Image_of_Wish).text

    def find_add_compare(self):
        return self.is_visible(LumasPageLocators.Image_of_Compare).text
