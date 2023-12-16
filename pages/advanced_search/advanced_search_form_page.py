from base.seleniumbase import BasePage
from locators.advanced_search_locators import AdvancedSearchLocators as locator
from locators.advanced_search_locators import AdvancedSearchLocators



class AdvancedSearchFormPage(BasePage):
    QUERY_LIST = ['top', 'bottom', 'capri', 'short', 'tank', 'watch', 'sweatshirt', 'pant', 'hoodie']
    CLOTHES_LIST = ['top', 'bottom', 'jacket', 'short', 'tank', 'sweatshirt', 'pant', 'hoodie']

    def __init__(self, driver,url):
        super().__init__(driver, url)
        self.current_url = url

    def enter_product_name(self, string):
        self.driver.find_element(*locator.PRODUCT_NAME_TEXTBOX).send_keys(string)

    def click_search(self):
        self.driver.find_element(*locator.SEARCH_BUTTON).click()

    def get_list_of_item_titles(self):
        title_element_list = self.is_visible_all_elements(locator.ITEM_CARD_TITLES)
        title_list = []
        for title_element in title_element_list:
            title_list.append(title_element.text)
        return title_list

    def button_clickable(self):
        return self.is_clickable(locator.SEARCH_BUTTON)

    def button_visible(self):
        return self.is_visible(locator.SEARCH_BUTTON)

    def get_search_fields_list(self):
        return self.is_visible_all_elements(locator.SEARCH_FIELDS_LIST)

    def clear_all_search_fields(self):
        [field.clear() for field in self.get_search_fields_list()]

    def get_error_message(self):
        return self.is_visible(locator.ERROR_MESSAGE_ON_ADVANCED_SEARCH_PAGE).text.strip()

    def visibility_of_size_options(self):
        return self.is_visible_all_elements(locator.SIZE_OPTIONS)

    def visibility_of_color_options(self):
        return self.is_visible_all_elements(locator.COLOR_OPTIONS)
      
