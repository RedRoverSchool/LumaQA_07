'''TC_011.006.02.04 | Shop Tees >Tees>add.prodact'''

from selenium.webdriver.common.by import By
from pages.sale_page import TeesPageProdact
from data.sale_page import CHECKOUT_PAGE


def test_add_prodact(driver, login_form, choice_sale, choice_tees_on_sale, choice_prodact):
    page = TeesPageProdact(driver, url=TeesPageProdact.URL)
    page.open()
    page.check_visibility_basket()
    page.check_clickability_basket()

    basket = driver.find_element(By.CSS_SELECTOR, 'a[class="action showcart"]')
    basket.click()

    basket_cart = driver.find_element(By.XPATH, '//a[contains(text(), "Tiffany Fitness Tee")]')
    assert basket_cart

    proceed_to_checkout_button = driver.find_element(By.CSS_SELECTOR, 'div button[id="top-cart-btn-checkout"]')
    proceed_to_checkout_button.click()

    assert CHECKOUT_PAGE
