import pytest
from selenium.webdriver.common.by import By
from pages.sale_page import SalePage, TeesPage
from pages.main_page import MainPage
import time


@pytest.fixture()
def choice_sale(driver):
    page = MainPage(driver, url=MainPage.URL)
    page.open()
    page.check_visibility_the_title()
    page.check_visibility_of_sale_section()
    page.check_clickability_of_sale_section()

    section_button = driver.find_element(By.CSS_SELECTOR, '#ui-id-8')
    section_button.click()

    text_name_page = driver.find_element(By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
    assert text_name_page


@pytest.fixture()
def choice_tees_on_sale(driver, choice_sale):
    page = SalePage(driver, url=SalePage.URL)
    page.open()
    page.check_visibility_of_Tees_on_sale()
    page.check_clickability_of_Tees_on_sale()

    widget_button = driver.find_element(By.XPATH, '//*[contains(text(), "Tees on sale")]')
    widget_button.click()

    text_name_page = driver.find_element(By.CSS_SELECTOR, 'h1[id="page-title-heading"]')
    assert text_name_page


@pytest.fixture()
def choice_prodact(driver, choice_sale, choice_tees_on_sale):
    page = TeesPage(driver, url=TeesPage.URL)
    page.open()

    widget_button = driver.find_element(By.XPATH, '//*[contains(text(), "Tiffany Fitness Tee")]')
    widget_button.click()

    card = driver.find_element(By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]')
    assert card
    time.sleep(3)

    size = driver.find_element(By.CSS_SELECTOR, 'div[id="option-label-size-143-item-167"]')
    size.click()
    time.sleep(3)

    color = driver.find_element(By.CSS_SELECTOR, 'div[id="option-label-color-93-item-58"]')
    color.click()
    time.sleep(3)

    text_name_page = driver.find_element(By.CSS_SELECTOR,
                                         'div[id="option-label-size-143-item-167"]' and 'div[id="option-label-color'
                                                                                        '-93-item-58"]')
    assert text_name_page
    time.sleep(3)


@pytest.fixture()
def add_prodact(driver, choice_sale, choice_tees_on_sale, choice_prodact):
    add_to_card = driver.find_element(By.CSS_SELECTOR, '#product-addtocart-button')
    add_to_card.click()
    time.sleep(3)

    basket = driver.find_element(By.CSS_SELECTOR, 'a[class="action showcart"]')
    basket.click()
    time.sleep(3)

    basket_cart = driver.find_element(By.XPATH, '//a[contains(text(), "Tiffany Fitness Tee")]')
    assert basket_cart
    time.sleep(3)


@pytest.fixture()
def checkout_prodact(driver, choice_sale, choice_tees_on_sale, choice_prodact, add_prodact):
    proceed_to_checkout_button = driver.find_element(By.CSS_SELECTOR, 'div button[id="top-cart-btn-checkout"]')
    proceed_to_checkout_button.click()
    time.sleep(3)

    shipping_page = driver.find_element(By.CSS_SELECTOR, '#shipping')
    assert shipping_page
    time.sleep(3)

    order_summary = driver.find_element(By.XPATH, '// strong[contains(text(), "Tiffany Fitness Tee")]')
    assert order_summary
    time.sleep(3)







