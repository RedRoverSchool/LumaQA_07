from selenium.webdriver.common.by import By


class BasePageLocators:
    HEADER = (By.CSS_SELECTOR, 'h1 span')
    MSG_ERROR = (By.CSS_SELECTOR, '[data-ui-id="message-error"]')
    MSG_SUCCESS = (By.CSS_SELECTOR, '[data-ui-id="message-success"]')
    LOGO_TITLE = (By.CSS_SELECTOR, '[class="logo"]')
    ERIN_SECTION = (By.CSS_SELECTOR, '.home-erin')
    LINK_WHATS_NEW = (By.XPATH, "//a[@id='ui-id-3']")

    LINK_WOMEN = (By.XPATH, "//a[@id='ui-id-4']")
    LINK_WOMEN_TOPS = (By.XPATH, "//a[@id='ui-id-9']")
    LINK_WOMEN_TOPS_JACKETS = (By.XPATH, "//a[@id='ui-id-11']")
    LINK_WOMEN_TOPS_HOODIES = (By.XPATH, "//*[@id='ui-id-12']")
    LINK_WOMEN_TOPS_TEES = (By.XPATH, "//*[@id='ui-id-13']")
    LINK_WOMEN_TOPS_BRAS_AND_TANKS = (By.XPATH, "//*[@id='ui-id-14']")
    LINK_WOMEN_BOTTOMS = (By.XPATH, "//*[@id='ui-id-10']")
    LINK_WOMEN_BOTTOMS_PANTS = (By.XPATH, "//*[@id='ui-id-15']")
    LINK_WOMEN_BOTTOMS_SHORTS = (By.XPATH, "//*[@id='ui-id-16']")

    LINK_MEN = (By.XPATH, "//*[@id='ui-id-5']")
    LINK_MEN_TOPS = (By.XPATH, "//*[@id='ui-id-17']")
    LINK_MEN_TOPS_JACKETS = (By.XPATH, "//*[@id='ui-id-19']")
    LINK_MEN_TOPS_HOODIES = (By.XPATH, "//*[@id='ui-id-20']")
    LINK_MEN_TOPS_TEES = (By.XPATH, "//*[@id='ui-id-21']")
    LINK_MEN_TOPS_TANKS = (By.XPATH, "//*[@id='ui-id-22']")
    LINK_MEN_BOTTOMS = (By.XPATH, "//*[@id='ui-id-18']")
    LINK_MEN_BOTTOMS_PANTS = (By.XPATH, "//*[@id='ui-id-23']")
    LINK_MEN_BOTTOMS_SHORTS = (By.XPATH, "//*[@id='ui-id-24']")

    LINK_GEAR = (By.XPATH, "//*[@id='ui-id-6']")
    LINK_GEAR_BAGS = (By.XPATH, "//*[@id='ui-id-25']")
    LINK_GEAR_FITNESS_EQ = (By.XPATH, "//*[@id='ui-id-26']")
    LINK_GEAR_WATCHES = (By.XPATH, "//*[@id='ui-id-27']")

    LINK_TRAINING = (By.XPATH, "//*[@id='ui-id-7']")
    LINK_TRAINING_VIDEO_DOWNLOAD = (By.XPATH, "//*[@id='ui-id-28']")

    LINK_SALE = (By.XPATH, "//*[@id='ui-id-8']")

    WRITE_FOR_US_LINK = (By.XPATH,'//footer//a[@href="https://softwaretestingboard.com/write-for-us/"]')
    COPYRIGHT_INFO = (By.XPATH,"//footer/following-sibling::*[@class='copyright']")

    SHOP_ERIN_RECOMMENDS = (By.CSS_SELECTOR, "a[class='block-promo home-erin'] span[class='action more icon']")
    SHOP_PERFORMANCE = (By.XPATH, "//span[normalize-space()='Shop Performance'][1]")
    BLOCK_PROMO = (By.XPATH, "//*[@class='block-promo-wrapper block-promo-hp']")

    BLOCK_1 = (By.XPATH, "//*[@class='block-promo home-main']")
    BLOCK_2 = (By.XPATH, "//*[@class='block-promo home-pants']")
    BLOCK_3 = (By.XPATH, "//*[@class='block-promo home-t-shirts']")
    BLOCK_5 = (By.XPATH, "//*[@class='block-promo home-performance']")
    BLOCK_6 = (By.XPATH, "//*[@class='block-promo home-eco']")
    LIST_IMAGES = [
        BLOCK_1, BLOCK_2, BLOCK_3, ERIN_SECTION, BLOCK_5, BLOCK_6
    ]