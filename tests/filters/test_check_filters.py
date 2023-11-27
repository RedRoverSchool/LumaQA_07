import allure
from locators.filters_locators import FiltersLocators
from pages.filters.filters import FiltersCheck, FilterItemPage


@allure.title("Проверка фильтра")
@allure.description("При настройке фильтра, выбрав размер, цвет и ткань, фильтр работает и товары отображаются верно.")
@allure.tag("Фильтр")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Sviatlana Kot")
@allure.testcase("https://trello.com/c/d5Yg9lJd", "TC_008.009.005")
def test_check_filters(driver):
    with allure.step('Открыта страница "Men"-"Tops"'):
        page = FiltersCheck(driver, url=FiltersLocators.URL)
        page.open()
    with allure.step("Выбрать размер'М'"):
        page.select_size().click()
        page.size_m().click()
    with allure.step("Выбрать цену '20.00-20.99'"):
        page.select_price().click()
        page.price_20_30().click()
    with allure.step("Выбрать материал 'Полиэстр'"):
        page.select_material().click()
        page.material_polyester().click()

    res = []
    href = []
    while page.paging_button_next_visible():
        for item in page.price_items():
            res.append(float(item.get_attribute('data-price-amount')))
        for item in page.size_items():
            assert item.get_attribute('aria-checked') == 'true'
        for item in page.items_with_filter():
            href.append(item.get_attribute('href'))
        page.paging_button_next().click()
    for item in page.price_items():
        res.append(float(item.get_attribute('data-price-amount')))
    with allure.step("Размер товара отображается согласно выбранного фильтра"):
        for item in page.size_items():
            assert item.get_attribute('aria-checked') == 'true'
    for item in page.items_with_filter():
        href.append(item.get_attribute('href'))

    with allure.step("Цена на товар отображается согласно выбранного фильтра"):
        for price in res:
            assert 29.99 >= price >= 20, 'Не верно выводит по цене'

    for item in href:
        page = FilterItemPage(driver, url=item)
        page.open()
        page.tab_more_information().click()
    with allure.step("Состав ткани соответствует выбранному фильтру 'Полиэстр'. Товары отображаются согласно выбранного фильтра"):
        assert 'Polyester' in page.material_polyester_more_information().text, 'Материал товара не соответствует выбранному фильтру'







