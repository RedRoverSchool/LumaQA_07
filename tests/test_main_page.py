from pages.main_page import MainPage


class TestMainPage:
    def test_verify_visibility_the_title(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.check_visibility_the_title()

        assert True

    def test_visibility_of_erin_recommends_widget(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.check_visibility_of_erin_recommends_widget()

    def test_clickability_of_erin_recommends_widget(self, driver):
        page = MainPage(driver, url=MainPage.URL)
        page.open()
        page.check_clickability_of_erin_recommends_widget()


