from pages.other_pages.what_is_new import NewPage
import pytest


def test_title(driver):
    page = NewPage(driver, url=NewPage.URL)
    page.open()
    title = page.title()
    assert title == NewPage.TITLE_TEXT, f'Expected text: {NewPage.TITLE_TEXT}, but got: {title}'


def test_widget_yoga(driver):
    page = NewPage(driver, url=NewPage.URL)
    page.open()
    widget_title = page.YOGA_WIDGET_TITLE
    assert widget_title == NewPage.YOGA_WIDGET_TITLE, (f'Expected text: {NewPage.YOGA_WIDGET_TITLE}, but got: '
                                                       f'{widget_title}')

def test_widget_subtitle(driver):
    page = NewPage(driver, url=NewPage.URL)
    page.open()
    subtitle = page.widget_subtitle()
    assert subtitle == NewPage.YOGA_SUBTITLE_TEXT, f'Expected text: {NewPage.YOGA_SUBTITLE_TEXT}, but got: {subtitle}'

