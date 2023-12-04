from locators.wish_list_locators import WishListLocators


class TestWishList():

    def test_visibility_items_left_corner(self, driver, open_main_page, sign_in, add_items_to_wish_list):
        wish_list_elements = driver.find_elements(*WishListLocators.WISH_LIST_SIDEBAR_ITEMS)
        wish_list = [element.text for element in wish_list_elements]
        assert len(wish_list) >= 1, "Items not found"


