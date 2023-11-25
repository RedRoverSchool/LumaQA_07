'''TC_011.006.02.05.01 | Shop Tees >Tees>checkout_prodact'''

from selenium.webdriver.common.by import By
from pages.checkout_page import CheckoutPage


def test_checkout_prodact(driver, choice_sale, choice_tees_on_sale, choice_prodact, add_prodact):
    page = CheckoutPage(driver, url=CheckoutPage.URL)
    page.open()
    # todo implement these two
    # page.checkout_step_shipping()
    # page.shipping_methods()

    shipping_page = driver.find_element(By.CSS_SELECTOR, '#shipping')
    assert shipping_page

    order_summary = driver.find_element(By.XPATH, '//div[@class="product-item-name-block"] /strong[contains(text(), "Tiffany Fitness Tee")]')
    assert order_summary

    message = driver.find_element(By.XPATH, '//span[contains(text(), "You can create an account after checkout.")]')
    assert message
