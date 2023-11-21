from selenium.webdriver.common.by import By


class SortItemsLocators:
    URL = 'https://magento.softwaretestingboard.com/men/tops-men.html'

    SORT_SELECT = (By.CSS_SELECTOR, '#sorter')
    DIRECTION_SWITCHER = (By.CSS_SELECTOR, '[data-role="direction-switcher"]')
    PAGING_BUTTON_NEXT = (By.XPATH, "(//a[@class = 'action  next'])[2]")
    NAME_ITEMS = (By.CSS_SELECTOR, 'div.products a.product-item-link')
    PRICE_ITEMS = (By.CSS_SELECTOR, 'div.price-box.price-final_price .price-wrapper')
    PAGING_ONE_PAGE = (By.XPATH, "(//a[@class='page']//span[text()='1'])[2]")


class ShowItemsPerPageLocators:
    URL = 'https://magento.softwaretestingboard.com/men/tops-men.html'

    SELECT_SHOW_ITEMS_QTY = (By.XPATH, "(//*[@id='limiter'])[2]")
    NAME_ITEMS = (By.CSS_SELECTOR, 'div.products a.product-item-link')
    PAGING_BUTTON_NEXT = (By.XPATH, "(//a[@class = 'action  next'])[2]")
    MODES_GRID_ACTIVE = (By.XPATH, "(//*[@class='modes-mode active mode-grid'])[1]")
    MODES_LIST = (By.XPATH, "(//*[@class='modes-mode mode-list'])[1]")
    MODES_LIST_ACTIVE = (By.XPATH, "(//*[@class='modes-mode active mode-list'])[1]")








