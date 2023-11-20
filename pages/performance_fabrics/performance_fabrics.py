from base.seleniumbase import BasePage

class PerformanceFabricsPage(BasePage):
    URL = 'https://magento.softwaretestingboard.com/collections/performance-fabrics.html'

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url