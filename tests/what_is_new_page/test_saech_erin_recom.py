from pages.main_page import MainPage


def test_widget_erin(options, driver, wait):
    page = MainPage(driver, url=MainPage.URL)
    page.open()
    page.check_visibility_of_erin_recommends_widget()
    page.check_clickability_of_erin_recommends_widget()

    assert 'Erin Recommends' in driver.page_source
