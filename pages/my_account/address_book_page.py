from selenium.webdriver.common.by import By

from base.seleniumbase import BasePage
from locators.address_book_locators import AddressBookLocators


class AddressBookPage(BasePage):
    URL_USER_HAVE_ADDRESS = "https://magento.softwaretestingboard.com/customer/address/"
    URL_USER_HAS_NO_ADDRESS = "https://magento.softwaretestingboard.com/customer/address/new/"

    def first_name_field(self):
        return self.is_visible(AddressBookLocators.FIRST_NAME_FIELD)

    def last_name_field(self):
        return self.is_visible(AddressBookLocators.LAST_NAME_FIELD)

    def phone_number_field(self):
        return self.is_visible(AddressBookLocators.PHONE_NUMBER_FIELD)

    def street_address_1_field(self):
        return self.is_visible(AddressBookLocators.STREET_1_FIELD)

    def city_field(self):
        return self.is_visible(AddressBookLocators.CITY_FIELD)

    def postcode_field(self):
        return self.is_visible(AddressBookLocators.POSTCODE_FIELD)

    def select_state(self, state):
        self.is_visible(AddressBookLocators.STATE_FIELD_DROPDOWN)
        return self.is_clickable((By.XPATH, f"//select[@id='region_id']/option[text()='{state}']")).click()

    def save_address_button(self):
        return self.is_clickable(AddressBookLocators.SAVE_ADDRESS_BUTTON)

    def clear_field(self, locator):
        return self.is_visible(locator).clear()

    def error_msg_empty_field(self, locator):
        return self.is_visible(locator)

    def additional_address_block(self):
        return self.is_visible(AddressBookLocators.ADDITIONAL_ADDRESS_BLOCK)

    def check_data_availability(self, what, where):
        """what - данные , where -где должны отображаться"""
        for i in what:
            if i not in where:
                return False
        return True

    def check_data_missing(self, what, where):
        """what - данные , where -где должны отображаться"""
        for i in what:
            if i in where:
                return False
        return True

    def edit_specific_address(self, first_name, last_name, phone_number, street, city, postcode):
        self.is_visible(AddressBookLocators.ADDITIONAL_ADDRESS_BLOCK)
        return self.is_visible((By.XPATH,
                                f"//tr[td[text()='{first_name}'] and td[text()='{last_name}'] and td[text()='{phone_number}'] and td[text()='{street}'] and td[text()='{city}'] and td[text()='{postcode}']]/td[@class='col actions']/a[@class = 'action edit']"))

    def delete_specific_address(self, first_name, last_name, phone_number, street, city, postcode):
        self.is_visible(AddressBookLocators.ADDITIONAL_ADDRESS_BLOCK)
        return self.is_visible((By.XPATH,
                                f"//tr[td[text()='{first_name}'] and td[text()='{last_name}'] and td[text()='{phone_number}'] and td[text()='{street}'] and td[text()='{city}'] and td[text()='{postcode}']]/td[@class='col actions']/a[@class = 'action delete']"))

    def ok_button_on_popup(self):
        return self.is_visible(AddressBookLocators.OK_BUTTON_ON_POPUP_WINDOW)

    def use_as_default_shipping_checkbox(self):
        return self.is_clickable(AddressBookLocators.USE_AS_DEFAULT_SHIPPING_CHECKBOX)

    def info_default_shipping(self):
        return self.is_visible(AddressBookLocators.DEFAULT_SHIPPING_ADDRESS_BLOCK).text

    def fill_all_require_fields(self, state, firstname, lastname, phone_number, street_1, city, postcode):
        self.select_state(state)
        self.clear_and_send_keys(self.first_name_field(), firstname)
        self.clear_and_send_keys(self.last_name_field(), lastname)
        self.clear_and_send_keys(self.phone_number_field(), phone_number)
        self.clear_and_send_keys(self.street_address_1_field(), street_1)
        self.clear_and_send_keys(self.city_field(), city)
        self.clear_and_send_keys(self.postcode_field(), postcode)

    def fill_all_require_fields_except_state(self, firstname, lastname, phone_number, street_1, city, postcode):
        self.clear_and_send_keys(self.first_name_field(), firstname)
        self.clear_and_send_keys(self.last_name_field(), lastname)
        self.clear_and_send_keys(self.phone_number_field(), phone_number)
        self.clear_and_send_keys(self.street_address_1_field(), street_1)
        self.clear_and_send_keys(self.city_field(), city)
        self.clear_and_send_keys(self.postcode_field(), postcode)

    def add_new_address(self, state, firstname, lastname, phone_number, street_1, city, postcode):
        self.fill_all_require_fields(state, firstname, lastname, phone_number, street_1, city, postcode)
        self.save_address_button().click()
        self.is_visible(BasePage.MESSAGE_SUCCESS)
