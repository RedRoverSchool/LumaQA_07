from pages.training_page.traning_page import TrainingPage
from locators.training_page_locators import TrainingPageLocators


class TestTrainingPage:
    def test_open_Training_page(self, driver):
        page = TrainingPage(driver, url=TrainingPage.URL)
        page.open()
        page.click_training_menu()
        expected_url = "https://magento.softwaretestingboard.com/training.html"
        assert driver.current_url == expected_url, 'Wrong URL'


    def test_text_is_displayed(self, driver):
        page = TrainingPage(driver, url=TrainingPage.URL)
        page.open()
        page.click_training_menu()
        training_text = page.is_visible(TrainingPageLocators.TRAINING_TEXT)
        shop_by_text = page.is_visible(TrainingPageLocators.SHOP_BY_TEXT)
        video_download_text = page.is_visible(TrainingPageLocators.VIDEO_DOWNLOAD)
        compare_products_text = page.is_visible(TrainingPageLocators.COMPARE_PRODUCTS_TEXT)
        my_wish_list_text = page.is_visible(TrainingPageLocators.MY_WISH_LIST_TEXT)
        assert training_text.is_displayed(), "Training text is not displayed"
        assert shop_by_text.is_displayed(), "Shop By text is not displayed"
        assert video_download_text.is_displayed(), "Video Download text is not displayed"
        assert compare_products_text.is_displayed(), "Compare Products text is not displayed"
        assert my_wish_list_text.is_displayed(), "My Wish List text is not displayed"


    def test_Video_Download_is_clickable(self, driver):
        page = TrainingPage(driver, url=TrainingPage.URL)
        page.open()
        video_download_link = page.is_clickable(TrainingPageLocators.VIDEO_DOWNLOAD)
        assert video_download_link.is_displayed(), "Video Download link is not displayed"
        assert video_download_link.get_attribute('href') is not None, "Video Download link is None"