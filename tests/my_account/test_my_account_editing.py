from pages.main_page import MainPage
from pages.account.create_account import CreateAccountPage
from pages.account.account_edit import AccountEditPage
from pages.account.sign_in import SignInPage
from data.fake_data import FakeData
from locators.base_page_locators import BasePageLocators as bpl
from locators.my_account_page_locators import MyAccountPageLocators as mapl
import allure


class TestMyAccountDataEditing(FakeData):
    @allure.title("TC_004.015.007 | Authorization> User's account > My account > Changing password > Positive")
    # @allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
    @allure.tag("Authorization", "My account", "Changing password")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.label("owner", "valdemards")
    # @allure.link("https://dev.example.com/", name="Website")
    # @allure.issue("AUTH-123")
    @allure.testcase("https://trello.com/c/UbzNXcU5/319-tc004015007-authorization-users-account-my-account-changing-password-positive", "TC_004.015.007")
    def test_change_password_positive(self, driver):
        password_current = CreateAccountPage(driver).password
        page = AccountEditPage(driver, MainPage.URL)
        png_bytes = driver.get_screenshot_as_png()
        allure.attach(png_bytes, name='test', attachment_type=allure.attachment_type.PNG)
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
