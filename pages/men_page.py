from base.seleniumbase import BasePage
from locators.men_page_locators import MenPageLocators


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
