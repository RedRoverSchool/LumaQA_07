from selenium.webdriver.common.by import By
from base.seleniumbase import BasePage

class NewPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/what-is-new.html"

    TITLE = (By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]')
    YOGA_COLL = (By.CSS_SELECTOR, 'a.new-main  span.info')
    YOGA_SUBTITLE = (By.CSS_SELECTOR, 'a.new-main  strong.title')

    TITLE_TEXT = "What's New"
    YOGA_WIDGET_TITLE = "New Luma Yoga Collection"
    YOGA_SUBTITLE_TEXT = 'The very latest yoga styles plus twists on timeless classics'


    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url

    def title(self) -> str:
        return self.is_visible(self.TITLE).text

    def widget_yoga_call(self) -> str:
        return self.is_visible(self.YOGA_COLL).text

    def widget_subtitle(self) -> str:
        return self.is_visible(self.YOGA_SUBTITLE).text

