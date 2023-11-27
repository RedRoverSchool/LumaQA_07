import allure
from locators.filters_locators import FiltersLocators
from pages.filters.filters import FiltersCheck, FilterItemPage, FilterPerformancePage


@allure.title("Проверка фильтра")
@allure.description("При настройке фильтра, выбрав размер, цвет и ткань, фильтр работает и товары отображаются верно.")
@allure.tag("Фильтр")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Sviatlana Kot")
@allure.testcase("https://trello.com/c/d5Yg9lJd", "TC_008.009.001")
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


@allure.title("Проверка фильтра")
@allure.description("При настройке фильтра, выбрав коллекцию 'Performance fabric' и тип 'Rainy', фильтр работает и товары отображаются верно.")
@allure.tag("Фильтр")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Sviatlana Kot")
@allure.testcase("https://trello.com/c/yFXjFhDR", "TC_008.009.002")
def test_check_filters_fabric_and_climate(driver):
    with allure.step('Получаем список имен из коллекции "Performance fabric"'):
        page = FilterPerformancePage(driver, url=FilterPerformancePage.URL)
        page.open()
        names = page.get_items()

    with allure.step('Открыта страница "Women"-"Jackets"'):
        page = FiltersCheck(driver, url=FiltersLocators.URL_WOMEN_JACkETS)
        page.open()
    with allure.step("Выбрать коллекцию 'Performance fabric'"):
        page.select_performance_fabric().click()
    with allure.step("Выбрать фильтр 'Yes'"):
        page.performance_fabric_yes().click()
    with allure.step("Выбрать тип 'Climate'"):
        page.select_climate().click()
    with allure.step("Выбрать фильтр 'Rainy'"):
        page.select_climate_rainy().click()
    href = []
    while page.paging_button_next_visible():
        for item in page.items_with_filter():
            href.append(item.get_attribute('href'))
        page.paging_button_next().click()
    for item in page.items_with_filter():
        href.append(item.get_attribute('href'))

    while page.paging_button_next_visible():
        for item in page.name_items():
            assert item.text in names, "Товар не из 'Performance Fabric'"
        page.paging_button_next().click()
    for item in page.name_items():
        with allure.step("Ожидаемый результат: 'Товар соответствует выбранной коллекции 'Performance Fabric'"):
            assert item.text in names, "Товар не из 'Performance Fabric'"

    for item in href:
        page = FilterItemPage(driver, url=item)
        page.open()
        page.tab_more_information().click()
    with allure.step("Ожидаемый результат: Тип соответствует выбранному фильтру 'Rainy'"):
        assert 'Rainy' in page.climate_more_information().text, 'Тип товара не соответствует выбранному фильтру'








