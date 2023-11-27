from selenium.webdriver.common.by import By


class FiltersLocators:
    URL = 'https://magento.softwaretestingboard.com/men/tops-men.html'

    SELECT_SIZE = (By.XPATH, "//div[@data-role='title'][text()='Size']")
    SELECT_PRICE = (By.XPATH, "//div[@data-role='title'][text()='Price']")
    SELECT_MATERIAL = (By.XPATH, "//div[@data-role='title'][text()='Material']")
    SIZE_M = (By.XPATH, "(//div[@id='narrow-by-list']//*[@class='swatch-option text '])[3]")
    PRICE_20_30 = (By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/men/tops-men.html?price=20-30&size=168"]')
    MATERIAL_POLYESTER = (By.XPATH, '//a[@href="https://magento.softwaretestingboard.com/men/tops-men.html?material=38&price=20-30&size=168"]')
    TAB_MORE_INFORMATION = (By.XPATH, '//*[@id="tab-label-additional"]')
    MATERIAL_POLYESTER_MORE_INFORMATION = (By.XPATH, '//td[@data-th="Material"]')
    SIZE = (By.XPATH, "//div[contains(@class, 'swatch-option text')][3]")
    ITEMS_MEN_TOPS_WITH_FILTER = (By.XPATH, '//*[@class="product photo product-item-photo"]')





