from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators


class Header(BasePage):

    def check_logo_visibility(self):
        assert self.is_visible(BasePageLocators.LOGO_TITLE)

