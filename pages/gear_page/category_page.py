from base.seleniumbase import BasePage

class CategoryPage(BasePage):
    # can be any for all 3 category page

    def __init__(self, driver,url):
        super().__init__(url=url,driver=driver)
