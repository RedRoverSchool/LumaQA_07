from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators
from data.home_page_url import HOME_PAGE


class Header(BasePage):

    def check_logo_visibility(self):
        assert self.is_visible(BasePageLocators.LOGO_TITLE)

    def check_logo_redirection(self):
        assert self.current_url == HOME_PAGE, "Logo doesn't redirect to the main page!"

    def check_header_visibility(self):
        assert self.is_visible(BasePageLocators.HEADER_SEARCHBAR)