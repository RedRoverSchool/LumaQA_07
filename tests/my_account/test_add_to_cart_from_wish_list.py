from pages.item_page import ItemDetailsPage
from pages.my_account.my_wish_list_page import MyWishListPage


def test_add_to_cart_from_wish_list(driver, create_account, add_items_to_wish_list):
    page = MyWishListPage(driver, url=MyWishListPage.URL)
    page.open()
    page.all_to_cart().click()
    assert page.message_success == '1 product(s) have been added to shopping cart: "Clamber Watch".'
    errors = page.messages_error_list
    assert 'You need to choose options for your item for "Breathe-Easy Tank".' in errors
    assert 'The requested qty is not available for "Push It Messenger Bag".' in errors
    assert 'You need to choose options for your item for "Ina Compression Short".' in errors
    assert 'You need to choose options for your item for "Tiffany Fitness Tee".' in errors
    assert 'You need to choose options for your item for "Ida Workout Parachute Pant".' in errors

