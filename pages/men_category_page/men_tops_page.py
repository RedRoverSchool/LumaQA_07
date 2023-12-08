from base.seleniumbase import BasePage
from locators.men_tops_page_locators import MenTopsPageLocators
from locators.men_page_locators import MenPageLocators, MenCategoryPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class MenTops(BasePage):
    locator = MenCategoryPageLocators()

    def check_clickability_grid(self):
        return self.is_clickable(MenPageLocators.MEN_TOPS_GRID)

    def click_men_tops_product_foto(self):
        return self.is_clickable(MenTopsPageLocators.TOP_MEN_PRODUCT_FOTO).click()

    def click_men_tops_product_title(self):
        return self.is_clickable(MenTopsPageLocators.TOP_MEN_PRODUCT_TITLE).click()

    def check_visibility_grid(self):
        return self.is_visible(MenPageLocators.MEN_TOPS_GRID)

    def hover_to_cart(self, position):
        cart = self.is_visible(MenCategoryPageLocators.get_position_cart(position))
        self.action_move_to_element(cart)
        # time.sleep(2)

    def check_button(self, position):
        button = self.is_visible(MenCategoryPageLocators.get_position_button(position))
        button.click()

    def wait_url(self, url, timeout: int = 5):
        wait(self.driver, timeout).until(EC.url_to_be(url))

    def click_image(self, position):
        image = self.is_clickable(MenCategoryPageLocators.get_product_image(position))
        image.click()

    def mode_list_is_visible(self):
        return self.is_visible(MenCategoryPageLocators.LIST_MODE)

    def mode_list_is_clickable(self):
        return self.is_clickable(MenCategoryPageLocators.LIST_MODE)

    def list_page_view(self):
        """ Начальный вид страницы; классы элементов до применения фильтра"""
        view_before = self.driver.page_source
        self.find_element_and_click(MenCategoryPageLocators.LIST_MODE)
        after_filter = self.driver.page_source
        return view_before, after_filter

