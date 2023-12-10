import time

import allure
from data.fake_data import FakeData

from pages.main_page import MainPage
from pages.account.create_account import CreateAccountPage
from pages.account.account_edit import AccountEditPage
from pages.account.account_add_address import AddressAddPage

from locators.base_page_locators import BasePageLocators as bpl
from locators.my_account_page_locators import MyAccountPageLocators as mapl
from locators.address_book_locators import AddressBookLocators as apl

class TestMyAccountDataEditing(FakeData):
    @allure.title("TC_004.015.007 | Authorization> User's account > My account > Changing password > Positive")
    @allure.tag("Authorization", "My account", "Changing password")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "valdemards")
    @allure.testcase("https://trello.com/c/UbzNXcU5/319-tc004015007-authorization-users-account-my-account-changing-password-positive", "TC_004.015.007")
    def test_change_password_positive(self, driver):
        password_current = CreateAccountPage(driver).password
        page = AccountEditPage(driver, MainPage.URL)
        # png_bytes = driver.get_screenshot_as_png()
        # allure.attach(png_bytes, name='test', attachment_type=allure.attachment_type.PNG)
        with allure.step("Click “Welcome,…” dropdown menu"):
            page.is_clickable(bpl.WELCOME_MENU_BUTTON).click()
        with allure.step("Choose “My account” option"):
            page.is_clickable(bpl.WELCOME_MENU_MY_ACCOUNT_BUTTON).click()
        with allure.step("Click “Change Password” button"):
            page.is_clickable(mapl.CHANGE_PASSWORD_BUTTON).click()
        with allure.step("Type current account password in “Current Password” field of “Change Password” block"):
            page.password_current = password_current
        with allure.step("Type new password in “New Password” field of “Change Password” block"):
            page.password = (password_new := self.password)
        with allure.step("Type the same new password in “Confirm New Password” field of “Change Password” block"):
            page.password_confirm = password_new
        with allure.step("Click “Save” button"):
            page.save().click()
        with allure.step("You saved the account information” alert is visible"):
            assert page.message_success == AccountEditPage.SUCCESS, "Message not as expected"

    @allure.title("TC_004.015.008 | Authorization> User's account > My account > Changing password > Negative")
    @allure.tag("Authorization", "My account", "Changing password")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "valdemards")
    @allure.testcase("https://trello.com/c/azxh1osn/322-tc004015008-authorization-users-account-my-account-changing-password-negative", "TC_004.015.008")
    def test_change_password_negative(self, driver):
        password_current = CreateAccountPage(driver).password
        page = AccountEditPage(driver, MainPage.URL)
        with allure.step("Click “Welcome,…” dropdown menu"):
            page.is_clickable(bpl.WELCOME_MENU_BUTTON).click()
        with allure.step("Choose “My account” option"):
            page.is_clickable(bpl.WELCOME_MENU_MY_ACCOUNT_BUTTON).click()
        with allure.step("Click “Change Password” button"):
            page.is_clickable(mapl.CHANGE_PASSWORD_BUTTON).click()
        with allure.step("Type “ “ in “Current Password” field of “Change Password” block"):
            page.password_current = ' '
        with allure.step("Type “ “ in “New Password” field of “Change Password” block"):
            page.password = (password_new := ' ')
        with allure.step("Type” “ in “Confirm New Password” field of “Change Password” block"):
            page.password_confirm = password_new
        with allure.step(" Click “Save” button"):
            page.save().click()
        with allure.step("“This is a required field.“ alert under “Current Password” field of “Change Password” block is displayed"):
            assert page.message_current_password_error() == AccountEditPage.CHANGE_PASSWORD_ERROR
        with allure.step("“This is a required field.“ alert under “New Password” field of “Change Password” block is displayed"):
            assert page.message_change_password_error() == AccountEditPage.CHANGE_PASSWORD_ERROR
        with allure.step("“This is a required field.“ alert under “Confirm New Password” field of “Change Password” block is displayed"):
            assert page.message_confirm_change_password_error() == AccountEditPage.CHANGE_PASSWORD_ERROR

    @allure.title("TC_004.015.005 | Authorization> User's account > My account > Contact information editing > Positive")
    @allure.tag("Authorization", "My account", "Edit contact information")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "valdemards")
    @allure.testcase(
        "https://trello.com/c/VE2067zt/321-tc004015005-authorization-users-account-my-account-contact-information-editing-positive",
        "TC_004.015.005")
    def test_edit_contact_information_positive(self, driver):
        current_password = CreateAccountPage(driver).password
        page = AccountEditPage(driver, MainPage.URL)

        with allure.step('Click “Welcome,…” dropdown menu'):
            page.is_clickable(bpl.WELCOME_MENU_BUTTON).click()
        with allure.step('Choose “My account” option'):
            page.is_clickable(bpl.WELCOME_MENU_MY_ACCOUNT_BUTTON).click()
        with allure.step('Click “Edit” button'):
            page.is_clickable(mapl.EDIT_BUTTON).click()
        with allure.step('Type “Bob” in “First Name” field of “Account Information” block'):
            page.first_name = 'Bob'
        with allure.step('Type “Ivanov” in “LastName” field of “Account Information” block'):
            page.last_name = 'Ivanov'
        with allure.step('Check “Change Email” checkbox'):
            page.change_email().click()
        with allure.step('Type new email in “Email” field of “Change Email” block'):
            page.email = self.email
        with allure.step('Type current account password in “Current Password” field of “Change Email” block'):
            page.password_current = current_password
        with allure.step('Click “Save” button'):
            page.save().click()
        with allure.step('“You saved the account information” alert is visible'):
            assert page.message == AccountEditPage.SUCCESS, 'Couldn\'t change contact information'

    @allure.title("TC_004.015.010 | Authorization> User's account > My account > Adding new address > Positive")
    @allure.tag("Authorization", "My account", "Add new address")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "valdemards")
    @allure.testcase(
        "https://trello.com/c/V3z2NigL/326-tc004015010-authorization-users-account-my-account-adding-new-address-positive",
        "TC_004.015.010")
    def test_add_new_address_positive(self, driver):
        CreateAccountPage(driver)
        page = AddressAddPage(driver, MainPage.URL)
        with allure.step('Click “Welcome,…” dropdown menu'):
            page.is_clickable(bpl.WELCOME_MENU_BUTTON).click()
        with allure.step('Choose “My account” option'):
            page.is_clickable(bpl.WELCOME_MENU_MY_ACCOUNT_BUTTON).click()
        with allure.step('Click “Manage Addresses” button in “Address Book” block'):
            page.is_clickable(mapl.MANAGE_ADDRESSES_BUTTON).click()
        with allure.step('Type “street 6” in upper “Street Address” field of “Address” block'):
            page.street_1 = 'street 6'
        with allure.step('Type “city” in “City” field of “Address” block'):
            page.city = 'city'
        with allure.step('Choose “Alabama” in “State/Province” dropdown menu of “Address” block'):
            page.state = 'Alabama'
        with allure.step('Type “12345” in “Zip/Postal Code” field of “Address” block'):
            page.postcode = '12345'
        with allure.step('Type “123” in “Phone Number” field of “Contact information” block'):
            page.telephone = '123'
        with allure.step('Click “Save Address” button'):
            page.save().click()
        with allure.step('You saved the address.” alert is visible'):
            assert page.message_success == AddressAddPage.SUCCESS, 'Couldn\'t add new address'

    @allure.title("TC_004.015.011 | Authorization> User's account > My account > Adding new address > Negative")
    @allure.tag("Authorization", "My account", "Add new address")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "valdemards")
    @allure.testcase(
        "https://trello.com/c/bk23eFop/327-tc004015011-authorization-users-account-my-account-adding-new-address-negative",
        "TC_004.015.011")
    def test_add_new_address_negative(self, driver):
        CreateAccountPage(driver)
        page = AddressAddPage(driver, MainPage.URL)
        with allure.step('Click “Welcome,…” dropdown menu'):
            page.is_clickable(bpl.WELCOME_MENU_BUTTON).click()
        with allure.step('Choose “My account” option'):
            page.is_clickable(bpl.WELCOME_MENU_MY_ACCOUNT_BUTTON).click()
        with allure.step('Click “Manage Addresses” button in “Address Book” block'):
            page.is_clickable(mapl.MANAGE_ADDRESSES_BUTTON).click()
        with allure.step('Type “ ” in upper “Street Address” field of “Address” block'):
            page.street_1 = ' '
        with allure.step('Type “ ” in “City” field of “Address” block'):
            page.city = ' '
        with allure.step('Type “ ” in “Zip/Postal Code” field of “Address” block'):
            page.postcode = ' '
        with allure.step('Type “ ” in “Phone Number” field of “Contact information” block'):
            page.telephone = ' '
        with allure.step('Click “Save Address” button'):
            page.save().click()
        with allure.step('“This is a required field.“  alert under “Street Address” field of “Address” block is displayed'):
            assert page.message_street_1_error() == AddressAddPage.REQUIRED_FIELD_ERROR
        with allure.step('“This is a required field.“  alert under “City” field of “Address” block is displayed'):
            assert page.message_city_error() == AddressAddPage.REQUIRED_FIELD_ERROR
        with allure.step('“Please select an option“  alert under “State/Province” dropdown menu of “Address” block is displayed'):
            assert page.message_state_error() == AddressAddPage.PLEASE_SELECT_ERROR
        with allure.step('“This is a required field.“  alert under “Zip/Postal Code” field of “Address” block is displayed'):
            assert page.message_postal_error() == AddressAddPage.REQUIRED_FIELD_ERROR
        with allure.step('“This is a required field.“  alert under “Phone Number” field of “Contact Information” block is displayed'):
            assert page.message_phone_error() == AddressAddPage.REQUIRED_FIELD_ERROR

    @allure.title("TC_004.015.013|Authorization>User's account>My account>Default Billing Address editing > Positive")
    @allure.tag("Authorization", "My account", "Default Billing Address")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "valdemards")
    @allure.testcase(
        "https://trello.com/c/gNu1iKfr/329-tc004015013-authorization-users-account-my-account-default-billing-address-editing-positive",
        "TC_004.015.013")
    def test_edit_default_billing_address_positive(self, driver):
        CreateAccountPage(driver)
        page = AddressAddPage(driver, MainPage.URL)
        with allure.step('Click “Welcome,…” dropdown menu'):
            page.is_clickable(bpl.WELCOME_MENU_BUTTON).click()
        with allure.step('Choose “My account” option'):
            page.is_clickable(bpl.WELCOME_MENU_MY_ACCOUNT_BUTTON).click()
        with allure.step('Click “Edit Address” button in “Default Billing Address” section of “Address Book” block'):
            page.is_clickable(mapl.EDIT_BILLING_ADDRESS_BUTTON).click()
        with allure.step('Type “street 7” in upper “Street Address” field of “Address” block'):
            page.street_1 = 'street 7'
        with allure.step('Type “city” in “City” field of “Address” block'):
            page.city = 'city'
        with allure.step('Choose “Alabama” in “State/Province” dropdown menu of “Address” block'):
            page.state = 'Alabama'
        with allure.step('Type “12345” in “Zip/Postal Code” field of “Address” block'):
            page.postcode = '12345'
        with allure.step('Type “123” in “Phone Number” field of “Contact information” block'):
            page.telephone = '123'
        with allure.step('Click “Save Address” button'):
            page.save().click()
        default_billing_address = page.is_visible(apl.DEFAULT_BILLING_ADDRESS_BLOCK).text.split('\n')
        with allure.step('New Street address, city, state,zip code, country and phone are visible in “Default Billing Address” section'):
            assert default_billing_address[2] == 'street 7', 'Wrong data in Street 1 field'
            assert default_billing_address[3].split(',')[0] == 'city', 'Wrong data in City field'
            assert default_billing_address[3].split(', ')[1] == 'Alabama', 'Wrong data in State field'
            assert default_billing_address[3].split(', ')[2] == '12345', 'Wrong data in street Postal code field'
            assert default_billing_address[5].split(': ')[1] == '123', 'Wrong data in Phone field'

    @allure.title("TC_004.015.014 | Authorization> User's account > My account > Default Billing Address editing > Negative")
    @allure.tag("Authorization", "My account", "Default Billing Address")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "valdemards")
    @allure.testcase(
        "https://trello.com/c/OvYteebG/330-tc004015014-authorization-users-account-my-account-default-billing-address-editing-negative",
        "TC_004.015.014")
    def test_edit_default_billing_address_negative(self, driver):
        CreateAccountPage(driver)
        page = AddressAddPage(driver, MainPage.URL)
        with allure.step('Click “Welcome,…” dropdown menu'):
            page.is_clickable(bpl.WELCOME_MENU_BUTTON).click()
        with allure.step('Choose “My account” option'):
            page.is_clickable(bpl.WELCOME_MENU_MY_ACCOUNT_BUTTON).click()
        with allure.step('Click “Edit Address” button in “Default Billing Address” section of “Address Book” block'):
            page.is_clickable(mapl.EDIT_BILLING_ADDRESS_BUTTON).click()
        with allure.step('Type “ ” in upper “Street Address” field of “Address” block'):
            page.street_1 = ' '
        with allure.step('Type “ ” in “City” field of “Address” block'):
            page.city = ' '
        with allure.step('Type “ ” in “Zip/Postal Code” field of “Address” block'):
            page.postcode = ' '
        with allure.step('Type “ ” in “Phone Number” field of “Contact information” block'):
            page.telephone = ' '
        with allure.step('Click “Save Address” button'):
            page.save().click()
        with allure.step('“This is a required field.“  alert under “Street Address” field of “Address” block is displayed'):
            assert page.message_street_1_error() == AddressAddPage.REQUIRED_FIELD_ERROR
        with allure.step('“This is a required field.“  alert under “City” field of “Address” block is displayed'):
            assert page.message_city_error() == AddressAddPage.REQUIRED_FIELD_ERROR
        with allure.step('“Please select an option“  alert under “State/Province” dropdown menu of “Address” block is displayed'):
            assert page.message_state_error() == AddressAddPage.PLEASE_SELECT_ERROR
        with allure.step('“This is a required field.“  alert under “Zip/Postal Code” field of “Address” block is displayed'):
            assert page.message_postal_error() == AddressAddPage.REQUIRED_FIELD_ERROR
        with allure.step('“This is a required field.“  alert under “Phone Number” field of “Contact Information” block is displayed'):
            assert page.message_phone_error() == AddressAddPage.REQUIRED_FIELD_ERROR

    @allure.title("TC_004.015.016 | Authorization> User's account > My account > Default Shipping Address editing > Positive")
    @allure.tag("Authorization", "My account", "Default Shipping Address")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "valdemards")
    @allure.testcase(
        "https://trello.com/c/QBs5SaWC/331-tc004015016-authorization-users-account-my-account-default-shipping-address-editing-positive",
        "TC_004.015.016")
    def test_edit_default_shipping_address_positive(self, driver):
        CreateAccountPage(driver)
        page = AddressAddPage(driver, MainPage.URL)
        with allure.step('Click “Welcome,…” dropdown menu'):
            page.is_clickable(bpl.WELCOME_MENU_BUTTON).click()
        with allure.step('Choose “My account” option'):
            page.is_clickable(bpl.WELCOME_MENU_MY_ACCOUNT_BUTTON).click()
        with allure.step('Click “Edit Address” button in “Default Shipping Address” section of “Address Book” block'):
            page.is_clickable(mapl.EDIT_SHIPPING_ADDRESS_BUTTON).click()
        with allure.step('Type “street 7” in upper “Street Address” field of “Address” block'):
            page.street_1 = 'street 7'
        with allure.step('Type “city” in “City” field of “Address” block'):
            page.city = 'city'
        with allure.step('Choose “Alabama” in “State/Province” dropdown menu of “Address” block'):
            page.state = 'Alabama'
        with allure.step('Type “12345” in “Zip/Postal Code” field of “Address” block'):
            page.postcode = '12345'
        with allure.step('Type “123” in “Phone Number” field of “Contact information” block'):
            page.telephone = '123'
        with allure.step('Click “Save Address” button'):
            page.save().click()
        default_billing_address = page.is_visible(apl.DEFAULT_SHIPPING_ADDRESS_BLOCK).text.split('\n')
        with allure.step('New Street address, city, state,zip code, country and phone are visible in “Default Shipping Address” section'):
            assert default_billing_address[2] == 'street 7', 'Wrong data in Street 1 field'
            assert default_billing_address[3].split(',')[0] == 'city', 'Wrong data in City field'
            assert default_billing_address[3].split(', ')[1] == 'Alabama', 'Wrong data in State field'
            assert default_billing_address[3].split(', ')[2] == '12345', 'Wrong data in street Postal code field'
            assert default_billing_address[5].split(': ')[1] == '123', 'Wrong data in Phone field'

    @allure.title("TC_004.015.017 | Authorization> User's account > My account > Default Shipping Address editing > Negative")
    @allure.tag("Authorization", "My account", "Default Shipping Address")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "valdemards")
    @allure.testcase(
        "https://trello.com/c/itDxm4Zl/332-tc004015017-authorization-users-account-my-account-default-shipping-address-editing-negative",
        "TC_004.015.017")
    def test_edit_default_shipping_address_negative(self, driver):
        CreateAccountPage(driver)
        page = AddressAddPage(driver, MainPage.URL)
        with allure.step('Click “Welcome,…” dropdown menu'):
            page.is_clickable(bpl.WELCOME_MENU_BUTTON).click()
        with allure.step('Choose “My account” option'):
            page.is_clickable(bpl.WELCOME_MENU_MY_ACCOUNT_BUTTON).click()
        with allure.step('Click “Edit Address” button in “Default Shipping Address” section of “Address Book” block'):
            page.is_clickable(mapl.EDIT_SHIPPING_ADDRESS_BUTTON).click()
        with allure.step('Type “ ” in upper “Street Address” field of “Address” block'):
            page.street_1 = ' '
        with allure.step('Type “ ” in “City” field of “Address” block'):
            page.city = ' '
        with allure.step('Type “ ” in “Zip/Postal Code” field of “Address” block'):
            page.postcode = ' '
        with allure.step('Type “ ” in “Phone Number” field of “Contact information” block'):
            page.telephone = ' '
        with allure.step('Click “Save Address” button'):
            page.save().click()
        with allure.step('“This is a required field.“  alert under “Street Address” field of “Address” block is displayed'):
            assert page.message_street_1_error() == AddressAddPage.REQUIRED_FIELD_ERROR
        with allure.step('“This is a required field.“  alert under “City” field of “Address” block is displayed'):
            assert page.message_city_error() == AddressAddPage.REQUIRED_FIELD_ERROR
        with allure.step('“Please select an option“  alert under “State/Province” dropdown menu of “Address” block is displayed'):
            assert page.message_state_error() == AddressAddPage.PLEASE_SELECT_ERROR
        with allure.step('“This is a required field.“  alert under “Zip/Postal Code” field of “Address” block is displayed'):
            assert page.message_postal_error() == AddressAddPage.REQUIRED_FIELD_ERROR
        with allure.step('“This is a required field.“  alert under “Phone Number” field of “Contact Information” block is displayed'):
            assert page.message_phone_error() == AddressAddPage.REQUIRED_FIELD_ERROR
