from selenium.webdriver.common.by import By


class BasePageLocators:
    HEADER = (By.CSS_SELECTOR, 'h1 span')
    MSG_ERROR = (By.CSS_SELECTOR, '[data-ui-id="message-error"]')
    MSG_SUCCESS = (By.CSS_SELECTOR, '[data-ui-id="message-success"]')
    LOGO_TITLE = (By.CSS_SELECTOR, '[class="logo"]')
    ERIN_SECTION = (By.CSS_SELECTOR, '.home-erin')

    LINK_GEAR_CATALOG = (By.XPATH, "//*[@id='ui-id-6']")
    LINK_WATCHES_CATALOG = (By.XPATH, "//*[@id='ui-id-27']")

    WRITE_FOR_US_LINK = (By.XPATH,'//footer//a[@href="https://softwaretestingboard.com/write-for-us/"]')
    COPYRIGHT_INFO = (By.XPATH,"//footer/following-sibling::*[@class='copyright']")

    SHOP_ERIN_RECOMMENDS = (By.CSS_SELECTOR, "a[class='block-promo home-erin'] span[class='action more icon']")

