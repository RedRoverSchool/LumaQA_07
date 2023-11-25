import pytest
from pages.new_luma_yoga_collection_page.new_luma_yoga_collection_page import NewLumaYogaCollectionPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def new_luma_yoga_collection_page_precondition_for_test_data():
    options = Options()
    options.add_argument("--window-size=2880,1800")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    new_luma_yoga_collection_page = NewLumaYogaCollectionPage(driver=driver)
    new_luma_yoga_collection_page.open()
    return  new_luma_yoga_collection_page

@pytest.fixture(scope="function")
def new_luma_yoga_collection_page_precondition(driver):
    new_luma_yoga_collection_page = NewLumaYogaCollectionPage(driver=driver)
    new_luma_yoga_collection_page.open()
    return  new_luma_yoga_collection_page