from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def options():
    options = Options()
    options.add_argument('--window-size=2880,1800')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return options 

@pytest.fixture 
def driver(options):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver 
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout = 15)
    return wait 