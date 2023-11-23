import os
import time
from shutil import rmtree

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def pytest_configure(config):
    shot = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
    rmtree(shot, ignore_errors=True)
    os.makedirs(shot, exist_ok=True)
    allure_results = os.path.join(os.path.dirname(os.path.abspath(__file__)), "allure-results")
    rmtree(allure_results, ignore_errors=True)
    os.makedirs(allure_results, exist_ok=True)


@pytest.fixture
def options():
    options = Options()
    options.add_argument('--window-size=2880,1800')
    # options.add_argument('--headless')
    options.add_argument("--ignore-certificate-errors")
    if os.environ.get('PYTHONDONTWRITEBYTECODE') == '1':
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
    return options 


@pytest.fixture 
def driver(options):
    driver = webdriver.Chrome(options=options)
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
