import time

from pages.account.create_account import CreateAccountPage
from pages.account.sign_in import SignInPage
from pages.login.logout_page import LogoutPage
from locators.my_account_page_locators import MyAccountPageLocators as mapl


"""TC_004.015.001 | Authorization> User's account > My account > Title visibility
    Pre-conditions:
        User is logged in
        Home Page is opened

    Steps:
        Click “Welcome,…” dropdown menu
        Choose “My account” option

    Expected results:
        Title “My account” is visible"""

"""TC_004.015.002 | Authorization> User's account > My account > Block title visibility
    Pre-conditions:
        User is logged in
        Home Page  is opened
    
    Steps:
        Click “Welcome,…” dropdown menu
        Choose “My account” option
    
    Expected results:
        Block title “Account information” is visible"""

"""TC_004.015.004 | Authorization> User's account > My account > Contact information visibility
    Pre-conditions:
        User is logged in
        Home Page page is opened
    
    Steps:
        Click “Welcome,…” dropdown menu
        Choose “My account” option
        
    Expected results:
        Block title “Contact information” is visible
        First name, last name and email address are visible"""

"""TC_004.015.009 | Authorization> User's account > My account > Address book visibility
    Pre-conditions:
        User is logged in
        Home Page page is opened
    
    Steps:
        Click “Welcome,…” dropdown menu
        Choose “My account” option
    
    Expected results:
        Block title “Address Book” is visible
"""

"""TC_004.015.012 | Authorization> User's account > My account > Default Billing Address visibility
    Pre-conditions:
        User is logged in
        Home Page page is opened
    
    Steps:
        Click “Welcome,…” dropdown menu
        Choose “My account” option
        
    Expected results:
        Section title “Default Billing Address” is visible
        Street address, city, state,zip code, country and phone fields are visible in “Default Billing Address” section and they are not empty"""

"""TC_004.015.015 | Authorization> User's account > My account > Default Shipping Address visibility
    Pre-conditions:
        User is logged in
        Home Page page is opened
    
    Steps:
        Click “Welcome,…” dropdown menu
        Choose “My account” option
    
    Expected results:
        Section title “Default Shipping Address” is visible
        Street address, city, state,zip code, country and phone fields are visible in “Default Shipping Address” section and they are not empty"""


class TestMyAccountTitleVisibility:
    def test_my_account_visibility(self, driver):
        page = CreateAccountPage(driver)
        password_current = page.password
        email_current = page.email
        LogoutPage(driver)
        page = SignInPage(driver)
        page.email = email_current
        page.password_one = password_current
        page.sign_in().click()

        """TC_004.015.001 | Authorization> User's account > My account > Title visibility"""
        assert page.is_visible(mapl.MY_ACCOUNT_TITLE).text == 'My Account'

        """TC_004.015.002 | Authorization> User's account > My account > Block title visibility"""
        assert page.is_visible(mapl.ACCOUNT_INFORMATION_BLOCK_TITLE).text == 'Account Information'

        """TC_004.015.004 | Authorization> User's account > My account > Contact information visibility"""
        assert page.is_visible(mapl.CONTACT_INFORMATION_BOX_TITLE).text == 'Contact Information'

        """TC_004.015.009 | Authorization> User's account > My account > Address book visibility"""
        assert page.is_visible(mapl.ADDRESS_BOOK_BLOCK_TITLE).text == 'Address Book'

        """TC_004.015.012 | Authorization> User's account > My account > Default Billing Address visibility"""
        assert page.is_visible(mapl.DEFAULT_BILLING_ADDRESS_BOX_TITLE).text == 'Default Billing Address'

        """TC_004.015.015 | Authorization> User's account > My account > Default Shipping Address visibility"""
        assert page.is_visible(mapl.DEFAULT_SHIPPING_ADDRESS_BOX_TITLE).text == 'Default Shipping Address'


