from locators.login_page_locators import LoginPageLocators
from pages.login.login_page import LoginPage
import time

import pytest



@pytest.mark.parametrize('creds',
                             [('tyyttyt@gmail.com', '1234asd!'), ('testTestpro@gmail.com', 'Zaqxsw100')])

def test_authorization_valid_credentials(driver,creds):
   login,password=creds
   page = LoginPage(driver, LoginPageLocators.URL)
   page.open()
   page.set_email(login)
   page.set_password(password)
   page.click_sign_in_button()
   page.get_text_message()
   actual_title=page.get_text_message()
   assert actual_title=="My Account"
@pytest.mark.parametrize('creds',
                             [('user2@gamail.com', 'pass2'),('user3@yandex.ru',' ')])
def test_authorization_not_valid_credentials(driver, creds):
      login, password = creds
      page = LoginPage(driver, LoginPageLocators.URL)
      page.open()
      page.set_email(login)
      page.set_password(password)
      page.click_sign_in_button()
      assert "The account sign-in was incorrect or your account is disabled temporarily."
      "Please wait and try again later."  in driver.page_source

