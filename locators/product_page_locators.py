from selenium.webdriver.common.by import By

class ProductPageLocators:

    # Product page
    HEADER = (By.XPATH, "//header[@class='page-header']")
    NAVIGATION_SECTION = (By.XPATH, "//div[@class='sections nav-sections']")
    BREADCRUMBS = (By.XPATH, "//div[@class='breadcrumbs']")
    BODY = (By.XPATH, "//main[@id='maincontent']")
    FOOTER = (By.XPATH, "//footer[@class='page-footer']")
    COPYRIGHT = (By.XPATH, "//small[@class='copyright']")
    PRODUCT_QUANTITY = (By.XPATH, '//input[@id="qty"]')

    # Product page body
    MAIN_INFO = (By.XPATH, "//div[@class='product-info-main']")
    PICTURES = (By.XPATH, "//div[@class='product media']")
    DETAILED_INFO = (By.XPATH, "//div[@class='product info detailed']")
    RELATED_PRODUCTS = (By.XPATH, "//div[@class='block related']")
    LIKED_PRODUCTS = (By.XPATH, "//div[@class='block upsell']")
    RELATED_PRODUCTS_HEADING = (By.ID, "block-related-heading")

    # class="product-info-main"
    PRODUCT_NAME = (By.XPATH, "//span[@itemprop='name']")
    RATING_BLOCK = (By.XPATH, "//div[@class = 'product-reviews-summary']")
    PRICE_BLOCK = (By.XPATH, "//span[@id = 'product-price-1812'] ")
    AVAILABILITY_BLOCK = (By.XPATH, "//div[@class = 'stock available'] ")

    # class="product media"

    # class="product info detailed"


    # class="block upsell"

    ADD_TO_BLOCK = (By.XPATH, "//div[@class = 'product-addto-links']")