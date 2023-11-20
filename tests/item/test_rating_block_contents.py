from faker import Faker
from locators.item_page_locators import ItemPageRatingLocators
from pages.item_page import ItemRatingBlock


def test_rating_block_contents(driver):
    page = ItemRatingBlock(driver, url=ItemPageRatingLocators.URL)
    page.open()
    page.item_antonia_racer_tank().click()
    page.link_reviews().click()
    page.block_customer_reviews()
    assert page.bar_stars_contents() == page.bar_stars(), 'Неправильно отображается рейтинг'
    assert page.link_reviews().get_attribute('href') == ItemPageRatingLocators.URL_REVIEWS, 'Не верный переход'
    assert page.link_add_your_reviews().get_attribute('href') == ItemPageRatingLocators.URL_ADD_YOUR_REVIEWS, 'Не верный переход'






