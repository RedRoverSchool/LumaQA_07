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
