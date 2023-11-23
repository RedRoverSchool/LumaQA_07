from pages.item_page import ItemPageJacketsJupiterTrainer


def test_discount_check(driver):
    page = ItemPageJacketsJupiterTrainer(driver, url=ItemPageJacketsJupiterTrainer.URL)
    page.open()
    page.size_item().click()
    page.color_item().click()
    page.qty_item().clear()
    page.qty_item().send_keys('4')
    page.add_to_cart().click()
    page.link_shopping_cart().click()
    assert page.discount_in_summary() > 0, 'Нет скидки'
    assert round(page.subtotal() * 0.2, 2) == page.discount_in_summary(), 'Не верно отображается скидка'


def test_discount_check_under_200(driver):
    page = ItemPageJacketsJupiterTrainer(driver, url=ItemPageJacketsJupiterTrainer.URL)
    page.open()
    page.size_item().click()
    page.color_item().click()
    page.qty_item().clear()
    page.qty_item().send_keys('3')
    page.add_to_cart().click()
    page.link_shopping_cart().click()
    assert page.discount_display() is False, 'Скидка отображается'




