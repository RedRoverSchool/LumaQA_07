from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage


class CollectionPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/collections/eco-new.html'
    ITEMS_URL = ["https://magento.softwaretestingboard.com/bruno-compete-hoodie.html",
                 "https://magento.softwaretestingboard.com/layla-tee.html",
                 "https://magento.softwaretestingboard.com/fiona-fitness-short.html",
                 "https://magento.softwaretestingboard.com/stellar-solar-jacket.html",
                 "https://magento.softwaretestingboard.com/elisa-evercool-trade-tee.html"]
    TITLE = (By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]')
    BANNER_TITLE = (By.CSS_SELECTOR, 'strong.title')
    BANNER_SUBTITLE = (By.CSS_SELECTOR, 'span.info')
    BRUNO_TITLE = (By.CSS_SELECTOR, 'a[title="Bruno Compete Hoodie"]')
    LAYLA_TITLE = (By.CSS_SELECTOR, 'a[title="Layla Tee"]')
    FIONA_TITLE = (By.CSS_SELECTOR, 'a[title="Fiona Fitness Short"]')
    STELLAR_TITLE = (By.CSS_SELECTOR, 'a[title="Stellar Solar Jacket"]')
    ELISA_TITLE = (By.CSS_SELECTOR, 'a[title="Elisa EverCool&trade; Tee"]')
    ITEMS = (By.XPATH, '//ol[@class="product-items widget-product-grid"]/li')
    ITEMS_IMAGES = (By.CSS_SELECTOR, 'span.product-image-container')
    ITEM_TITLE = (By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]')
    ITEM_PRICES = (By.CSS_SELECTOR, 'span.price')
    ITEM_COLORS = (By.CSS_SELECTOR, 'div[aria-label="Color"]')
    SELECT_FRAME = (By.CLASS_NAME, 'selected')
    ITEM_SIZES = (By.CSS_SELECTOR, 'div.product-item-info #option-label-size-143-item-166')

    TITLE_TEXT = 'Eco Collection New'
    BANNER_TEXT = 'Eco-friendly, ego-friendly'
    SUBTITLE_TEXT = 'Recycled polyester, hemp and organic cotton apperel'
    BRUNO_TEXT = 'Bruno Compete Hoodie'
    LAYLA_TEXT = 'Layla Tee'
    FIONA_TEXT = 'Fiona Fitness Short'
    STELA_TEXT = 'Stellar Solar Jacket'
    ELISA_TEXT = 'Elisa EverCool™ Tee'
    TEXT = ['Bruno Compete Hoodie', 'Layla Tee', 'Fiona Fitness Short', 'Stellar Solar Jacket',
            'Elisa EverCool™ Tee']
    TITLE_ALL = (By.CSS_SELECTOR, 'ol.product-items.widget-product-grid')
    ITEMS_TEXT = ["Bruno Compete Hoodie", "Layla Tee", "Fiona Fitness Short", "Stellar Solar Jacket",
                  "Elisa EverCool™ "
                  "Tee"]
    PRICE_TEXT = ['$63.00', '$29.00', '$75.00']

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url

    def title(self) -> str:
        return self.is_visible(self.TITLE).text

    def banner_title(self) -> str:
        return self.is_visible(self.BANNER_TITLE).text

    def banner_subtitle(self) -> str:
        return self.is_visible(self.BANNER_SUBTITLE).text

    def bruno_title(self) -> str:
        return self.is_visible(self.BRUNO_TITLE).text

    def find_titles(self):
        return self.is_visible_all_elements(self.TITLE_ALL)

    def items(self) -> list:
        return self.is_visible_all_elements(self.ITEMS)

    def images(self) -> list:
        return self.is_visible_all_elements(self.ITEMS_IMAGES)

    def prices(self) -> list:
        return self.is_visible_all_elements(self.ITEM_PRICES)

    def colors(self) -> list:
        return self.is_visible_all_elements(self.ITEM_COLORS)

    def sizes(self) -> list:
        return self.is_visible_all_elements(self.ITEM_SIZES)

    def select_frame(self) :
        return self.is_visible(self.SELECT_FRAME)

