from locators.cart_page_locators import CartPageLocators
from pages.cart.cart_page import AddItemToCart, CartPage, UpdateItem


def test_edit_item_color(driver):
    page = AddItemToCart(driver, url=CartPageLocators.URL_ITEM_DEIRDRE_RELAXED)
    page.open()
    page.size_28().click()
    page.color_grey_item().click()
    page.add_to_cart().click()
    assert page.message_success == 'You added Deirdre Relaxed-Fit Capri to your shopping cart.'
    page = CartPage(driver, url=CartPageLocators.URL_CART_PAGE)
    page.open()
    page.button_edit_item().click()
    page = UpdateItem(driver, url='')
    page.size_29().click()
    page.color_blue().click()
    page.update_cart().click()
    page = CartPage(driver, url='')
    assert '29' in page.item_options().text, 'Размер не изменен'
    assert 'Blue' in page.item_options().text, 'Цвет не изменен'
    assert page.message_success == 'Deirdre Relaxed-Fit Capri was updated in your shopping cart.', 'Сообщение не появилось'


