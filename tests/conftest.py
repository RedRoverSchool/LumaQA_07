import pytest
from faker import Faker
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.account.create_account import CreateAccountPage


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
def create_account(driver, first_name, last_name, email, password):
    CreateAccountPage(driver).new(first_name, last_name, email, password)

