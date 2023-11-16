from selenium.webdriver.common.by import By


class MenPageLocators:
    MEN_DROPDOWN_BUTTON = (By.ID, "ui-id-5")
    TOPS_DROPDOWN_BUTTON = (By.ID, "ui-id-17")
    BOTTOMS_DROPDOWN_BUTTON = (By.ID, "ui-id-18")
    TOPS_CATEGORY_LINK = (By.XPATH, "//*[@id='narrow-by-list2']/dd/ol/li[1]/a")
    SIDE_BAR_JACKETS = (By.XPATH, "//a[@id='ui-id-19']//span[contains(text(),'Jackets')]")


class MenCategoryPageLocators:
    CATEGORY_BUTTON = (
        By.XPATH,
        '//div[@class="filter-options-title" and text()="Category"]'
        )
    TEES_FILTER = (
        By.XPATH,
        '//div[@class="filter-options-content"]//a[contains(text(), "Tees")]'
        )
    ITEM = (By.CLASS_NAME, 'product-item-info')
    ITEM_PHOTO = (By.CLASS_NAME, 'product-image-photo')
    ITEM_TITLE = (By.CLASS_NAME, 'product-item-link')
    ADD_TO_CART = (By.CLASS_NAME, 'action.tocart.primary')
    ADD_TO_WISH_LIST = (By.CLASS_NAME, 'action.towishlist')
    ADD_TO_COMPARE = (By.CLASS_NAME, 'action.tocompare')


class TopsMenPageLocators:
    URL = 'https://magento.softwaretestingboard.com/men/tops-men.html'


