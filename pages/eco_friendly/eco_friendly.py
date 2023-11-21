from base.seleniumbase import BasePage

class EcoFriendlyPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url