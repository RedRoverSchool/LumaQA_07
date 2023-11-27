from pages.performance_fabrics.performance_sportswear import PerformanceSportsWearPage


def test_performance_add_wish(driver):
    page=PerformanceSportsWearPage(driver,url=PerformanceSportsWearPage.URL)
    page.open()
    page.hold_on_element()
    page.find_button_add_wish()
    page.go_to_page_customer()
    assert "Customer Login" in driver.page_source

def test_performance_add_compare(driver):
    page = PerformanceSportsWearPage(driver, url=PerformanceSportsWearPage.URL)
    page.open()
    page.hold_on_element()
    page.find_button_add_compare()
    page.go_to_page_compare()
    assert "You added product Celeste Sports Bra to the " in driver.page_source

def test_performance_add_cart(driver):
    page = PerformanceSportsWearPage(driver, url=PerformanceSportsWearPage.URL)
    page.open()
    page.hold_on_element()
    page.find_button_add_cart()
    page.go_to_page_add_cart()

    assert "Celeste Sports Bra"==page.go_to_page_add_cart()







