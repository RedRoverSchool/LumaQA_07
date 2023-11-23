from selenium.webdriver.common.by import By


class ItemPageLocators:
    ITEM_NAME = (By.XPATH, "//*[@itemprop='name']")
    ITEM_SKU_NUMBER = (By.XPATH, "//*[@class='product attribute sku']")

    ADD_TO_CART_BUTTON = (By.XPATH, "//*[@id='product-addtocart-button']")

    ADD_YOUR_REVIEW_LINK = (By.XPATH, "//*[@class='action add']")
    BLOCK_REVIEW_ADD = (By.XPATH, "//*[@class='block review-add']")
    BLOCK_CUSTOMER_REVIEWS = (By.XPATH,"//*[text()='Customer Reviews']")
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

    # Echo Fit Compression Short (EFCS)
    LINK_EFCS_SIZE_28 = (By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/echo-fit-compression-short.html"]/following-sibling::div[@class="product details product-item-details"]//child::div[@option-label="28"]')
    LINK_EFCS_SIZE_BLACK = (By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/echo-fit-compression-short.html"]/following-sibling::div[@class="product details product-item-details"]//child::div[@option-label="Black"]')
    LINK_EFCS_ADD_TO_CART = (By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/echo-fit-compression-short.html"]/following-sibling::div[@class="product details product-item-details"]//child::button[@title="Add to Cart"]')
    LINK_EFCS_SIZE_29 = (By.XPATH, '//div[@class="swatch-option text"]')
    LINK_EFCS_SIZE_BLUE = (By.XPATH, '//div[@aria-label = "Blue"]')

class ItemPageReviewsLocators:
    URL = 'https://magento.softwaretestingboard.com/breathe-easy-tank.html'

    TAB_REVIEWS = (By.CSS_SELECTOR, '#tab-label-reviews-title')
    RATING_3_STAR = (By.XPATH, "(//div[@class='control review-control-vote']/label)[3]")
    NICKNAME_FIELD = (By.CSS_SELECTOR, 'input#nickname_field')
    SUMMARY_FIELD = (By.CSS_SELECTOR, 'input#summary_field')
    REVIEW_FIELD = (By.CSS_SELECTOR, 'textarea#review_field')
    SUBMIT_REVIEW_BUTTON = (By.CSS_SELECTOR, 'button.submit ')
    SUCCESS_MESSAGE = 'You submitted your review for moderation.'


class ItemPageRatingLocators:
    URL = 'https://magento.softwaretestingboard.com/women/tops-women.html'
    URL_REVIEWS = 'https://magento.softwaretestingboard.com/antonia-racer-tank.html#reviews'
    URL_ADD_YOUR_REVIEWS = 'https://magento.softwaretestingboard.com/antonia-racer-tank.html#review-form'

    ITEM_ANTONIA_RACER_TANK = (By.CSS_SELECTOR, '[href="https://magento.softwaretestingboard.com/'
                                                'antonia-racer-tank.html"]')
    REVIEW_RATINGS = (By.CSS_SELECTOR, '.review-ratings .rating-result')
    RATING_RESULT = (By.CSS_SELECTOR, '.product-reviews-summary .rating-result')
    LINK_REVIEWS = (By.CSS_SELECTOR, '.reviews-actions .view')
    LINK_ADD_YOUR_REVIEWS = (By.CSS_SELECTOR, '.reviews-actions .add')


class ColorSizeBlockLocators:
    COLOR = (By.XPATH, "//div[contains(@class, 'swatch-option color')][1]")
    SIZE = (By.XPATH, "//div[contains(@class, 'swatch-option text')][1]")
    SELECTED_SIZE = (By.XPATH, "//div[@attribute-code='size']//span[@class='swatch-attribute-selected-option']")
    SELECTED_COLOR = (By.XPATH, "//div[@attribute-code='color']//span[@class='swatch-attribute-selected-option']")


class ItemPageJacketsJupiterTrainerLocators:
    COLOR = (By.XPATH, "//div[contains(@class, 'swatch-option color')][2]")
    SIZE = (By.XPATH, "//div[contains(@class, 'swatch-option text')][2]")
    FIELD_QTY = (By.XPATH, '//*[@id="qty"]')
    BUTTON_ADD_TO_CART = (By.XPATH, '//*[@id="product-addtocart-button"]')
    LINK_SHOPPING_CART = (By.XPATH, '//*[@data-ui-id="message-success"]'
                                    '//a[@href="https://magento.softwaretestingboard.com/checkout/cart/"]')
    SUBTOTAL = (By.XPATH, '//tr[@class="totals sub"]//span')
    DISCOUNT = (By.XPATH, '//tr[@class="totals"]//td[@class="amount"]//span[@class="price"]')


