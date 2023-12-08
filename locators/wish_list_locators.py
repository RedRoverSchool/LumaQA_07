from selenium.webdriver.common.by import By


class WishListLocators:
    BUTTON_ALL_TO_CART = (By.XPATH, '//*[@class="action tocart"]')
    WISH_LIST_SIDEBAR = (By.ID, 'wishlist-sidebar')
    WISH_LIST_SIDEBAR_ITEMS = (By.CSS_SELECTOR, '#wishlist-sidebar .product-item')
    SHARE_WISH_LIST_BUTTON = (By.XPATH, '//*[@title="Share Wish List"]')
    EMAIL_ADDRESS_TEXT_BOX = (By.XPATH, '//*[@id="email_address"]')
    MESSAGE_FIELD_TEXT_BOX = (By.XPATH, '//*[@id="message"]')
    PAGINATION = (By.XPATH, '//*[@class="pages"]')
    SELECT_SHOW_ITEMS_QTY = (By.XPATH, "//*[@id='limiter']")
