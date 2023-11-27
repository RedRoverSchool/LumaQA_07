from pages.main_page import MainPage
from pages.account.create_account import CreateAccountPage
from pages.account.account_edit import AccountEditPage
from pages.account.sign_in import SignInPage
from data.fake_data import FakeData
from locators.base_page_locators import BasePageLocators as bpl
from locators.my_account_page_locators import MyAccountPageLocators as mapl

class TestMyAccountDataEditing(FakeData):
    """TC_004.015.007 | Authorization> User's account > My account > Changing password > Positive"""
    """Pre-conditions:
        User is logged in
        Home Page page is opened

    Steps:
        Click “Welcome,…” dropdown menu
        Choose “My account” option
        Click “Change Password” button
        Type current account password in “Current Password” field of “Change Password” block
        Type new password in “New Password” field of “Change Password” block
        Type the same new password in “Confirm New Password” field of “Change Password” block
        Click “Save” button

    Expected results:
        “You saved the account information” alert is visible"""
    def test_change_password_positive(self, driver):
        password_current = CreateAccountPage(driver).password
        page = AccountEditPage(driver, MainPage.URL)
        page.is_clickable(bpl.WELCOME_MENU_BUTTON).click()
        page.is_clickable(bpl.WELCOME_MENU_MY_ACCOUNT_BUTTON).click()
        page.is_clickable(mapl.CHANGE_PASSWORD_BUTTON).click()
        page.password_current = password_current
        page.password = (password_new := self.password)
        page.password_confirm = password_new
        page.save().click()
        assert page.current_url == SignInPage.URL, "Unexpected page URL"
        assert page.message_success == AccountEditPage.SUCCESS, "Message not as expected"


    """TC_004.015.008 | Authorization> User's account > My account > Changing password > Negative"""
    """Pre-conditions:
        User is logged in
        Home Page page is opened
    
    Steps:
        Click “Welcome,…” dropdown menu
        Choose “My account” option
        Click “Change Password” button
        Type “ “ in “Current Password” field of “Change Password” block
        Type “ “ in “New Password” field of “Change Password” block
        Type” “ in “Confirm New Password” field of “Change Password” block
        Click “Save” button
    
    Expected results:
        “This is a required field.“ alert under “Current Password” field of “Change Password” block is displayed
        “This is a required field.“ alert under “New Password” field of “Change Password” block is displayed
        “This is a required field.“ alert under “Confirm New Password” field of “Change Password” block is displayed"""
    def test_change_password_negative(self, driver):
        password_current = CreateAccountPage(driver).password
        page = AccountEditPage(driver, MainPage.URL)
        page.is_clickable(bpl.WELCOME_MENU_BUTTON).click()
        page.is_clickable(bpl.WELCOME_MENU_MY_ACCOUNT_BUTTON).click()
        page.is_clickable(mapl.CHANGE_PASSWORD_BUTTON).click()
        page.password_current = ' '
        page.password = (password_new := ' ')
        page.password_confirm = password_new
        page.save().click()
        assert page.message_current_password_error() == AccountEditPage.CHANGE_PASSWORD_ERROR
        assert page.message_change_password_error() == AccountEditPage.CHANGE_PASSWORD_ERROR
        assert page.message_confirm_change_password_error() == AccountEditPage.CHANGE_PASSWORD_ERROR
