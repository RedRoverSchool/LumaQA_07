from selenium.webdriver.common.by import By


class AdvancedSearchLocators:
    PRODUCT_NAME_TEXTBOX = (By.CSS_SELECTOR, '#name')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.primary button.search')
    ITEM_CARD_TITLES = (By.CSS_SELECTOR, '.product-item-link')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.error')
