from selenium.webdriver.common.by import By


class AdvancedSearchResultsLocators:
    ERROR_MESSAGE_ON_ADVANCED_SEARCH_RESULTS_PAGE = (By.CSS_SELECTOR, '.message.error')
    PRODUCT_CARD_NAMES = (By.CSS_SELECTOR, '.product-item-link')
    MESSAGE_HOW_MANY_ITEMS_FOUND = (By.CSS_SELECTOR, '.search.found')
    MESSAGE_NUMBER_OF_ITEMS = (By.CSS_SELECTOR, '.toolbar-products:nth-of-type(1) > .toolbar-amount')
    LIST_OF_SIZES = (By.CSS_SELECTOR, '.swatch-option.text')
