import pytest
from locators.login_page_locators import LoginPageLocators
from pages.login.login_page import LoginPage


@pytest.fixture
def sign_in_wish_list(driver):
    page = LoginPage(driver, LoginPageLocators.URL)
    page.open()
    page.email().send_keys('rudahin01@bk.ru')
    page.password().send_keys('Mlpokn600')
    page.button_sign_in().click()
    assert page.header().text == 'My Account', "Не удалось войти"