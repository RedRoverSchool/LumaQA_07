import random
from base.seleniumbase import BasePage
from locators.men_page_locators import MenPageLocators, MenCategoryPageLocators as MenCPL


class MenPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/men.html'

    def select_tops_from_sidebar_menu(self):
        self.hold_mouse_on_element(MenPageLocators.TOPS_CATEGORY_LINK)
        self.is_clickable(MenPageLocators.TOPS_CATEGORY_LINK).click()

    def select_tops_from_men_dropdown(self):
        self.hold_mouse_on_element(MenPageLocators.MEN_DROPDOWN_BUTTON)
        self.is_clickable(MenPageLocators.TOPS_DROPDOWN_BUTTON).click()

    def select_jackets_from_tops_dropdown(self):
        self.hold_mouse_on_element(MenPageLocators.MEN_DROPDOWN_BUTTON)
        self.hold_mouse_on_element(MenPageLocators.TOPS_DROPDOWN_BUTTON)
        self.hold_mouse_on_element(MenPageLocators.SIDE_BAR_JACKETS)
        self.is_clickable(MenPageLocators.SIDE_BAR_JACKETS).click()

    def select_bottoms_from_men_dropdown(self):
        self.hold_mouse_on_element(MenPageLocators.MEN_DROPDOWN_BUTTON)
        self.is_clickable(MenPageLocators.BOTTOMS_DROPDOWN_BUTTON).click()

    def select_bottoms_from_sidebar_menu(self):
        self.hold_mouse_on_element(MenPageLocators.BOTTOMS_CATEGORY_LINK)
        self.is_clickable(MenPageLocators.BOTTOMS_CATEGORY_LINK).click()


class MenJacketsPage(BasePage):
    def random_choice_item(self):
        num_jackets = 11
        jacket_items = [MenCPL.create_item_list(i) for i in range(1, num_jackets + 1)]
        random_jacket = random.choice(jacket_items)
        self.hold_mouse_on_element(random_jacket)
        return random_jacket

    def check_all_button(self):
        inner_buttons = self.find_element(MenPageLocators.INNER_BUTTONS)
        return inner_buttons

    def check_redirect_page(self):
        self.find_element_and_click(MenPageLocators.LANDO_GYM_JACKET)

    def all_item(self):
        num_jackets = 11
        jacket_items = [MenCPL.create_item_list(i) for i in range(1, num_jackets + 1)]
        for item_selector in jacket_items:
            try:
                self.is_visible(item_selector)
            except Exception:
                return False, f'Item is not visible: {item_selector}'
            return True, 'All items are visible'

    def item_with_a_shadow(self):
        element = self.driver.find_element(*MenCPL.ITEM)
        box_shadow = element.value_of_css_property('box-shadow')
        return box_shadow == 'rgba(0, 0, 0, 0.3) 3px 4px 4px 0px'
