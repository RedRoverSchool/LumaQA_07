from selenium.webdriver.common.by import By


class WomenTopsPageLocators:
    TOP_WOMEN_PRODUCTS = (By.XPATH, "//div[@class='product-item-info']//span[@class='product-image-container']")
    TOP_WOMEN_PRODUCTS_CLICKABLE = (By.CSS_SELECTOR, ".product-item-name a")
    PAGE_NAME = (By.TAG_NAME, "h1")
