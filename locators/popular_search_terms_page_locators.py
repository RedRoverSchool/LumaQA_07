from selenium.webdriver.common.by import By


POPULAR_SEARCH_TERMS_PAGE_TITLE_LOCATOR = (By.XPATH, "//span[@class='base']")


class PopularSearchTermsPageLocators:
    HEADING = (By.CSS_SELECTOR, '.base')
    KEYWORDS_LIST = (By.CSS_SELECTOR, '[class="item"] > a')
    HOODIE_ITEM_KEYWORDS_LINK = (By.CSS_SELECTOR, '[href$="HOODIE"]')

class PopularSearchTermsPageFooterLocators:
    FOOTER_SEARCH_TERMS_LINK = (By.XPATH, "//li[@class='nav item current']")
