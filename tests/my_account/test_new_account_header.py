from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_new_account_header():
    """TC__004.003.009 | Authorization > check page title"""
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
    header_text = driver.find_element(By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]').text
    assert header_text == 'Create New Customer Account'