import locators.product_page_locators
from pages.product_page.product_main_info import ProductPage
from data.product_page_data import PRODUCT_PAGE_EXAMPLE
from locators.product_page_locators import ProductPageLocators
from locators.base_page_locators import BasePageLocators as BP
from data.home_page_url import HOME_PAGE
from pages.account.sign_in import SignInPage
from locators.product_page_locators import ProductPageLocators as loc
from tests.login.test__sign_in import TestX


class TestProductPage:

    def test_check_product_name_in_main_info(self, driver):
        """TC_002.005.001"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        text = page.check_product_name_in_main_info()
        assert text == "Breathe-Easy Tank"

    def test_rating_block_is_visible(self, driver):
        """TC_002.005.002"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        assert page.rating_block_is_visible()

    def test_price_block_is_visible(self, driver):
        """TC_002.005.003"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        assert page.price_block_is_visible()

    def test_add_to_block_is_visible(self, driver):
        """TC_002.005.009/1"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        assert page.product_add_to_block_is_visible()

    def test_availability_block_is_displayed(self, driver):
        """TC_002.005.004"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        assert page.availability_block_is_displayed(), "Availability is not displayed"

    def test_clickability_add_to_cart(self, driver):
        """TC_002.015.002"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        page.choose_size()
        page.choose_color()
        page.click_add_to_cart()

        assert page.counter_number_is_visible(), "'Add to cart' button is not clickability"

    def test_add_to_wish_list_is_visible(self, driver):
        """TC_002.016.002"""
        TestX.test_correct_credentials_login(self, driver)
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        assert page.visible(ProductPageLocators.ADD_WISH_ELEMENT), "Element 'Add to wish list' is invisible"

    def test_main_logo_redirect_to_main_page(self, driver):
        """TC_003.001.002"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        page.visible(BP.LOGO_TITLE).click()
        assert driver.current_url == HOME_PAGE
        # assert page.visible(loc.ADD_WISH_ELEMENT), "Element 'Add to wish list' is invisible"

    def test_add_to_wish_list_is_clickable(self, driver):
        """TC_002.016.001"""
        TestX.test_correct_credentials_login(self, driver)
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        page.visible(loc.ADD_WISH_ELEMENT).click()
        assert driver.find_element(*loc.NAME_OF_WISH_LIST).text == "My Wish List"

    def test_size_choice_block_is_displayed(self, driver):
        """TC_002.005.005"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        assert page.size_choice_block_is_displayed(), "Size choice block is not displayed"

    def test_color_choice_block_is_displayed(self, driver):
        """TC_002.005.006"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        assert page.color_choice_block_is_displayed(), "Color choice block is not displayed"

    def test_quantity_color_choice_block_is_displayed(self, driver):
        """TC_002.005.007"""
        page = ProductPage(driver, PRODUCT_PAGE_EXAMPLE)
        page.open()
        assert page.quantity_choice_block_is_displayed(), "Quantity choice block is not displayed"
