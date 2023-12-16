import os
import subprocess
import time
from shutil import rmtree, move

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from base.seleniumbase import BasePage
from data.home_page_url import HOME_PAGE
from locators.login_page_locators import LoginPageLocators
from locators.base_page_locators import BasePageLocators


def pytest_configure(config):
    shot = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
    rmtree(shot, ignore_errors=True)
    os.makedirs(shot, exist_ok=True)


def pytest_unconfigure(config):
    cwd_report = os.path.join(os.getcwd(), "allure-report")
    cwd_result = os.path.join(os.getcwd(), config.getoption("--alluredir"))
    report_history = os.path.join(cwd_report, "history")
    result_history = os.path.join(cwd_result, "history")

    allure = "allure"  # if os.environ.get('PYTHONDONTWRITEBYTECODE') == '1' else "allure.bat"
    subprocess.run([allure, "generate", "--clean"])

    rmtree(result_history, ignore_errors=True)
    move(report_history, cwd_result)
    rmtree(cwd_report, ignore_errors=True)


@pytest.fixture
def options():
    options = Options()
    options.add_argument('--window-size=1000,800')
    options.add_argument('--headless')
    options.add_argument("--ignore-certificate-errors")
    if os.environ.get('PYTHONDONTWRITEBYTECODE') == '1':
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
    return options


@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options=options)
    # print(f"Created driver: {driver}")
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=15)
    return wait


@pytest.fixture(autouse=True)
def save_screenshot(request, driver):
    failed_before = request.session.testsfailed
    yield

    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        time_string = time.asctime().replace(":", "_")[10:-5]

        test_file_name = os.path.splitext(os.path.basename(request.module.__file__))[0]
        screenshots_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
        file_directory = os.path.join(screenshots_directory, test_file_name)
        run_directory = os.path.join(file_directory, test_name)

        os.makedirs(run_directory, exist_ok=True)

        file_name = f"{time_string}.png"
        full_file_path = os.path.join(run_directory, file_name)
        driver.get_screenshot_as_file(full_file_path)

        allure.attach.file(full_file_path, name=file_name, attachment_type=allure.attachment_type.PNG)


@pytest.fixture()
def open_main_page(driver):
    base_page = BasePage(driver=driver, url=HOME_PAGE)
    base_page.open()
    return base_page


@pytest.fixture
def sign_in(driver):
    driver.find_element(*BasePageLocators.LINK_HEADER_SIGN_IN).click()
    driver.find_element(*LoginPageLocators.EMAIL).send_keys('testTestpro@gmail.com')
    driver.find_element(*LoginPageLocators.PASSWORD).send_keys('Zaqxsw100')
    driver.find_element(*LoginPageLocators.BUTTON_SIGN_IN).click()
