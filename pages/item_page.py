import math
from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators
from locators.item_page_locators import ItemPageLocators
from locators.item_page_locators import ItemPageReviewsLocators


class ItemPage(BasePage):
    URL_DRIVEN_BACKPACK = "https://magento.softwaretestingboard.com/driven-backpack.html"
    URL_PUSH_IT_MESSENGER_BAG = "https://magento.softwaretestingboard.com/push-it-messenger-bag.html"
    URL_HARMONY_LUMAFLEX_STRENGTH_BAND_KIT = "https://magento.softwaretestingboard.com/harmony-lumaflex-trade-strength-band-kit.html"
    URL_PURSUIT_LUMAFLEX_TONE_BAND = "https://magento.softwaretestingboard.com/pursuit-lumaflex-trade-tone-band.html"
    URL_LUCIA_CROSS_FIT_BRA = "https://magento.softwaretestingboard.com/lucia-cross-fit-bra.html"
    URL_HERA_PULLOVER_HOODIE = "https://magento.softwaretestingboard.com/hera-pullover-hoodie.html"

    def enter_quantity_items(self, quantity):
        self.is_clickable(ItemPageLocators.QUANTITY_OF_ITEM).clear()
        return self.is_clickable(ItemPageLocators.QUANTITY_OF_ITEM).send_keys(quantity)

    def add_driven_backpack_from_item_card_to_cart(self, quantity: int = 1):
        '''МОЖНО УКАЗАТЬ КОЛИЧЕСТВО И ДОБАВИТЬ СРАЗУ НЕСКОЛЬКО'''
        self.enter_quantity_items(quantity)
        self.is_clickable(ItemPageLocators.ADD_TO_CART_BUTTON).click()
        self.is_visible(BasePageLocators.MSG_SUCCESS)

    def item_name(self):
        return self.is_visible(ItemPageLocators.ITEM_NAME)

    def item_sku_number(self):
        return self.is_visible(ItemPageLocators.ITEM_SKU_NUMBER)

    def item_review_count(self):
        return int(self.is_visible(ItemPageLocators.ITEM_REVIEW_COUNT).text)

    def item_review(self):
        return self.is_clickable(ItemPageLocators.ITEM_REVIEW_LINK)

    def customer_review_header(self):
        return self.is_visible(ItemPageLocators.CUSTOMER_REVIEWS_HEADER)

    def item_rating(self):
        return int(self.is_visible(ItemPageLocators.ITEM_RATING).get_attribute('title').split('%')[0])

    def add_your_review_link(self):
        return self.is_clickable(ItemPageLocators.ADD_YOUR_REVIEW_LINK)

    def block_review_add(self):
        return self.is_visible(ItemPageLocators.BLOCK_REVIEW_ADD)

    def get_customer_review(self, number_of_review):
        return self.is_visible((By.XPATH,
                                f"(//div[@class = 'review-ratings']//div[@class='rating-result'])[{number_of_review}]")).get_attribute(
            'title')

    def get_overall_rating(self, count):
        overall_rating = 0
        for i in range(1, count + 1):
            overall_rating += int((self.get_customer_review(i).split('%'))[0])
        return math.ceil(overall_rating / count)


class ItemPageJackets(BasePage):
    URL = 'https://magento.softwaretestingboard.com/olivia-1-4-zip-light-jacket.html'
    HEADER_RELATED_PRODUCTS = (By.CSS_SELECTOR, '#block-related-heading')
    RELATED_ITEM = (By.CSS_SELECTOR, '.product-item')

    def header_related(self):
        return self.is_visible(self.HEADER_RELATED_PRODUCTS).text

    def related_item(self):
        return self.item_count(self.RELATED_ITEM)


class ItemReviews(BasePage):

    def tab_reviews(self):
        return self.is_clickable(ItemPageReviewsLocators.TAB_REVIEWS)

    def rating_star(self):
        return self.hold_mouse_on_element_and_click(ItemPageReviewsLocators.RATING_STAR)

    def nick_name(self, value):
        return self.clear_and_send_keys(self.is_visible(ItemPageReviewsLocators.NICKNAME_FIELD), value)

    def summary(self, value):
        return self.clear_and_send_keys(self.is_visible(ItemPageReviewsLocators.SUMMARY_FIELD), value)

    def review(self, value):
        return self.clear_and_send_keys(self.is_visible(ItemPageReviewsLocators.REVIEW_FIELD), value)

    def submit_review_button(self):
        return self.is_clickable(ItemPageReviewsLocators.SUBMIT_REVIEW_BUTTON)








