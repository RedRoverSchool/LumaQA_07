from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from base.seleniumbase import BasePage


# driver = webdriver.Chrome()

def test_new_account_header(driver):
    """TC__004.003.009 | Authorization > check page title"""
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
    wait(driver, BasePage.TIMEOUT).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]')))
    header_text = driver.find_element(By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]').text
    assert header_text == 'Create New Customer Account'