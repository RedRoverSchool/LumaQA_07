from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators
from locators.item_page_locators import ItemPageLocators



class MainPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/'

    def check_visibility_the_title(self):
        return self.is_visible(BasePageLocators.LOGO_TITLE)

    def check_visibility_of_erin_recommends_widget(self):
        return self.is_visible(BasePageLocators.ERIN_SECTION)

    def check_clickability_of_erin_recommends_widget(self):
        return self.is_clickable(BasePageLocators.ERIN_SECTION)

    def add_clamber_watch_from_gear_catalog_to_cart(self):
        self.hold_mouse_on_element(BasePageLocators.LINK_GEAR)
        self.is_clickable(BasePageLocators.LINK_GEAR_WATCHES).click()
        self.hold_mouse_on_element(ItemPageLocators.LINK_CLAMBER_WATCH)
        self.is_clickable(ItemPageLocators.ADD_TO_CART_CLAMBER_WATCH_BUTTON).click()
        self.is_visible(BasePageLocators.MSG_SUCCESS)

    def scroll_down_to_shop_erin_recom(self):
        self.scroll_to_element(BasePageLocators.SHOP_ERIN_RECOMMENDS)

    def men_btn_catalog(self):
        return self.is_clickable(BasePageLocators.LINK_MEN)

    def select_tops_from_mens_dropdown_menu(self):
        self.hold_mouse_on_element(BasePageLocators.LINK_MEN)
        self.is_clickable(BasePageLocators.LINK_MEN_TOPS)

    def select_bottoms_from_mens_dropdown_menu(self):
        self.hold_mouse_on_element(BasePageLocators.LINK_MEN)
        self.is_clickable(BasePageLocators.LINK_MEN_BOTTOMS)

    def visibility_of_men_tops_secondary_dropdown_menu(self):
        self.hold_mouse_on_element(BasePageLocators.LINK_MEN_TOPS)
        return self.is_visible(BasePageLocators.LINK_MEN_TOPS_JACKETS)

    def visibility_of_men_bottoms_secondary_dropdown_menu(self):
        self.hold_mouse_on_element(BasePageLocators.LINK_MEN_BOTTOMS)
        return self.is_visible(BasePageLocators.LINK_MEN_BOTTOMS_PANTS)

    def scroll_down_to_shop_performance(self):
        self.scroll_to_element(BasePageLocators.SHOP_PERFORMANCE)

    def check_images_boxes_on_page(self):
        results = []
        for block_selector in BasePageLocators.LIST_IMAGES:
            block_present = self.is_visible(block_selector)
            results.append(block_present)
        return results

    def scroll_down_to_shop_eco_friendly(self):
        self.scroll_to_element(BasePageLocators.SHOP_ECO_FRIENDLY)

