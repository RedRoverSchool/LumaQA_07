from locators.whatever_page_locators import WhateverPageLocators
from base.seleniumbase import BasePage

class WhateverPage(BasePage):

    def find_widget_whatever_day(self):
        return self.is_visible(WhateverPageLocators.Whatever_Day)


    def find_widget_perfomance_fabrics(self):
        return self.is_clickable(WhateverPageLocators.Perfomance_Fabrics).click()