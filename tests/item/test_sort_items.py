from locators.sort_items_locators import SortItemsLocators
from pages.men_category_page.sort_items import SortItemsByProduct


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



