from selenium.webdriver.common.by import By


# TRAINING_PAGE_LOCATORS
class TrainingPageLocators:
    TRAINING_MENU = (By.XPATH, "//a[@id='ui-id-7']/span[last()]")
    TRAINING_TEXT = (By.CSS_SELECTOR, "#page-title-heading span")
    SHOP_BY_TEXT = (By.CSS_SELECTOR, "div[class='title'] strong")
    VIDEO_DOWNLOAD = (By.CSS_SELECTOR, "li[class='item'] a")
    COMPARE_PRODUCTS_TEXT = (By.CSS_SELECTOR, "#block-compare-heading")
    MY_WISH_LIST_TEXT = (By.CSS_SELECTOR, "div[class='block block-wishlist'] strong[role='heading']")
    BLOCK1 = (By.XPATH, "//a[@class='block-promo training-main']")
    BLOCK1_TEXT = (By.CSS_SELECTOR, "a[class='block-promo training-main'] span[class='content']")
    BLOCK1_IMG = (By.CSS_SELECTOR, "a[class='block-promo training-main'] img")
    BLOCK2 = (By.XPATH, "//a[@class='block-promo training-erin']")
    BLOCK2_TEXT_1 = (By.XPATH, "//a[@class='block-promo training-erin']//strong[@class='title']")
    BLOCK2_TEXT_2 = (By.XPATH, "//a[@class='block-promo training-erin']//span[@class='info']")
    BLOCK3 = (By.XPATH, "//a[@class='block-promo training-on-demand']")
    BLOCK4 = (By.XPATH, "//div[@class='content-heading']")
