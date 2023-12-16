from selenium.webdriver.common.by import By

class PriceTabLocators:
    PRICE_TAB = (By.XPATH,'//div[@class="filter-options-title" and text()="Price"]')
    PRICE_LIST = (By.XPATH,'//div[@style="display: block;"]/ol[@class="items"]/li/a')
    PRICE_TITLES_LOCATOR = (By.XPATH, ".//span[@class='price']")
    SIDEBAR_MAIN = (By.XPATH,'//div[@class="sidebar sidebar-main"]')
    NOW_SHOPPING_BY_TITLE = (By.XPATH,'.//strong[@class="block-subtitle filter-current-subtitle"]')
    PRICE_LEVEL_AFTER_FILTER = (By.XPATH,'.//span[@class="filter-value"]')

class Items:
    PRODUCT_ITEM_INFO = (By.XPATH,'//div[@class="product-item-info"]')
    ITEM_REVIEWS = (By.XPATH,'.//div[@class="reviews-actions"]//span')
    ITEM_NAME = (By.XPATH,'.//a[@class="product-item-link"]')
    ITEM_IMG = (By.XPATH,'.//img[@class="product-image-photo"]')
    ITEM_COLORS = (By.XPATH,'.//div[@aria-label="Color"]')