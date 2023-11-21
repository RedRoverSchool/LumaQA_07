from selenium.webdriver.common.by import By


class SortItemsLocators:
    URL = 'https://magento.softwaretestingboard.com/men/tops-men.html'

    SORT_SELECT = (By.CSS_SELECTOR, '#sorter')
    DIRECTION_SWITCHER = (By.CSS_SELECTOR, '[data-role="direction-switcher"]')
    PAGING_BUTTON_NEXT = (By.XPATH, "(//a[@class = 'action  next'])[2]")
    NAME_ITEMS = (By.CSS_SELECTOR, 'div.products a.product-item-link')







