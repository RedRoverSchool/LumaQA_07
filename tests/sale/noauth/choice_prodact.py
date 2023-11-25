'''TC_011.006.02.02.01 | Shop Tees>Tees>choice_tees_on_sale'''
import time

from selenium.webdriver.common.by import By
from pages.sale_page import TeesPage


def test_choice_prodact(driver, choice_sale, choice_tees_on_sale):
    page = TeesPage(driver, url=TeesPage.URL)
    page.open()

    widget_button = driver.find_element(By.XPATH, '//*[contains(text(), "Tiffany Fitness Tee")]')
    widget_button.click()

    card = driver.find_element(By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]')
    assert card

    size = driver.find_element(By.CSS_SELECTOR, 'div[id="option-label-size-143-item-167"]')
    size.click()

    color = driver.find_element(By.CSS_SELECTOR, 'div[id="option-label-color-93-item-58"]')
    color.click()

    qty = driver.find_element(By.CSS_SELECTOR, 'input[id="qty"]' and 'input[value="1"]')
    assert qty

    text_name_page = driver.find_element(By.CSS_SELECTOR, 'div[id="option-label-size-143-item-167"]' and 'div[id="option-label-color-93-item-58"]')
    assert text_name_page

    add_to_card = driver.find_element(By.CSS_SELECTOR, 'button[id="product-addtocart-button"]')
    add_to_card.click()
    time.sleep(5)

    message = driver.find_element(By.XPATH, '//*[contains(text(), "You added Tiffany Fitness Tee to your")]')
    assert message
