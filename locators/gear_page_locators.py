from selenium.webdriver.common.by import By

class GearPageLocators:
    # Categories on Gear page
    SIDEBAR_ELEMENTS = (By.XPATH,'//dd//a')
    SIDEBAR_MAIN = (By.XPATH,'//div[@class="sidebar sidebar-main"]')
    SHOP_BY_TITLE = (By.XPATH,'.//div[@class="title"]/strong')
    CATEGORY_TITLE = (By.XPATH,'//dl[@id="narrow-by-list2"]/dt')

class CategoryPageLocators:    
    # category page
    LAST_ITEM_COUNTER= (By.XPATH,'//p[@id="toolbar-amount"]//span[last()]')
    ITEM_ON_THE_PAGE = (By.XPATH,'//a[@class="product-item-link"]')
    NEXT_BUTTON = (By.XPATH,'//div[@class="pages"]//a[@class="action  next"][last()]')

class BannerLocators:
    # Gear page banners
    SPRITE_YOGA_COMPANION_KIT_BANNER = (By.XPATH, '//a[@class="block-promo gear-main"]')
    LOOSEN_UP_BANNER = (By.XPATH, '//a[@class="block-promo gear-fitnes"]')
    LUMA_WATER_BOTTLE_BANNER = (By.XPATH, '//a[@class="block-promo gear-equipment"]')
    BAGS_BANNER = (By.XPATH, '//a[@class="block-promo gear-category-bags"]')
    FITNESS_EQUIPMENT_BANNER = (By.XPATH, '//a[@class="block-promo gear-category-equipment"]')
    WATCHES_BANNER = (By.XPATH, '//a[@class="block-promo gear-category-watches"]')
    # Gear page buttons
    SPRITE_YOGA_COMPANION_KIT_BANNER_BUTTON = (By.XPATH, '//span[@class="more button"]')