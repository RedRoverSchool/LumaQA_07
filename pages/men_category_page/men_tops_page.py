from base.seleniumbase import BasePage
from locators.men_tops_page_locators import MenTopsPageLocators
from locators.men_page_locators import MenPageLocators, MenCategoryPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

# from locators.men_tops_page_locators import MenTopsPageLocators


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
        self.is_visible(MenPageLocators.MEN_TOPS_LIST)




