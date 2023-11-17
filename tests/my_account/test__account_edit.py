from random import choice

from base.seleniumbase import BasePage
from data.fake_data import FakeData
from pages.account.account_add_address import AddressAddPage
from pages.account.account_edit import AccountEditPage
from pages.account.create_account import CreateAccountPage
from pages.account.my_account import MyAccountPage
from pages.account.sign_in import SignInPage
from pages.login.logout_page import LogoutPage


class TestX(FakeData):
    def test_change_first_name(self, driver, create_account):
        page = AccountEditPage(driver)
        page.first_name = self.first_name
        page.save().click()
        assert page.current_url == MyAccountPage.URL, "Unexpected page URL"
        assert page.message_success == AccountEditPage.SUCCESS, "Message not as expected"

    def test_change_last_name(self, driver, create_account):
        page = AccountEditPage(driver)
        page.last_name = self.last_name
        page.save().click()
        assert page.current_url == MyAccountPage.URL, "Unexpected page URL"
        assert page.message_success == AccountEditPage.SUCCESS, "Message not as expected"

    def test_change_password(self, driver):
        password_current = CreateAccountPage(driver).password
        page = AccountEditPage(driver)
        page.change_password().click()
        page.password_current = password_current
        page.password = (password_new := self.password)
        page.password_confirm = password_new
        page.save().click()
        assert page.current_url == SignInPage.URL, "Unexpected page URL"
        assert page.message_success == AccountEditPage.SUCCESS, "Message not as expected"

    def test_change_email(self, driver):
        password_current = CreateAccountPage(driver).password
        page = AccountEditPage(driver)
        page.change_email().click()
        page.email = self.email
        page.password_current = password_current
        page.save().click()
        count = BasePage.ATTEMPTS
        while page.message == AccountEditPage.ERROR_EMAIL_IN_USE and count:
            page.change_email().click()
            page.email = self.email
            page.password_current = password_current
            page.save().click()
            count -= 1
        assert page.message == AccountEditPage.SUCCESS, (f"Не удалось изменить email"
                                                         f" за {BasePage.ATTEMPTS} попыток!")
        assert page.current_url == SignInPage.URL, "Unexpected page URL"

    def test_change_email_to_already_used_email(self, driver):
        email_in_use = CreateAccountPage(driver).email
        LogoutPage(driver)
        password_current = CreateAccountPage(driver).password
        page = AccountEditPage(driver)
        page.change_email().click()
        page.email = email_in_use
        page.password_current = password_current
        page.save().click()
        assert page.current_url == AccountEditPage.URL, "Unexpected page URL"
        assert page.message_error == AccountEditPage.ERROR_EMAIL_IN_USE, "Message not as expected"

    def test_change_email_and_password(self, driver):
        password_current = CreateAccountPage(driver).password
        page = AccountEditPage(driver)
        page.change_email().click()
        page.change_password().click()
        page.email = self.email
        page.password_current = password_current
        page.password = (password_new := self.password)
        page.password_confirm = password_new
        page.save().click()
        count = BasePage.ATTEMPTS
        while page.message == AccountEditPage.ERROR_EMAIL_IN_USE and count:
            page.change_email().click()
            page.email = self.email
            page.password_current = password_current
            page.password = (password_new := self.password)
            page.password_confirm = password_new
            page.save().click()
            count -= 1
        assert page.message == AccountEditPage.SUCCESS, (f"Не удалось изменить email и пароль"
                                                         f" за {BasePage.ATTEMPTS} попыток!")
        assert page.current_url == SignInPage.URL, "Unexpected page URL"

    def test_change_email_and_password_to_already_used_email(self, driver):
        email_in_use = CreateAccountPage(driver).email
        LogoutPage(driver)
        password_current = CreateAccountPage(driver).password
        page = AccountEditPage(driver)
        page.change_email().click()
        page.change_password().click()
        page.email = email_in_use
        page.password_current = password_current
        page.password = (password_new := self.password)
        page.password_confirm = password_new
        page.save().click()
        assert page.message == AccountEditPage.ERROR_EMAIL_IN_USE, "Message not as expected"
        assert page.current_url == AccountEditPage.URL, "Unexpected page URL"

    def test_add_address_with_select_state(self, driver):
        CreateAccountPage(driver)

        page = AddressAddPage(driver)
        page.company = self.company
        page.telephone = self.phone_number

        page.country = choice(AddressAddPage.WITH_REGIONS)
        page.state = (state := choice(page.state[1:]))
        page.city = (city := self.city)
        page.postcode = (postcode := self.postcode)
        page.street_1 = self.secondary_address
        page.street_2 = self.street_address
        page.street_3 = f"{city} {state} {postcode}"

        # page.set_billing.click()
        page.save().click()

        assert page.current_url == AddressAddPage.URL_DONE
        assert page.message_success == AddressAddPage.SUCCESS

    def test_add_address_with_input_state(self, driver):
        CreateAccountPage(driver)

        page = AddressAddPage(driver)
        page.company = self.company
        page.telephone = self.phone_number

        page.country = choice(list(filter(lambda x: x not in AddressAddPage.WITH_REGIONS, page.country)))

        city = self.city
        state = self.state
        postcode = self.postcode
        page.street_1 = self.secondary_address
        page.street_2 = self.street_address
        page.street_3 = f"{city} {state} {postcode}"
        page.city = city
        page.postcode = postcode
        page.region = state

        # page.set_shpping.click()

        page.save().click()

        assert page.current_url == AddressAddPage.URL_DONE
        assert page.message_success == AddressAddPage.SUCCESS

    def test_change_password_negative(self, driver, create_account, password):
        page = AccountEditPage(driver)
        page.change_password().click()
        page.password_current = password
        page.save().click()

        assert page.message_change_password_error() == AccountEditPage.CHANGE_PASSWORD_ERROR
        assert page.message_confirm_change_password_error() == AccountEditPage.CHANGE_PASSWORD_ERROR
