from selenium.webdriver.common.by import By


class MenTopsPageLocators:
    TOP_MEN_PRODUCT_FOTO = (By.CSS_SELECTOR, "a[class='product photo product-item-photo'] img[alt='Cassius Sparring Tank']")
    TOP_MEN_PRODUCT_TITLE = (By.XPATH, "//div[@class = 'product details product-item-details']//a[contains(text(), 'Cassius')]")
    # PAGE_NAME = (By.TAG_NAME, "h1")
