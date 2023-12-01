import pytest
from pages.item_page import ItemDetailsPage


@pytest.fixture()
def add_items_to_wish_list(driver):
    lst = ['https://magento.softwaretestingboard.com/breathe-easy-tank.html',
           'https://magento.softwaretestingboard.com/push-it-messenger-bag.html',
           'https://magento.softwaretestingboard.com/ina-compression-short.html',
           'https://magento.softwaretestingboard.com/clamber-watch.html',
           'https://magento.softwaretestingboard.com/tiffany-fitness-tee.html',
           'https://magento.softwaretestingboard.com/ida-workout-parachute-pant.html']
    for href in lst:
        page = ItemDetailsPage(driver, url=href)
        page.add_to_wish_list().click()
        assert page.message.endswith('has been added to your Wish List. Click here to continue shopping.')

