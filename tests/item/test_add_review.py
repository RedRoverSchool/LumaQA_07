import time

import pytest
from faker import Faker
from locators.item_page_locators import ItemPageReviewsLocators
from pages.item_page import ItemReviews


@pytest.mark.debug
def test_add_review(driver):
    page = ItemReviews(driver, url=ItemPageReviewsLocators.URL)
    page.open()
    page.tab_reviews().click()

    # page.nick_name(Faker().first_name())
    page.summary('Заголовок отзыва')
    page.review(Faker().text(150))
    page.nick_name(Faker().first_name())
    page.rating_star()
    page.submit_review_button().click()
    assert page.message_success == ItemPageReviewsLocators.SUCCESS_MESSAGE, 'Что-то пошло не так'






