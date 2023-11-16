from locators.training_page_locators import TrainingPageLocators
from base.seleniumbase import BasePage

class TrainingPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/training.html"

    def click_training_menu(self):
        self.is_clickable(TrainingPageLocators.TRAINING_MENU).click()