from selenium.webdriver.common.by import By


class MenPageLocators:
    MEN_DROPDOWN_BUTTON = (By.ID, "ui-id-5")
    TOPS_DROPDOWN_BUTTON = (By.ID, "ui-id-17")
    # // *[ @ id = 'ui-id-17]"

    TOPS_CATEGORY_LINK = (By.XPATH, "//*[@id='narrow-by-list2']/dd/ol/li[1]/a")


class TopsMenPageLocators:
    URL = 'https://magento.softwaretestingboard.com/men/tops-men.html'


