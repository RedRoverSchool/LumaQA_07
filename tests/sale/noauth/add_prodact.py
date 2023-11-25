'''TC_011.006.02.04.01 | Shop Tees >Tees>add.prodact'''

from selenium.webdriver.common.by import By
from pages.sale_page import TeesPage


def test_add_prodact(driver, choice_sale, choice_tees_on_sale, choice_prodact):
    page = TeesPage(driver, url=TeesPage.URL)
    page.open()
    # todo add this function
    page.check_visibility_cart_prodact()

    add_to_card = driver.find_element(By.CSS_SELECTOR, '#product-addtocart-button')
    add_to_card.click()

    basket = driver.find_element(By.CSS_SELECTOR, 'a[class="action showcart"]')
    basket.click()

    basket_cart = driver.find_element(By.XPATH, '//a[contains(text(), "Tiffany Fitness Tee")]')
    assert basket_cart

    proceed_to_checkout_button = driver.find_element(By.CSS_SELECTOR, 'div button[id="top-cart-btn-checkout"]')
    proceed_to_checkout_button.click()
