'''TC_011.006.02.03 | Shop Tees >Tees>choice_prodact'''

from selenium.webdriver.common.by import By
from pages.sale_page import TeesPage
import time


def test_choice_prodact(driver, login_form, choice_sale, choice_tees_on_sale):
    page = TeesPage(driver, url=TeesPage.URL)
    page.open()
    page.check_visibility_products_list()
    page.check_clickability_products_list()

    widget_button = driver.find_element(By.XPATH, '//div[@class="product details product-item-details"] // a[contains(text(), "Tiffany Fitness Tee")]')
    widget_button.click()
    time.sleep(5)

    card = driver.find_element(By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]')
    assert card

    size = driver.find_element(By.CSS_SELECTOR, 'div[id="option-label-size-143-item-167"]')
    size.click()
    time.sleep(5)

    color = driver.find_element(By.CSS_SELECTOR, 'div[id="option-label-color-93-item-58"]')
    color.click()

    qty = driver.find_element(By.CSS_SELECTOR, 'input[id="qty"]' and 'input[value="1"]')
    assert qty

    add_to_card = driver.find_element(By.CSS_SELECTOR, 'button[id="product-addtocart-button"]')
    add_to_card.click()
    time.sleep(5)

    message = driver.find_element(By.XPATH, '//*[contains(text(), "You added Tiffany Fitness Tee to your")]')
    assert message
