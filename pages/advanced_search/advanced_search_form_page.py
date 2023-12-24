from base.seleniumbase import BasePage
from locators.advanced_search_locators import AdvancedSearchLocators as locators


class AdvancedSearchFormPage(BasePage):
    QUERY_LIST = ['top', 'bottom', 'capri', 'short', 'tank', 'watch', 'sweatshirt', 'pant', 'hoodie']
    CLOTHES_LIST = ['top', 'bottom', 'jacket', 'short', 'tank', 'sweatshirt', 'pant', 'hoodie']

    def __init__(self, driver,url):
        super().__init__(driver, url)
        self.current_url = url

    def enter_product_name(self, string):
        self.driver.find_element(*locators.PRODUCT_NAME_TEXTBOX).send_keys(string)

    def click_search(self):
        self.driver.find_element(*locators.SEARCH_BUTTON).click()

    def get_list_of_item_titles(self):
        title_element_list = self.is_visible_all_elements(locators.ITEM_CARD_TITLES)
        title_list = []
        for title_element in title_element_list:
            title_list.append(title_element.text)
        return title_list

    def button_clickable(self):
        return self.is_clickable(locators.SEARCH_BUTTON)

    def button_visible(self):
        return self.is_visible(locators.SEARCH_BUTTON)

    def get_search_fields_list(self):
        return self.is_visible_all_elements(locators.SEARCH_FIELDS_LIST)

    def clear_all_search_fields(self):
        [field.clear() for field in self.get_search_fields_list()]

    def get_error_message(self):
        return self.is_visible(locators.ERROR_MESSAGE_ON_ADVANCED_SEARCH_PAGE).text.strip()

    def visibility_of_size_options(self):
        return self.is_visible_all_elements(locators.SIZE_OPTIONS)

    def visibility_of_color_options(self):
        return self.is_visible_all_elements(locators.COLOR_OPTIONS)

    def get_search_button_hex_background_color(self):
        """The method gets the 'Search' button hex background color value"""
        search_button = self.find_element(locators.SEARCH_BUTTON)

        return self.convert_rgb_color_to_hex(search_button.value_of_css_property("background"))

    def is_image_displayed(self, element):
        base_window = self.get_current_window_handle()

        # visibility #1 check
        try:
            self.is_element_visible(element, 3)
        except:
            print('not visible 1')
            return False

        # zero image size check
        if not element.size['width'] or not element.size['height']:
            print('no size')
            return False

        # visibility #2 check
        if not element.is_displayed():
            print('not visible 2')
            return False

        img_link = element.get_attribute('src')
        img_exts = self.IMAGE_EXTENSIONS

        # image link check
        if not any(img_link.endswith(ext) for ext in img_exts):
            print('no link')
            return False

        img_page_status = self.get_http_response(img_link)

        # img page response check
        if img_page_status != 200:
            print('no GET')
            return False

        self.driver.execute_script("window.open('about:blank', 'test_image_url_tab');")
        self.driver.switch_to.window('test_image_url_tab')
        self.driver.get(img_link)
        img_page_url = self.driver.current_url
        self.driver.close()
        self.driver.switch_to.window(base_window)

        # image page url check
        if not any(img_page_url.endswith(ext) for ext in img_exts):
            print('no url')
            return False

        return True

    def are_six_search_fields_visible(self):
        """The methods checks if the search fields are visible"""
        return self.are_dictionary_elements_visible(locators.SEARCH_FIELDS_TEXTBOXES)

    def is_multipage(self):
        pagination_list = self.driver.find_elements(*locators.PAGINATION)
        return len(pagination_list)

    def is_not_last_page(self):
        next_arrow_list = self.driver.find_elements(*locators.NEXT_PAGE_ARROW)
        return len(next_arrow_list)

    def click_next_page(self):
        self.is_clickable(locators.NEXT_PAGE_ARROW).click()

    def are_all_images_present(self):
        image_check_list = []
        missing_image_list = []
        image_elements = self.driver.find_elements(*locators.PRODUCT_ITEM_IMAGES)
        for image in image_elements:
            image_displayed = self.is_image_displayed(image)
            image_check_list.append(image_displayed)
            if not image_displayed:
                missing_image_list.append(image.get_attribute(('src')))
        return {'confirm': all(image_check_list), 'missing_images': list(missing_image_list)}
