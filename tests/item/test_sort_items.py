import pytest

from locators.sort_items_locators import SortItemsLocators, ShowItemsPerPageLocators
from pages.men_category_page.sort_items import SortItemsByProduct, ShowItemsPerPage


def test_sort_items_by_product_name(driver):
    page = SortItemsByProduct(driver, url=SortItemsLocators.URL)
    page.open()
    page.sort_select().select_by_value('name')

    assert page.wait_url_redirection(SortItemsByProduct.URL_SORTED_BY_NAME)
    assert page.sort_direction().get_attribute('data-value') == 'desc'
    res = []
    while page.paging_button_next_visible():
        for item in page.name_items():
            res.append(item.text)
        page.paging_button_next().click()
    for item in page.name_items():
        res.append(item.text)
    assert res == sorted(res), 'Не верно отсортирован'


def test_sort_items_by_price(driver):
    page = SortItemsByProduct(driver, url=SortItemsLocators.URL)
    page.open()
    page.sort_select().select_by_value('price')

    # assert page.wait_url_redirection(SortItemsByProduct.URL_SORTED_BY_NAME)
    assert page.sort_direction().get_attribute('data-value') == 'desc'
    res = []
    while page.paging_button_next_visible():
        for item in page.price_items():
            res.append(float(item.get_attribute('data-price-amount')))
        page.paging_button_next().click()
    for item in page.price_items():
        res.append(float(item.get_attribute('data-price-amount')))
    assert res == sorted(res), 'Не верно отсортирован'
    page.sort_direction().click()
    page.paging_one_page().click()
    res = []
    while page.paging_button_next_visible():
        for item in page.price_items():
            res.append(float(item.get_attribute('data-price-amount')))
        page.paging_button_next().click()
    for item in page.price_items():
        res.append(float(item.get_attribute('data-price-amount')))
    assert res == sorted(res, reverse=True), 'Не верно отсортирован'


@pytest.mark.parametrize('qty', [12, 24, 36])
def test_show_items_per_page_grid(driver, qty):
    page = ShowItemsPerPage(driver, url=ShowItemsPerPageLocators.URL)
    page.open()
    page.modes_grid_active()
    page.select_show_items().select_by_value(str(qty))
    assert page.item_count(ShowItemsPerPageLocators.NAME_ITEMS) == qty, 'Не верное количество'


@pytest.mark.parametrize('qty', [5, 10, 15, 20, 25])
def test_show_items_per_page_list(driver, qty):
    page = ShowItemsPerPage(driver, url=ShowItemsPerPageLocators.URL)
    page.open()
    page.modes_list().click()
    page.modes_list_active()
    page.select_show_items().select_by_value(str(qty))
    assert page.item_count(ShowItemsPerPageLocators.NAME_ITEMS) == qty, 'Не верное количество'













