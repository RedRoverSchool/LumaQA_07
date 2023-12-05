from selenium.webdriver.common.by import By

class PriceTabLocators:
    PRICE_TAB = (By.XPATH,'//div[@class="filter-options-title" and text()="Price"]')
    PRICE_LIST = (By.XPATH,'//div[@style="display: block;"]/ol[@class="items"]/li/a')
    PRICE_TITLES_LOCATOR = (By.XPATH, ".//span[@class='price']")
    SIDEBAR_MAIN = (By.XPATH,'//div[@class="sidebar sidebar-main"]')
    NOW_SHOPPING_BY_TITLE = (By.XPATH,'.//strong[@class="block-subtitle filter-current-subtitle"]')
    PRICE_LEVEL_AFTER_FILTER = (By.XPATH,'.//span[@class="filter-value"]')