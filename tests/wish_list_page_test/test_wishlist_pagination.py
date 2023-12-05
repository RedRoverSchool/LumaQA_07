import allure

from locators.wish_list_locators import WishListLocators
from pages.item_page import ItemDetailsPage
from pages.my_account.my_wish_list_page import MyWishListPage


@allure.title("Проверка пагинации")
@allure.description("Если выбрано показать 10 товаров на странице при добавлении 11 товара появляется пагинация")
@allure.tag("Wishlist")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Sviatlana Kot")
@allure.testcase("https://trello.com/c/nLlAVwNm", "TC_014.002.001")
def test_check_pagination(driver, sign_in_wish_list):
    with allure.step('Добавляем один товар'):
        page = ItemDetailsPage(driver, url='https://magento.softwaretestingboard.com/juno-jacket.html')
    page.add_to_wish_list().click()
    assert page.message.endswith('has been added to your Wish List. Click here to continue shopping.')
    page = MyWishListPage(driver, url=MyWishListPage.URL)
    with allure.step('Выбираем показать 10 товаров на странице'):
        page.select_show_items_limiter().select_by_visible_text('10')
    with allure.step("Ожидаемый результат: Пагинация появляется на странице"):
        assert page.item_count(WishListLocators.PAGINATION) > 0, 'Пагинация не отображается'

