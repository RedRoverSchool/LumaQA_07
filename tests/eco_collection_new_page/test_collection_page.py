import time

from pages.other_pages.eco_collection_new import CollectionPage
import pytest


def test_title_page(driver):
    page = CollectionPage(driver, url=CollectionPage.URL)
    page.open()
    title = page.title()
    assert title == CollectionPage.TITLE_TEXT, f'Expected text: {CollectionPage.TITLE_TEXT}, but got: {title}'


def test_banner_title(driver):
    page = CollectionPage(driver, url=CollectionPage.URL)
    page.open()
    banner_title = page.banner_title()
    assert banner_title == CollectionPage.BANNER_TEXT, (f'Expected text: {CollectionPage.BANNER_TEXT}, '
                                                        f'but got: {banner_title}')


def test_bunner_subtitle(driver):
    page = CollectionPage(driver, url=CollectionPage.URL)
    page.open()
    subtitle = page.banner_subtitle()
    assert subtitle == CollectionPage.SUBTITLE_TEXT, f'Expected text: {CollectionPage.SUBTITLE_TEXT}, but got: {subtitle}'


def test_items(driver):
    """ TC _006.013.004 | Eco Collection New > The items name is visible and clickable """
    page = CollectionPage(driver, url=CollectionPage.URL)
    page.open()
    for item in range(len(page.items())):
        page.open()
        items = page.items()
        items[item].click()
        title = page.is_visible(CollectionPage.ITEM_TITLE).text
        assert title in CollectionPage.ITEMS_TEXT, f'Expected text: {CollectionPage.ITEMS_TEXT}, but got: {title}'
        assert page.current_url in CollectionPage.ITEMS_URL, (f'Expected text: {CollectionPage.ITEMS_URL}, '
                                                              f'but got: {page.current_url}')

def test_images(driver):
    """TC _006.013.005 | Eco Collection New >The item’s image is clickable"""
    page = CollectionPage(driver, url=CollectionPage.URL)
    page.open()
    for image in range(len(page.images())):
        page.open()
        images = page.images()
        images[image].click()
        title = page.is_visible(CollectionPage.ITEM_TITLE).text
        assert title in CollectionPage.ITEMS_TEXT, f'Expected text: {CollectionPage.ITEMS_TEXT}, but got: {title}'
        assert page.current_url in CollectionPage.ITEMS_URL, (f'Expected text: {CollectionPage.ITEMS_URL}, '
                                                              f'but got: {page.current_url}')


def test_prices(driver):
    """TC _006.013.006 | Eco Collection New > The items price is visible"""
    page = CollectionPage(driver, url=CollectionPage.URL)
    page.open()
    prices = page.prices()
    for price in range(len(prices)):
        price = prices[price].text
        assert price in CollectionPage.PRICE_TEXT, f'Expected text: {CollectionPage.PRICE_TEXT}, but got: {price}'

def test_colors(driver):
    """TC _006.013.007 | Eco Collection New > The color options are selectable"""
    page = CollectionPage(driver, url=CollectionPage.URL)
    page.open()
    colors = page.colors()
    for color in range(len(colors)):
        colors[color].click()
        frame_assert = page.select_frame()

def test_size(driver):
    """TC _006.013.008 | Eco Collection New > The size options are selectable"""
    page = CollectionPage(driver, url=CollectionPage.URL)
    page.open()
    sizes = page.sizes()
    for size in range(len(sizes)):
        sizes[size].click()
        time.sleep(3)
        frame_assert = page.select_frame()



