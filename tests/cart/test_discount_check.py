from pages.item_page import ItemPageJacketsJupiterTrainer
import allure


@allure.title("Проверка скидки общей суммой свыше $200")
@allure.description("При добавлении товаров на сумму свыше $200, в 'Summary' появляется скидка 20%")
@allure.tag("Корзина товаров")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Sviatlana Kot")
@allure.testcase("https://trello.com/c/D3X1DAAu", "TC_005.002.005")
def test_discount_check(driver):
    with allure.step('Открыта страница товара'):
        page = ItemPageJacketsJupiterTrainer(driver, url=ItemPageJacketsJupiterTrainer.URL)
        page.open()
    with allure.step("Выбрать размер'S'"):
        page.size_item().click()
    with allure.step("Выбрать цвет 'Green'"):
        page.color_item().click()
    with allure.step("Ввести в поле 'Qty' '4'"):
        page.qty_item().clear()
        page.qty_item().send_keys('4')
    with allure.step("Нажать на кнопку 'Add to cart'"):
        page.add_to_cart().click()
    with allure.step("Нажать на ссылку 'Shopping cart'"):
        page.link_shopping_cart().click()
    with allure.step("В 'Summary' на странице корзины отображается скидка 20%"):
        assert page.discount_in_summary() > 0, 'Нет скидки'
    assert round(page.subtotal() * 0.2, 2) == page.discount_in_summary(), 'Не верно отображается скидка'


@allure.title("Проверка скидки общей суммой до $200")
@allure.description("При добавлении товаров на сумму до $200, в 'Summary' не отображается скидка 20%")
@allure.tag("Корзина товаров")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Sviatlana Kot")
@allure.testcase("https://trello.com/c/w0U3NyZK", "TC_005.002.004")
def test_discount_check_under_200(driver):
    with allure.step('Открыта страница товара'):
        page = ItemPageJacketsJupiterTrainer(driver, url=ItemPageJacketsJupiterTrainer.URL)
        page.open()
    with allure.step("Выбрать размер'S'"):
        page.size_item().click()
    with allure.step("Выбрать цвет 'Green'"):
        page.color_item().click()
    with allure.step("Ввести в поле 'Qty' '3'"):
        page.qty_item().clear()
        page.qty_item().send_keys('3')
    with allure.step("Нажать на кнопку 'Add to cart'"):
        page.add_to_cart().click()
    with allure.step("Нажать на ссылку 'Shopping cart'"):
        page.link_shopping_cart().click()
    with allure.step("В 'Summary' на странице корзины не отображается скидка"):
        assert page.discount_display() is False, 'Скидка отображается'




