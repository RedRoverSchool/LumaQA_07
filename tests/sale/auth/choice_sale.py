'''TC_011.006.02.01 | Sale'''

from selenium.webdriver.common.by import By
from pages.login.login_page import MyAccountPage


def test_choice_sale(driver, login_form):
    page = MyAccountPage(driver, url=MyAccountPage.URL)
    page.open()
    page.check_visibility_of_sale_section()
    page.check_clickability_of_sale_section()

    section_button = driver.find_element(By.XPATH, '//a[@id="ui-id-8"]')
    section_button.click()

    text_name_page = driver.find_element(By.XPATH, '//span[@data-ui-id="page-title-wrapper"]')
    assert text_name_page


