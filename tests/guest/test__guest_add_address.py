from random import choice
from data.fake_data import FakeData
from pages.checkout_page import GuestShippingAddressPage
from pages.item_page import ItemPage


class TestX(FakeData):
    def test_guest_add_shipping_address_with_select_state(self, driver):
        # page = ItemDetailsPage(driver)
        # page.add_to_cart().click()
        # assert page.msg == ItemDetailsPage.SUCCESS

        page = ItemPage(driver, url=ItemPage.URL_DRIVEN_BACKPACK)
        page.open()
        page.add_driven_backpack_from_item_card_to_cart(3)


        page = GuestShippingAddressPage(driver)
        # page.is_loading()

        page.email = self.email
        # page.is_loading()

        page.first_name = self.first_name
        page.last_name = self.last_name
        page.company = self.company

        page.country = choice(GuestShippingAddressPage.WITH_REGIONS)
        page.state = (state := choice(page.state[1:]))
        page.city = (city := self.city)
        page.postcode = (postcode := self.postcode)
        page.street_1 = self.secondary_address
        page.street_2 = self.street_address
        page.street_3 = f"{city} {state} {postcode}"
        page.telephone = self.phone_number
        # page.is_loading()
        page.shipping_method().click()

        page.button_next().click()
        page.wait_close_loader_one()

        page.redirect(GuestShippingAddressPage.URL_DONE)
        assert page.current_url == GuestShippingAddressPage.URL_DONE
