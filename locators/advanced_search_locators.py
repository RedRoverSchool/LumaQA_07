from selenium.webdriver.common.by import By


class AdvancedSearchLocators:
    PRODUCT_NAME_TEXTBOX = (By.CSS_SELECTOR, '#name')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.primary button.search')
    ITEM_CARD_TITLES = (By.CSS_SELECTOR, '.product-item-link')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.error')
    Product_Name=(By.CSS_SELECTOR,'.field.name')
    SKU=(By.CSS_SELECTOR,'.field.sku')
    Description=(By.CSS_SELECTOR,'.field.description')
    ShortDescription=(By.CSS_SELECTOR,'.field.short_description')
    Price=(By.CSS_SELECTOR,'.field.price span')
    USD = (By.CSS_SELECTOR,'.addafter')
    GRID = (By.XPATH,'//*[@id="mode-grid"]')
    LIST=(By.XPATH,'//*[@id="mode-list"]')
    ERROR_MESSAGE_ON_ADVANCED_SEARCH_PAGE = (By.CSS_SELECTOR, '.messages [data-bind$="(message.text)"]')
    SEARCH_FIELDS_LIST = (By.CSS_SELECTOR, '.fieldset input[title]')
    SIZE_OPTIONS = (By.CSS_SELECTOR, ".swatch-attribute.size")
    COLOR_OPTIONS = (By.CSS_SELECTOR, '.swatch-attribute.color')
    