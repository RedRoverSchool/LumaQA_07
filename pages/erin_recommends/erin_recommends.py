from base.seleniumbase import BasePage

class ErinRecommendsPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/collections/erin-recommends.html'

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url