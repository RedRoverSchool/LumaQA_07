from selenium.webdriver.common.by import By


class MenTopsPageLocators:
    TOP_MEN_PRODUCT_FOTO = (By.CSS_SELECTOR, "a[class='product photo product-item-photo'] img[alt='Cassius Sparring Tank']")
    TOP_MEN_PRODUCT_TITLE = (By.XPATH, "//div[@class = 'product details product-item-details']//a[contains(text(), 'Cassius')]")
    TOP_MEN_SORTER = (By.CSS_SELECTOR, '.toolbar-products:nth-child(3) .sorter-options')
    TOP_MEN_PRODUCT_ITEMS_NAME = (By.CSS_SELECTOR, '.product-items .product-item-link')
    TOP_MEN_ARROW = (By.CSS_SELECTOR, ".toolbar-products:nth-child(3) .sort-asc")
    TOP_MEN_PRODUCT_ITEMS_PRICE = (By.CSS_SELECTOR, ".price-wrapper .price")
    TOP_MEN_LIST_MODE = (By.CSS_SELECTOR, ".toolbar-products:nth-child(3) .mode-list")
    # PAGE_NAME = (By.TAG_NAME, "h1")
