'''TC_011.006.02.02.01 | Shop Tees>Tees>choice_tees_on_sale'''

from selenium.webdriver.common.by import By
from pages.sale_page import SalePage


def test_choice_tees_on_sale(driver, choice_sale):
    page = SalePage(driver, url=SalePage.URL)
    page.open()
    page.check_visibility_of_Tees_on_sale()
    page.check_clickability_of_Tees_on_sale()

    widget_button = driver.find_element(By.XPATH, '//*[contains(text(), "Tees on sale")]')
    widget_button.click()

    text_name_page = driver.find_element(By.CSS_SELECTOR, 'h1[id="page-title-heading"]')
    assert text_name_page
