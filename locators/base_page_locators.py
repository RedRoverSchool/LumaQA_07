from selenium.webdriver.common.by import By


class BasePageLocators:
    HEADER = (By.CSS_SELECTOR, 'h1 span')
    MSG_ERROR = (By.CSS_SELECTOR, '[data-ui-id="message-error"]')
    MSG_SUCCESS = (By.CSS_SELECTOR, '[data-ui-id="message-success"]')
