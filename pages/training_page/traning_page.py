from locators.training_page_locators import TrainingPageLocators
from base.seleniumbase import BasePage

class TrainingPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/training.html"
    BLOCK1_IMG_HEIGHT = 372
    BLOCK1_IMG_WIDTH = 1280

    def click_training_menu(self):
        self.is_clickable(TrainingPageLocators.TRAINING_MENU).click()


    def click_video_download_link(self):
        self.is_clickable(TrainingPageLocators.VIDEO_DOWNLOAD).click()