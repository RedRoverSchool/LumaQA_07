import pytest
import allure

from data.fake_data import FakeData
from locators.address_book_locators import AddressBookLocators as AddressForm
from locators.address_book_locators import AddressBookLocators
from locators.checkout_page_locators import MultipleAddressesPageLocators
from pages.cart.cart_page import CartPage
from pages.checkout_page import MultipleAddressesPage
from pages.my_account.address_book_page import AddressBookPage


class TestMultipleAddressCheckout(FakeData):

    @allure.title(" 'Check out with multiple addresses' link")
    @allure.description("Link functionality check.The user does not have any addresses in the account.")
    @allure.tag("shopping cart", "link", "check out with multiple addresses")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "danya-f")
    @allure.testcase("https://trello.com/c/3DOb22Go", "TC_004.011.001")
    def test_link_user_has_no_one_address(self, driver, create_account, add_3_item_to_cart):
        with allure.step('1)Page "Cart" open'):
            page = CartPage(driver, url=CartPage.URL)
            page.open()

        with allure.step('2)Click "Check Out with Multiple Addresses" link'):
            page.checkout_multiple_addresses_link().click()

        with allure.step('3)Assert - checking header text'):
            assert page.header().text == MultipleAddressesPageLocators.TEXT_HEADER_USER_HAS_NO_ONE_ADDRESS, 'Неправильно отображается заголовок страницы'
        with allure.step('4)Assert - checking current url'):
            assert page.current_url == MultipleAddressesPage.URL_CREATE_SHIPPING_ADDRESS, 'Не открылась страница CREATE SHIPPING ADDRESS'

    @allure.title("'Check out with multiple addresses' link")
    @allure.description("Link functionality check.The user has already added at least one address to the Address Book")
    @allure.tag("shopping cart", "link", "check out with multiple addresses")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "danya-f")
    @allure.testcase("https://trello.com/c/tFxUcWAw", "TC_004.011.010")
    def test_link_user_has_an_address(self, driver, create_account, add_3_item_to_cart, add_first_address_in_account):
        with allure.step('1)Page "Cart" open'):
            page = CartPage(driver, url=CartPage.URL)
            page.open()

        with allure.step('2)Click "Check Out with Multiple Addresses" link'):
            page.checkout_multiple_addresses_link().click()

        with allure.step('3)Assert - checking header text'):
            assert page.header().text == MultipleAddressesPageLocators.TEXT_HEADER_USER_HAS_AN_ADDRESS, 'Неправильно отображается заголовок страницы'
        with allure.step('4)Assert - checking current url'):
            assert page.current_url == MultipleAddressesPage.URL_SHIP_TO_MULTIPLE_ADDRESSES, 'Не открылась страница SHIP TO MULTIPLE ADDRESSES'

    @allure.title("Asterisk visibility")
    @allure.description("Checking the presence of '*' near to the required fields name.")
    @allure.tag("check out with multiple addresses", "required fields", "asterisk")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "danya-f")
    @allure.testcase("https://trello.com/c/4e7Ylo8o", "TC_004.011.002")
    @pytest.mark.parametrize('locator, expected', [(AddressForm.LABEL_FIRST_NAME_FIELD, 'First Name *'),
                                                   (AddressForm.LABEL_LAST_NAME_FIELD, 'Last Name *'),
                                                   (AddressForm.LABEL_PHONE_NUMBER_FIELD, 'Phone Number *'),
                                                   (AddressForm.LABEL_STREET_FIELD, 'Street Address *'),
                                                   (AddressForm.LABEL_CITY_FIELD, 'City *'),
                                                   (AddressForm.LABEL_STATE_FIELD, 'State/Province *'),
                                                   (AddressForm.LABEL_POSTCODE_FIELD, 'Zip/Postal Code *'),
                                                   (AddressForm.LABEL_COUNTRY_FIELD, 'Country *')])
    def test_visibility_of_asterisk(self, driver, create_account, add_3_item_to_cart, locator, expected):
        with allure.step('1)Page "Cart" open'):
            page = CartPage(driver, url=CartPage.URL)
            page.open()

        with allure.step('2)Click "Check Out with Multiple Addresses" link'):
            page.checkout_multiple_addresses_link().click()
            page = MultipleAddressesPage(driver, page.current_url)

        with allure.step('3)Assert - checking current url'):
            assert page.current_url == MultipleAddressesPage.URL_CREATE_SHIPPING_ADDRESS, 'Не открылась страница Create Shipping Address'
        with allure.step('4)Assert - checking visible of asterisk'):
            assert page.presence_of_an_asterisk(locator) == expected, f'У поля {expected[:-2]} нету *'

    @allure.title("Error message visibility")
    @allure.description("Checking the visibility of an error message when a required field is empty")
    @allure.tag("check out with multiple addresses", "required fields", "error message")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "danya-f")
    @allure.testcase("https://trello.com/c/Cwm9cNC0", "TC_004.011.003")
    @pytest.mark.parametrize('locator, expected',
                             [(AddressForm.FIRST_NAME_FIELD, AddressForm.MESSAGE_ERROR_FIRST_NAME_FIELD),
                              (AddressForm.LAST_NAME_FIELD, AddressForm.MESSAGE_ERROR_LAST_NAME_FIELD),
                              (AddressForm.PHONE_NUMBER_FIELD, AddressForm.MESSAGE_ERROR_PHONE_NUMBER_FIELD),
                              (AddressForm.STREET_1_FIELD, AddressForm.MESSAGE_ERROR_STREET_1_FIELD),
                              (AddressForm.CITY_FIELD, AddressForm.MESSAGE_ERROR_CITY_FIELD),
                              (AddressForm.POSTCODE_FIELD, AddressForm.MESSAGE_ERROR_POSTCODE_FIELD)])
    def test_error_message_empty_field(self, driver, create_account, add_3_item_to_cart, locator, expected):
        with allure.step('1)Page "Cart" open'):
            page = CartPage(driver, url=CartPage.URL)
            page.open()

        with allure.step('2)Click "Check Out with Multiple Addresses" link'):
            page.checkout_multiple_addresses_link().click()
        with allure.step('3)Filling all require fields'):
            page = AddressBookPage(driver, url=page.current_url)
            page.fill_all_require_fields(self.state, self.first_name, self.last_name, self.phone_number,
                                         self.street_address,
                                         self.city, self.postcode)
        with allure.step(f'4)clear {locator} field'):
            page.clear_field(locator)
        with allure.step('5)Click save address button'):
            page.save_address_button().click()

        with allure.step('6)Assert - checking error message visibility'):
            assert page.error_msg_empty_field(
                expected).text == AddressForm.TEXT_ERROR_MSG_EMPTY_FIELD, 'Под обязательным ,пустым полем не появилась ошибка'

    @allure.title("Error message visibility")
    @allure.description("Checking the visibility of the error message when the state is not selected")
    @allure.tag("check out with multiple addresses", "required fields", "error message")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "danya-f")
    @allure.testcase("https://trello.com/c/ayEMoCu6", "TC_004.011.004")
    def test_error_message_state_is_not_selected(self, driver, create_account, add_3_item_to_cart):
        with allure.step('1)Page "Cart" open'):
            page = CartPage(driver, url=CartPage.URL)
            page.open()

        with allure.step('2)Click "Check Out with Multiple Addresses" link'):
            page.checkout_multiple_addresses_link().click()
        with allure.step('3)Filling all require fields,except state selection'):
            page = AddressBookPage(driver, url=page.current_url)
            page.fill_all_require_fields_except_state(self.first_name, self.last_name, self.phone_number,
                                                      self.street_address,
                                                      self.city, self.postcode)
        with allure.step('4)Click "save address" button'):
            page.save_address_button().click()

        with allure.step('5)Assert - checking error message visibility'):
            assert page.error_msg_empty_field(
                AddressForm.MESSAGE_ERROR_STATE_FIELD_DROPDOWN).text == AddressForm.TEXT_ERROR_MSG_STATE, 'Штат не выбран , а ошибка не появилась'

    @allure.title("Add one more address")
    @allure.description("Checking the availability of adding multiple addresses to  account for delivery")
    @allure.tag("check out with multiple addresses", "addresses", "address book")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "danya-f")
    @allure.testcase("https://trello.com/c/RSu3tsR0", "TC_004.011.005")
    def test_add_one_more_address(self, driver, create_account, add_3_item_to_cart, add_first_address_in_account):
        with allure.step('1)Page "Cart" open'):
            page = CartPage(driver, url=CartPage.URL)
            page.open()

        with allure.step('2)Click "Check Out with Multiple Addresses" link'):
            page.checkout_multiple_addresses_link().click()
        with allure.step('3)Click "enter a new address" button'):
            page = MultipleAddressesPage(driver, page.current_url)
            page.click_enter_a_new_address_button()
        with allure.step('4)Fill all fields and save new address'):
            AddressBookPage(driver, url=page.current_url).add_new_address(self.state, self.first_name, self.last_name,
                                                                          self.phone_number,
                                                                          self.street_address,
                                                                          self.city, self.postcode)

        with allure.step('5)Assert - checking current url'):
            assert page.current_url == MultipleAddressesPage.URL_SHIP_TO_MULTIPLE_ADDRESSES, 'Не открылась страница Ship to Multiple Addresses'
        with allure.step('6)Assert - checking success message text'):
            assert page.message_success == AddressForm.TEXT_SUCCESS_ADD_ADDRESS, 'Не удалось добавить дополнительный адрес'

    @allure.title("New address availability")
    @allure.description("Checking that the new address added can be selected for delivery")
    @allure.tag("check out with multiple addresses", "addresses", "address book", "shipping addresses")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "danya-f")
    @allure.testcase("https://trello.com/c/TeKHZDMQ", "TC_004.011.006")
    def test_new_address_availability(self, driver, create_account, add_3_item_to_cart, add_first_address_in_account):
        first_name, last_name, phone_number, street, city, postcode = self.first_name, self.last_name, self.phone_number, self.street_address, self.city, self.postcode
        new_address_info = [first_name, last_name, phone_number, street, city, postcode]
        with allure.step('1)Page "Cart" open'):
            page = CartPage(driver, url=CartPage.URL)
            page.open()

        with allure.step('2)Click "Check Out with Multiple Addresses" link'):
            page.checkout_multiple_addresses_link().click()
        with allure.step('3)Click "enter a new address" button'):
            page = MultipleAddressesPage(driver, page.current_url)
            page.click_enter_a_new_address_button()
        with allure.step('4)Fill all fields and save new address'):
            AddressBookPage(driver, url=page.current_url).add_new_address(self.state, first_name, last_name,
                                                                          phone_number,
                                                                          street, city, postcode)
        with allure.step('5)Click "back to cart" link'):
            page.back_to_cart_link().click()
        with allure.step('6)Click "proceed to checkout" button'):
            CartPage(driver, page.current_url).click_proceed_to_checkout_button()

        with allure.step('7)Assert - checking current url'):
            assert page.current_url == page.URL_USER_HAVE_ADDRESS, 'Не открылась страница с выбором шиппинг адреса'
        with allure.step('8)Assert - checking the availability of selecting a new added address as shipping'):
            assert page.check_data_availability(new_address_info,
                                                page.shipping_addresses_block().text), 'новый , добавленный адрес не сохранился'

        with allure.step('9)Click "ship here" button'):
            page.click_ship_here_button(first_name, last_name, street)

        with allure.step('10)Assert - checking that the new added address is selected as the current shipping address'):
            assert page.check_data_availability(new_address_info,
                                                page.current_delivery_address().text), 'не удалось использовать новый добавленный адрес'

    @allure.title("New address availability")
    @allure.description("Checking that the new address added is available in 'My Account'")
    @allure.tag("check out with multiple addresses", "addresses", "address book", "shipping addresses", "my account")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "danya-f")
    @allure.testcase("https://trello.com/c/3nEDMNb6", "TC_004.011.007")
    def test_new_address_availability_from_my_account(self, driver, create_account, add_3_item_to_cart,
                                                      add_first_address_in_account):
        first_name, last_name, phone_number, street, city, postcode = self.first_name, self.last_name, self.phone_number, self.street_address, self.city, self.postcode
        new_address_info = [first_name, last_name, phone_number, street, city, postcode]
        with allure.step('1)Page "Cart" open'):
            page = CartPage(driver, url=CartPage.URL)
            page.open()
        with allure.step('2)Click "Check Out with Multiple Addresses" link'):
            page.checkout_multiple_addresses_link().click()
        with allure.step('3)Click "enter a new address" button'):
            MultipleAddressesPage(driver, page.current_url).click_enter_a_new_address_button()
        with allure.step('4)Fill all fields and save new address'):
            AddressBookPage(driver, url=page.current_url).add_new_address(self.state, *new_address_info)
        with allure.step('5)Open "Address Book" page '):
            page = AddressBookPage(driver, url=AddressBookPage.URL_USER_HAVE_ADDRESS)
            page.open()
        with allure.step('6)Edit added address'):
            page.edit_specific_address(*new_address_info).click()
        with allure.step('7)Click "use as default shipping" checkbox'):
            page.use_as_default_shipping_checkbox().click()
        with allure.step('8)Click "save address" button'):
            page.save_address_button().click()

        with allure.step('9)Assert - checking success message text'):
            assert page.message_success == MultipleAddressesPageLocators.TEXT_SUCCESSFUL_MSG_SAVE_NEW_ADDRESS, 'Не удалось сохранить новый адрес как стандартный для доставки'
        with allure.step('10)Assert - checking that changes in the address have been saved'):
            assert page.check_data_availability(new_address_info,
                                                page.info_default_shipping()), 'Не удалось сохранить новый адрес как стандартный для доставки'

    @allure.title("Availability of address editing")
    @allure.description("Checking that any address can be edited")
    @allure.tag("check out with multiple addresses", "addresses", "address book", "shipping addresses", "my account",
                "edit information")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "danya-f")
    @allure.testcase("https://trello.com/c/8pk3AD3m", "TC_004.011.008")
    def test_availability_of_address_editing(self, driver, create_account, add_3_item_to_cart,
                                             add_first_address_in_account):
        new_first_name, new_last_name, new_phone_number, new_street, new_city, new_postcode = self.first_name, self.last_name, self.phone_number, self.street_address, self.city, self.postcode
        old_first_name, old_last_name, old_phone_number, old_street, old_city, old_postcode = self.first_name, self.last_name, self.phone_number, self.street_address, self.city, self.postcode
        new_address_info = [new_first_name, new_last_name, new_phone_number, new_street, new_city, new_postcode]
        with allure.step('1)Page "Cart" open'):
            page = CartPage(driver, url=CartPage.URL)
            page.open()

        with allure.step('2)Click "Check Out with Multiple Addresses" link'):
            page.checkout_multiple_addresses_link().click()
        with allure.step('3)Click "enter a new address" button'):
            page = MultipleAddressesPage(driver, page.current_url)
            page.click_enter_a_new_address_button()
        with allure.step('4)Fill all fields and save new address'):
            AddressBookPage(driver, url=page.current_url).add_new_address(self.state, old_first_name, old_last_name,
                                                                          old_phone_number, old_street, old_city,
                                                                          old_postcode)
        with allure.step('5)Select added address from the drop-down'):
            page.select_address_from_dropdown_send_to(old_first_name, old_last_name, old_postcode).click()
        with allure.step('6)Click "go to shipping information" button'):
            page.click_go_to_shipping_info_button()
        with allure.step('7)Click "change" button for added address'):
            page.change_button_for_a_specifically_address(old_first_name, old_last_name, old_phone_number).click()
        with allure.step('8)Edit added address and click "Save address" button'):
            AddressBookPage(driver, url=page.current_url).add_new_address(self.state, *new_address_info)

        with allure.step('9)Assert - checking current url'):
            assert page.current_url == MultipleAddressesPage.URL_SELECT_SHIPPING_METHOD, 'не произошло перенаправление после сохранения изменений адреса'
        with allure.step('10)Assert - checking success message text'):
            assert page.message_success == MultipleAddressesPageLocators.TEXT_SUCCESSFUL_MSG_SAVE_NEW_ADDRESS, 'Не появилось сообщени об успешном сохранении изменений адреса'
        with allure.step('11)Assert - checking that changes in the address have been saved'):
            assert page.check_data_availability(new_address_info,
                                                page.select_shipping_method_block().text), 'Изменения данных в адресе не сохранились'

    @allure.title("Availability of address deleting")
    @allure.description("Checking that any address can be deleted")
    @allure.tag("check out with multiple addresses", "addresses", "address book")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "danya-f")
    @allure.testcase("https://trello.com/c/wns7Fzzo", "TC_004.011.009")
    def test_availability_deleting_of_any_address(self, driver, create_account, add_3_item_to_cart,
                                                  add_first_address_in_account):
        first_name, last_name, phone_number, street, city, postcode = self.first_name, self.last_name, self.phone_number, self.street_address, self.city, self.postcode
        deleting_address_info = [first_name, last_name, phone_number, street, city, postcode]
        with allure.step('1)Page "Cart" open'):
            page = CartPage(driver, url=CartPage.URL)
            page.open()

        with allure.step('2)Click "Check Out with Multiple Addresses" link'):
            page.checkout_multiple_addresses_link().click()
        with allure.step('3)Click "enter a new address" button'):
            page = MultipleAddressesPage(driver, page.current_url)
            page.click_enter_a_new_address_button()
        with allure.step('4)Fill all fields and save new address'):
            AddressBookPage(driver, url=page.current_url).add_new_address(self.state, *deleting_address_info)
        with allure.step('5)Open "Address Book" page '):
            page = AddressBookPage(driver, url=AddressBookPage.URL_USER_HAVE_ADDRESS)
            page.open()
        with allure.step('6)Click "Delet" button for added address'):
            page.delete_specific_address(*deleting_address_info).click()
        with allure.step('7)Click "OK" button on pop-up window'):
            page.ok_button_on_popup().click()
        with allure.step('8)Save all addresses info from account to variable'):
            saved_additional_addresses = AddressBookPage(driver, url=page.current_url).additional_address_block().text

        with allure.step('9)Assert - checking success message text'):
            assert page.message_success == AddressBookLocators.TEXT_SUCCESS_DELETE_ADDRESS, 'Нет сообщения об успешном удалении адреса'
        with allure.step('9)Assert - checking the unavailability of a deleted address'):
            assert page.check_data_missing(deleting_address_info, saved_additional_addresses), 'Не удалось удалить адрес'
