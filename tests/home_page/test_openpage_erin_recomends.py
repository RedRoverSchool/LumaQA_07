from data.home_page_url import HOME_PAGE
from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators


def test_openpage_erin_recomends(driver,options,wait):
    page = BasePage(driver, url=HOME_PAGE)
    page.open()
    erin_section = page.is_visible(BasePageLocators.ERIN_SECTION)
    erin_section.click()
    assert page.current_url == 'https://magento.softwaretestingboard.com/collections/erin-recommends.html', "открыта неправильная страница"