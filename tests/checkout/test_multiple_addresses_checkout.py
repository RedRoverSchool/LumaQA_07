import pytest

from data.fake_data import FakeData
from locators.address_book_locators import AddressBookLocators as AddressForm
from locators.address_book_locators import AddressBookLocators
from locators.checkout_page_locators import MultipleAddressesPageLocators
from pages.cart.cart_page import CartPage
from pages.checkout_page import MultipleAddressesPage
from pages.my_account.address_book_page import AddressBookPage


class TestMultipleAddressCheckout(FakeData):

    def test_link_user_has_no_one_address(self, driver, create_account, add_3_item_to_cart):
        """TC_004.011.001"""
        page = CartPage(driver, url=CartPage.URL)
        page.open()

        page.checkout_multiple_addresses_link().click()

        assert page.header().text == MultipleAddressesPageLocators.TEXT_HEADER_USER_HAS_NO_ONE_ADDRESS, 'Неправильно отображается заголовок страницы'
        assert page.current_url == MultipleAddressesPage.URL_CREATE_SHIPPING_ADDRESS, 'Не открылась страница CREATE SHIPPING ADDRESS'

    def test_link_user_has_an_address(self, driver, create_account, add_3_item_to_cart, add_first_address_in_account):
        """TC_004.011.001"""
        page = CartPage(driver, url=CartPage.URL)
        page.open()

        page.checkout_multiple_addresses_link().click()

        assert page.header().text == MultipleAddressesPageLocators.TEXT_HEADER_USER_HAS_AN_ADDRESS, 'Неправильно отображается заголовок страницы'
        assert page.current_url == MultipleAddressesPage.URL_SHIP_TO_MULTIPLE_ADDRESSES, 'Не открылась страница SHIP TO MULTIPLE ADDRESSES'

    @pytest.mark.parametrize('locator, expected', [(AddressForm.LABEL_FIRST_NAME_FIELD, 'First Name *'),
                                                   (AddressForm.LABEL_LAST_NAME_FIELD, 'Last Name *'),
                                                   (AddressForm.LABEL_PHONE_NUMBER_FIELD, 'Phone Number *'),
                                                   (AddressForm.LABEL_STREET_FIELD, 'Street Address *'),
                                                   (AddressForm.LABEL_CITY_FIELD, 'City *'),
                                                   (AddressForm.LABEL_STATE_FIELD, 'State/Province *'),
                                                   (AddressForm.LABEL_POSTCODE_FIELD, 'Zip/Postal Code *'),
                                                   (AddressForm.LABEL_COUNTRY_FIELD, 'Country *')])
    def test_visibility_of_asterisk(self, driver, create_account, add_3_item_to_cart, locator, expected):
        """TC_004.011.002"""
        page = CartPage(driver, url=CartPage.URL)
        page.open()

        page.checkout_multiple_addresses_link().click()
        page = MultipleAddressesPage(driver, page.current_url)

        assert page.current_url == MultipleAddressesPage.URL_CREATE_SHIPPING_ADDRESS, 'Не открылась страница Create Shipping Address'
        assert page.presence_of_an_asterisk(locator) == expected, f'У поля {expected[:-2]} нету *'

    @pytest.mark.parametrize('locator, expected',
                             [(AddressForm.FIRST_NAME_FIELD, AddressForm.MESSAGE_ERROR_FIRST_NAME_FIELD),
                              (AddressForm.LAST_NAME_FIELD, AddressForm.MESSAGE_ERROR_LAST_NAME_FIELD),
                              (AddressForm.PHONE_NUMBER_FIELD, AddressForm.MESSAGE_ERROR_PHONE_NUMBER_FIELD),
                              (AddressForm.STREET_1_FIELD, AddressForm.MESSAGE_ERROR_STREET_1_FIELD),
                              (AddressForm.CITY_FIELD, AddressForm.MESSAGE_ERROR_CITY_FIELD),
                              (AddressForm.POSTCODE_FIELD, AddressForm.MESSAGE_ERROR_POSTCODE_FIELD)])
    def test_error_message_empty_field(self, driver, create_account, add_3_item_to_cart, locator, expected):
        """TC_004.011.003"""
        page = CartPage(driver, url=CartPage.URL)
        page.open()

        page.checkout_multiple_addresses_link().click()
        page = AddressBookPage(driver, url=page.current_url)
        page.fill_all_require_fields(self.state, self.first_name, self.last_name, self.phone_number,
                                     self.street_address,
                                     self.city, self.postcode)
        page.clear_field(locator)
        page.save_address_button().click()

        assert page.error_msg_empty_field(
            expected).text == AddressForm.TEXT_ERROR_MSG_EMPTY_FIELD, 'Под обязательным ,пустым полем не появилась ошибка'

    def test_error_message_state_is_not_selected(self, driver, create_account, add_3_item_to_cart):
        """TC_004.011.004"""
        page = CartPage(driver, url=CartPage.URL)
        page.open()

        page.checkout_multiple_addresses_link().click()
        page = AddressBookPage(driver, url=page.current_url)
        page.fill_all_require_fields_except_state(self.first_name, self.last_name, self.phone_number,
                                                  self.street_address,
                                                  self.city, self.postcode)
        page.save_address_button().click()

        assert page.error_msg_empty_field(
            AddressForm.MESSAGE_ERROR_STATE_FIELD_DROPDOWN).text == AddressForm.TEXT_ERROR_MSG_STATE, 'Штат не выбран , а ошибка не появилась'

    def test_add_one_more_address(self, driver, create_account, add_3_item_to_cart, add_first_address_in_account):
        """TC_004.011.005"""
        page = CartPage(driver, url=CartPage.URL)
        page.open()

        page.checkout_multiple_addresses_link().click()
        page = MultipleAddressesPage(driver, page.current_url)
        page.enter_a_new_address_button().click()
        page.wait_overlay_closed()
        AddressBookPage(driver, url=page.current_url).add_new_address(self.state, self.first_name, self.last_name,
                                                                      self.phone_number,
                                                                      self.street_address,
                                                                      self.city, self.postcode)

        assert page.current_url == MultipleAddressesPage.URL_SHIP_TO_MULTIPLE_ADDRESSES, 'Не открылась страница Ship to Multiple Addresses'
        assert page.message_success == AddressForm.TEXT_SUCCESS_ADD_ADDRESS, 'Не удалось добавить дополнительный адрес'

    def test_new_address_availability(self, driver, create_account, add_3_item_to_cart, add_first_address_in_account):
        """TC_004.011.006"""
        first_name, last_name, phone_number, street, city, postcode = self.first_name, self.last_name, self.phone_number, self.street_address, self.city, self.postcode
        new_address_info = [first_name, last_name, phone_number, street, city, postcode]
        page = CartPage(driver, url=CartPage.URL)
        page.open()

        page.checkout_multiple_addresses_link().click()
        page = MultipleAddressesPage(driver, page.current_url)
        page.enter_a_new_address_button().click()
        page.wait_overlay_closed()
        AddressBookPage(driver, url=page.current_url).add_new_address(self.state, first_name, last_name, phone_number,
                                                                      street, city, postcode)
        page.back_to_cart_link().click()
        CartPage(driver, page.current_url).proceed_to_checkout_button().click()

        assert page.current_url == page.URL_USER_HAVE_ADDRESS, 'Не открылась страница с выбором шиппинг адреса'
        assert page.check_data_availability(new_address_info,
                                            page.additional_address().text), 'новый , добавленный адрес не сохранился'

        page.ship_here_button().click()
        page.wait_overlay_closed()

        assert page.check_data_availability(new_address_info,
                                            page.current_delivery_address().text), 'не удалось использовать новый добавленный адрес'

    def test_new_address_availability_from_my_account(self, driver, create_account, add_3_item_to_cart,
                                                      add_first_address_in_account):
        """TC_004.011.007"""
        first_name, last_name, phone_number, street, city, postcode = self.first_name, self.last_name, self.phone_number, self.street_address, self.city, self.postcode
        new_address_info = [first_name, last_name, phone_number, street, city, postcode]
        page = CartPage(driver, url=CartPage.URL)
        page.open()

        page.checkout_multiple_addresses_link().click()
        MultipleAddressesPage(driver, page.current_url).enter_a_new_address_button().click()
        page.wait_overlay_closed()
        AddressBookPage(driver, url=page.current_url).add_new_address(self.state, *new_address_info)
        page = AddressBookPage(driver, url=AddressBookPage.URL_USER_HAVE_ADDRESS)
        page.open()
        page.edit_specific_address(*new_address_info).click()
        page.use_as_default_shipping_checkbox().click()
        page.save_address_button().click()

        assert page.message_success == MultipleAddressesPageLocators.TEXT_SUCCESSFUL_MSG_SAVE_NEW_ADDRESS, 'Не удалось сохранить новый адрес как стандартный для доставки'
        assert page.check_data_availability(new_address_info,
                                            page.info_default_shipping()), 'Не удалось сохранить новый адрес как стандартный для доставки'

    def test_availability_of_address_editing(self, driver, create_account, add_3_item_to_cart,
                                             add_first_address_in_account):
        """TC_004.011.008"""
        new_first_name, new_last_name, new_phone_number, new_street, new_city, new_postcode = self.first_name, self.last_name, self.phone_number, self.street_address, self.city, self.postcode
        old_first_name, old_last_name, old_phone_number, old_street, old_city, old_postcode = self.first_name, self.last_name, self.phone_number, self.street_address, self.city, self.postcode
        new_address_info = [new_first_name, new_last_name, new_phone_number, new_street, new_city, new_postcode]
        page = CartPage(driver, url=CartPage.URL)
        page.open()

        page.checkout_multiple_addresses_link().click()
        page = MultipleAddressesPage(driver, page.current_url)
        page.enter_a_new_address_button().click()
        page.wait_overlay_closed()
        AddressBookPage(driver, url=page.current_url).add_new_address(self.state, old_first_name, old_last_name,
                                                                      old_phone_number, old_street, old_city,
                                                                      old_postcode)
        page.select_address_from_dropdown_send_to(old_first_name, old_last_name, old_postcode).click()
        page.go_to_shipping_info_button().click()
        page.wait_overlay_closed()
        page.change_button_for_a_specifically_address(old_first_name, old_last_name, old_phone_number).click()
        AddressBookPage(driver, url=page.current_url).add_new_address(self.state, *new_address_info)

        assert page.current_url == MultipleAddressesPage.URL_SELECT_SHIPPING_METHOD, 'не произошло перенаправление после сохранения изменений адреса'
        assert page.message_success == MultipleAddressesPageLocators.TEXT_SUCCESSFUL_MSG_SAVE_NEW_ADDRESS, 'Не появилось сообщени об успешном сохранении изменений адреса'
        assert page.check_data_availability(new_address_info,
                                            page.select_shipping_method_block().text), 'Изменения данных в адресе не сохранились'

    def test_availability_deleting_of_any_address(self, driver, create_account, add_3_item_to_cart,
                                                  add_first_address_in_account):
        """TC_004.011.009"""
        first_name, last_name, phone_number, street, city, postcode = self.first_name, self.last_name, self.phone_number, self.street_address, self.city, self.postcode
        deleting_address_info = [first_name, last_name, phone_number, street, city, postcode]
        page = CartPage(driver, url=CartPage.URL)
        page.open()

        page.checkout_multiple_addresses_link().click()
        page = MultipleAddressesPage(driver, page.current_url)
        page.enter_a_new_address_button().click()
        page.wait_overlay_closed()
        AddressBookPage(driver, url=page.current_url).add_new_address(self.state, *deleting_address_info)
        page = AddressBookPage(driver, url=AddressBookPage.URL_USER_HAVE_ADDRESS)
        page.open()
        page.delete_specific_address(*deleting_address_info).click()
        page.ok_button_on_popup().click()
        saved_additional_addresses = AddressBookPage(driver, url=page.current_url).additional_address_block().text

        assert page.message_success == AddressBookLocators.TEXT_SUCCESS_DELETE_ADDRESS, 'Нет сообщения об успешном удалении адреса'
        assert page.check_data_missing(deleting_address_info, saved_additional_addresses), 'Не удалось удалить адрес'
