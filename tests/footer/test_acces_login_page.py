from data.home_page_url import HOME_PAGE
from data.men_page_url import MEN_PAGE
from data.whats_new_page import WHATS_NEW_PAGE
from locators.base_page_locators import BasePageLocators
from pages.footer.footer_page import FooterPage
import pytest



@pytest.mark.parametrize('value',
                         [HOME_PAGE, MEN_PAGE,WHATS_NEW_PAGE])

def test_access(driver,value):

   page = FooterPage(driver,value)
   page.open()
   page.chech_visibility_footer_sign_in_link()
   assert 'Customer Login' in driver.page_source
