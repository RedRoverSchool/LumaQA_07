from selenium.webdriver.common.by import By


class ItemPageLocators:
    ITEM_NAME = (By.XPATH, "//*[@itemprop='name']")
    ITEM_SKU_NUMBER = (By.XPATH, "//*[@class='product attribute sku']")

    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='product-addtocart-button']")

    ADD_YOUR_REVIEW_LINK = (By.XPATH, "//*[@class='action add']")
    BLOCK_REVIEW_ADD = (By.XPATH, "//*[@class='block review-add']")
    ITEM_REVIEW_COUNT = (By.XPATH, "//span[@itemprop='reviewCount']")
    ITEM_REVIEW_LINK = (By.XPATH, "//*[text()='Reviews']")
    ITEM_RATING = (By.XPATH, "//div[@class='rating-summary']//div[@class='rating-result']")

    CUSTOMER_REVIEWS_HEADER = (By.XPATH, "//strong[text() = 'Customer Reviews']")

    QUANTITY_OF_ITEM = (By.XPATH, "//*[@id='qty']")
    QUANTITY_ERROR_MSG = (By.XPATH, "//*[@id='qty-error']")

    # Clamber Watch Locators
    LINK_CLAMBER_WATCH = (
        By.XPATH, "//div/a[@href='https://magento.softwaretestingboard.com/clamber-watch.html']")
    ADD_TO_CART_CLAMBER_WATCH_BUTTON = (By.XPATH, "//input[@value='43']/following-sibling::button")


class ItemPageReviewsLocators:
    URL = 'https://magento.softwaretestingboard.com/breathe-easy-tank.html'

    TAB_REVIEWS = (By.CSS_SELECTOR, '#tab-label-reviews-title')
    RATING_STAR = (By.XPATH, "(//div[@class='control review-control-vote']/label)[3]")
    NICKNAME_FIELD = (By.CSS_SELECTOR, 'input#nickname_field')
    SUMMARY_FIELD = (By.CSS_SELECTOR, 'input#summary_field')
    REVIEW_FIELD = (By.CSS_SELECTOR, 'textarea#review_field')
    SUBMIT_REVIEW_BUTTON = (By.CSS_SELECTOR, 'button.submit ')
    SUCCESS_MESSAGE = 'You submitted your review for moderation.'





