from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from base.seleniumbase import BasePage
from locators.wish_list_locators import WishListLocators
from pages.wish_list_page import WishListPage


class TestWishList:

    def test_visibility_items_left_corner(self, driver, open_main_page, sign_in, add_items_to_wish_list):
        wait(driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located(WishListLocators.WISH_LIST_SIDEBAR_ITEMS))
        wish_list_elements = driver.find_elements(*WishListLocators.WISH_LIST_SIDEBAR_ITEMS)
        wish_list = [element.text for element in wish_list_elements]
        assert len(wish_list) >= 1, "Items not found"

    def test_share_wish_list_button_is_working(self, driver, open_main_page, sign_in, add_items_to_wish_list):
        page = WishListPage(driver, url="https://magento.softwaretestingboard.com/wishlist/")
        page.click_share_wish_list_button()
        page.fill_email_field("not@gmail.com")
        page.fill_message_field("asdfasdfasdf")
        page.click_share_wish_list_button()
        assert page.message == 'Your wish list has been shared.'
