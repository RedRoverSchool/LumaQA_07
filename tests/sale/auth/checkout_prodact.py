'''TC_011.006.02.05 | Shop Tees >Tees>checkout_prodact'''

from selenium.webdriver.common.by import By
from pages.checkout_page import CheckoutPage


def test_checkout_prodact(driver, login_form, choice_sale, choice_tees_on_sale, choice_prodact, add_prodact):
    page = CheckoutPage(driver, url=CheckoutPage.URL)
    page.open()
    # todo implement these three
    # page.checkout_step_shipping()
    # page.shipping_methods()
    # page.checkout_order_summary()

    shipping_page = driver.find_element(By.CSS_SELECTOR, '#shipping')
    assert shipping_page

    order_summary = driver.find_element(By.XPATH, '//strong[contains(text(), "Tiffany Fitness Tee")]')
    assert order_summary
