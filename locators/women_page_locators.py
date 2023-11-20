from selenium.webdriver.common.by import By


class WomenPageLocators:
    PRODUCTS = (By.XPATH, "//li[@class='item product product-item']")
    PAGE_NAME = (By.TAG_NAME, "h1")
    TOP_WOMEN = (By.XPATH, "//ol[@class='items']//a[@href='https://magento.softwaretestingboard.com/women/tops-women.html']")
