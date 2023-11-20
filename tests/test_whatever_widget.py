import time

from pages.whatever_page import WhateverPage


def test_whatever_widget(driver):
    page = WhateverPage(driver, "https://magento.softwaretestingboard.com/what-is-new.html")
    page.open()
    page.find_widget_whatever_day()
    assert 'Whatever day brings' in driver.page_source
    page.find_widget_perfomance_fabrics()
    assert 'Performance Sportswear New' in driver.page_source

