from pages.other_pages.what_is_new import NewPage
from locators.whats_new_page_locators import WhatsNewPageLocators


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


def test_widget_title_text(driver):
    whats_new_page = NewPage(driver, url=NewPage.URL)
    whats_new_page.open()
    title_element = whats_new_page.scroll_to_element(WhatsNewPageLocators.SENSE_RENEWAL_WIDGET_TITLE)
    title_element_text = whats_new_page.get_text(title_element)
    expected_title = whats_new_page.SENSE_RENEWAL_TITLE_TEXT
    assert title_element_text == expected_title, f'Expected text: {expected_title}, but got: {title_element_text}'
