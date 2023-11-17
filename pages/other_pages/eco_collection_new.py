from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage

class CollectionPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/collections/eco-new.html'
    TITLE = (By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]')
    BANNER_TITLE = (By.CSS_SELECTOR, 'strong.title')
    BANNER_SUBTITLE = (By.CSS_SELECTOR, 'span.info')

    TITLE_TEXT = 'Eco Collection New'
    BANNER_TEXT = 'Eco-friendly, ego-friendly'
    SUBTITLE_TEXT =  'Recycled polyester, hemp and organic cotton apperel'

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url

    def title(self) -> str:
        return self.is_visible(self.TITLE).text

    def banner_title(self) -> str:
        return self.is_visible(self.BANNER_TITLE).text

    def banner_subtitle(self) -> str:
        return self.is_visible(self.BANNER_SUBTITLE).text