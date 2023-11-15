from selenium.webdriver.common.by import By


class MenPageLocators:
    MEN_DROPDOWN_BUTTON = (By.ID, "ui-id-5")
    TOPS_DROPDOWN_BUTTON = (By.ID, "ui-id-17")
    BOTTOMS_DROPDOWN_BUTTON = (By.ID, "ui-id-18")
    TOPS_CATEGORY_LINK = (By.XPATH, "//*[@id='narrow-by-list2']/dd/ol/li[1]/a")
    SIDE_BAR_JACKETS = (By.XPATH, "//a[@id='ui-id-19']//span[contains(text(),'Jackets')]")


class TopsMenPageLocators:
    URL = 'https://magento.softwaretestingboard.com/men/tops-men.html'


