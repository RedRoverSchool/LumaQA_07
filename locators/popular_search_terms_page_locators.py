from selenium.webdriver.common.by import By


class PopularSearchTermsPageLocators:
    HEADING = (By.CSS_SELECTOR, '.base')
    KEYWORDS_LIST = (By.CSS_SELECTOR, '[class="item"] > a')
    HOODIE_ITEM_KEYWORDS_LINK = (By.CSS_SELECTOR, '[href$="HOODIE"]')
