from random import choice
from time import sleep

import pytest

from data.fake_data import FakeData
from pages.checkout_page import GuestShippingAddressPage
from pages.item_page import ItemPage, ItemDetailsPage


class TestX(FakeData):
    # @pytest.mark.debug
    def test_guest_add_shipping_address_with_select_state(self, driver):
        page = ItemDetailsPage(driver)
        page.add_to_cart().click()
        assert page.message_success == ItemDetailsPage.SUCCESS

        # page = ItemPage(driver, url=ItemPage.URL_DRIVEN_BACKPACK)
        # page.open()
        # page.add_driven_backpack_from_item_card_to_cart(3)

        page = GuestShippingAddressPage(driver)

        page.is_invisible(page.CHECKOUT_LOADER)
        page.email = self.email
        page.the_presence_of_element_located(page.EMAIL_POST)
        page.is_invisible(page.EMAIL_POST)

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

        page.shipping_method().click()

        page.button_next().click()

        page.redirect(GuestShippingAddressPage.URL_DONE)
        assert page.current_url == GuestShippingAddressPage.URL_DONE
