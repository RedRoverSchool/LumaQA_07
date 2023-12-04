from selenium.webdriver.common.by import By


class WishListLocators:
    BUTTON_ALL_TO_CART = (By.XPATH, '//*[@class="action tocart"]')
    WISH_LIST_SIDEBAR = (By.ID, 'wishlist-sidebar')
    WISH_LIST_SIDEBAR_ITEMS = (By.CSS_SELECTOR, '#wishlist-sidebar .product-item')



