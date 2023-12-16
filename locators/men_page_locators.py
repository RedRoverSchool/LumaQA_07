from selenium.webdriver.common.by import By


class MenPageLocators:
    MEN_DROPDOWN_BUTTON = (By.ID, "ui-id-5")
    TOPS_DROPDOWN_BUTTON = (By.ID, "ui-id-17")
    BOTTOMS_DROPDOWN_BUTTON = (By.ID, "ui-id-18")
    TOPS_CATEGORY_LINK = (By.XPATH, "//*[@id='narrow-by-list2']/dd/ol/li[1]/a")
    BOTTOMS_CATEGORY_LINK = (By.XPATH, "//*[@id='narrow-by-list2']/dd/ol/li[2]/a")
    SIDE_BAR_JACKETS = (By.XPATH, "//a[@id='ui-id-19']//span[contains(text(),'Jackets')]")
    MEN_TOPS_GRID = (By.XPATH, "//*[@id='maincontent']/div[3]/div[1]/div[3]/div[1]/strong[2]")
    ADD_TO_WISHLIST_2 = (By.CLASS_NAME, "//*[@class = 'actions-secondary']/a[1]")
    ADD_TO_COMPARE_2 = (By.CSS_SELECTOR, ".action.tocompare")
    INNER_BUTTONS = (By.XPATH, "//*[@class='product actions product-item-actions']")
    # MenTopJacketsPage
    JACKETS_ITEMS = (By.CLASS_NAME, "li[class='item product product-item']")
    LANDO_GYM_JACKET = (By.XPATH, "//a[contains(text(), 'Lando Gym Jacket')]")
    # MenBottomsPage
    SHOPPING_OPTIONS = (By.XPATH, '//*[@id="narrow-by-list"]/div[{num}]/div[1]')


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
    ADD_TO_CART_4 = (By.CSS_SELECTOR, "li[class = 'item product product-item']:nth-child(4)")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, "li[class = 'item product product-item']:nth-child(4) button")
    BUTTON_ADD_TO_CART_2 = (By.CSS_SELECTOR, "li[class = 'item product product-item'] button")
    JACKETS_IMAGE_CARD = (By.CSS_SELECTOR, "li[class='item product product-item']:nth-child(4)")
    ADD_TO_WISH_LIST = (By.CLASS_NAME, 'action.towishlist')
    ADD_TO_COMPARE = (By.CLASS_NAME, 'action.tocompare')
    TITLE_ITEM = (By.CSS_SELECTOR, 'span[class="base"]')
    CLEAR_ALL = (By.CLASS_NAME, 'action.clear')
    LIMITER = (By.XPATH, '(//select[@id="limiter"])[2]')
    LIST_MODE = (By.XPATH, '(//a[@id="mode-list"])[1]')

    @staticmethod
    def get_position_cart(position):
        return By.CSS_SELECTOR, f"li[class = 'item product product-item']:nth-child({position})"

    @staticmethod
    def get_position_button(position):
        return By.CSS_SELECTOR, f"li[class = 'item product product-item']:nth-child({position}) button"

    @staticmethod
    def get_product_image(position: int):
        return By.CSS_SELECTOR, f"li[class='item product product-item']:nth-child({position})"

    @staticmethod
    def get_option_locator(option):
        return By.XPATH, f'(//option[@value="{option}"])[2]'

    @staticmethod
    def create_item_list(num):
        return By.CSS_SELECTOR, f"li[class='item product product-item']:nth-child({num})"

    @staticmethod
    def choose_shopping_options(num):
        return By.XPATH, f'//*[@id="narrow-by-list"]/div[{num}]/div[1]'


class TopsMenPageLocators:
    URL = 'https://magento.softwaretestingboard.com/men/tops-men.html'


class MenShortsPageLocators:
    ITEM_PRODUCT = (By.CLASS_NAME, 'product-item-link')

    @staticmethod
    def get_position_title(title):
        return By.XPATH, f"//a[normalize-space()='{title}']"

    @staticmethod
    def get_title_on_new_page(title):
        return By.XPATH, f"//span[text()='{title}']"
