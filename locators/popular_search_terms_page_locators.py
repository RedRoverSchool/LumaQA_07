from selenium.webdriver.common.by import By


class PopularSearchTermsPageLocators:
    HEADING = (By.CSS_SELECTOR, '.base')
    KEYWORDS_LIST = (By.CSS_SELECTOR, '[class="item"] > a')
