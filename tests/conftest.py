import pytest
from faker import Faker

from base.seleniumbase import BasePage
from locators.login import LOGIN_PAGE, LOGAUT_PAGE
from pages.account.create_account import CreateAccountPage
from pages.item_page import ItemPage
from pages.login.login_page import LoginPage
from pages.my_account.address_book_page import AddressBookPage


@pytest.fixture
def first_name():
    return Faker().first_name()


@pytest.fixture
def last_name():
    return Faker().last_name()


@pytest.fixture
def email():
    return Faker().email()


@pytest.fixture
def password():
    return Faker().password()


@pytest.fixture
def state():
    return Faker().state()


@pytest.fixture
def postcode():
    return Faker().postcode()


@pytest.fixture
def phone_number():
    return Faker().phone_number()


@pytest.fixture
def street_address():
    return Faker().street_address()


@pytest.fixture
def city():
    return Faker().city()


@pytest.fixture
def create_account(driver):
    CreateAccountPage(driver)


@pytest.fixture
def add_3_item_to_cart(driver):
    page = ItemPage(driver, url=ItemPage.URL_DRIVEN_BACKPACK)
    page.open()
    page.add_driven_backpack_from_item_card_to_cart(3)


@pytest.fixture
def add_first_address_in_account(driver, state, first_name, last_name, phone_number, street_address, city, postcode):
    page = AddressBookPage(driver, url=AddressBookPage.URL_USER_HAS_NO_ADDRESS)
    page.open()
    page.add_new_address(state, first_name, last_name, phone_number, street_address, city, postcode)


@pytest.fixture
def authorization(driver):
    page = LoginPage(driver, LOGIN_PAGE)
    page.open()
    page.sign_in()
    yield
    page = LoginPage(driver, LOGAUT_PAGE)
    page.open()


@pytest.fixture
def any_page_precondition(driver, any_url):
    base_page = BasePage(driver=driver, url=any_url)
    base_page.open()
    return base_page
