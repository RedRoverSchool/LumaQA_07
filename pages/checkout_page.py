from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.seleniumbase import BasePage
from locators.checkout_page_locators import CheckoutPageLocators


class CheckoutPage(BasePage):
    URL = "https://magento.softwaretestingboard.com/checkout/"

    def email_field(self):
        return self.is_visible(CheckoutPageLocators.EMAIL_FIELD)

    def first_name_field(self):
        return self.is_visible(CheckoutPageLocators.FIRST_NAME_FIELD)

    def last_name_field(self):
        return self.is_visible(CheckoutPageLocators.LAST_NAME_FIELD)

    def street_address_1_field(self):
        return self.is_visible(CheckoutPageLocators.STREET_1_FIELD)

    def city_field(self):
        return self.is_visible(CheckoutPageLocators.CITY_FIELD)

    def postcode_field(self):
        return self.is_visible(CheckoutPageLocators.POSTCODE_FIELD)

    def country_dropdown_field(self):
        return self.is_visible(CheckoutPageLocators.COUNTRY_FIELD_DROPDOWN)

    def phone_number_field(self):
        return self.is_visible(CheckoutPageLocators.PHONE_NUMBER_FIELD)

    def select_state(self, state):
        self.is_visible(CheckoutPageLocators.STATE_FIELD_DROPDOWN)
        return self.is_clickable((By.XPATH, f"//*[@data-title='{state}']")).click()

    def select_flat_rate_shipping(self):
        return self.is_clickable(CheckoutPageLocators.SHIPPING_FLAT_RATE).click()

    def select_best_way_shipping(self):
        return self.is_clickable(CheckoutPageLocators.SHIPPING_BEST_WAY).click()

    def step_2_next_button(self):
        return self.is_clickable(CheckoutPageLocators.CHECKOUT_STEP_2_NEXT_BUTTON)

    def wait_overlay_closed(self):
        return self.is_invisible(CheckoutPageLocators.OVERLAY)

    def place_order_button(self):
        return self.is_clickable(CheckoutPageLocators.PLACE_ORDER_BUTTON)

    def place_order(self):
        self.place_order_button().click()
        self.wait_overlay_closed()

    def order_number_guest(self):
        return self.is_visible(CheckoutPageLocators.ORDER_NUMBER_GUEST)

    def fill_all_require_field_as_guest_us_shipping(self, state, email, firstname, lastname, street_1, city, postcode,
                                                    phone_number):
        self.select_state(state)
        self.email_field().send_keys(email)
        self.first_name_field().send_keys(firstname)
        self.last_name_field().send_keys(lastname)
        self.street_address_1_field().send_keys(street_1)
        self.city_field().send_keys(city)
        self.postcode_field().send_keys(postcode)
        self.phone_number_field().send_keys(phone_number)

    def fill_invalid_data_as_guest_us_shipping(self):
        self.email_field().send_keys('123')
        self.first_name_field().send_keys(' ')
        self.last_name_field().send_keys(' ')
        self.street_address_1_field().send_keys(' ')
        self.city_field().send_keys(' ')
        self.postcode_field().send_keys(' ')
        self.phone_number_field().send_keys(' ')
    def full_guest_place_order_us_address_flat_shipping(self, state, email, firstname, lastname, street_1, city,
                                                        postcode,
                                                        phone_number) -> str:
        self.fill_all_require_field_as_guest_us_shipping(state, email, firstname, lastname, street_1, city, postcode,
                                                         phone_number)
        self.select_flat_rate_shipping()
        self.step_2_next_button().click()
        self.wait_overlay_closed()
        self.place_order()
        order_id = self.order_number_guest().text
        return order_id

    def full_guest_place_order_us_address_best_way_shipping(self, state, email, firstname, lastname, street_1, city,
                                                            postcode,
                                                            phone_number) -> str:
        self.fill_all_require_field_as_guest_us_shipping(state, email, firstname, lastname, street_1, city, postcode,
                                                         phone_number)
        self.select_best_way_shipping()
        self.step_2_next_button().click()
        self.wait_overlay_closed()
        self.place_order()
        order_id = self.order_number_guest().text
        return order_id


class GuestShippingAddressPage(BasePage):
    WITH_REGIONS = ["AU", "BR", "CA", "CH", "CN", "CO", "EE", "ES",
                    "HR", "IN", "LT", "LV", "MX", "PL", "RO", "US",
                    "DE", "BE"]
    URL = "https://magento.softwaretestingboard.com/checkout/#shipping"
    URL_DONE = "https://magento.softwaretestingboard.com/checkout/#payment"

    EMAIL = (By.CSS_SELECTOR, "input#customer-email")

    FIRST_NAME = (By.CSS_SELECTOR, 'input[name="firstname"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[name="lastname"]')
    COMPANY = (By.CSS_SELECTOR, 'input[name="company"]')
    STREET_1 = (By.CSS_SELECTOR, 'input[name="street[0]"]')
    STREET_2 = (By.CSS_SELECTOR, 'input[name="street[1]"]')
    STREET_3 = (By.CSS_SELECTOR, 'input[name="street[2]"]')
    CITY = (By.CSS_SELECTOR, 'input[name="city"]')
    # select STATE is for WITH_REGIONS country's else input REGION (share same place)
    STATE = (By.CSS_SELECTOR, 'select[name="region_id"]')
    REGION = (By.CSS_SELECTOR, 'input[name="region"]')
    ZIP = (By.CSS_SELECTOR, 'input[name="postcode"]')
    COUNTRY = (By.CSS_SELECTOR, 'select[name="country_id"]')
    PHONE = (By.CSS_SELECTOR, 'input[name="telephone"]')

    BUTTON_NEXT = (By.CSS_SELECTOR, "button.continue")

    LD_PAYMENT_METHOD = (By.CSS_SELECTOR, "li.checkout-payment-method")

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url

    @property
    def email(self):
        return self.is_visible(self.EMAIL)

    @email.setter
    def email(self, val: str):
        self.clear_and_send_keys(self.email, val)

    @property
    def first_name(self):
        return self.is_visible(self.FIRST_NAME)

    @first_name.setter
    def first_name(self, val: str):
        self.clear_and_send_keys(self.first_name, val)

    @property
    def last_name(self):
        return self.is_visible(self.LAST_NAME)

    @last_name.setter
    def last_name(self, val: str):
        self.clear_and_send_keys(self.last_name, val)

    @property
    def company(self):
        return self.is_visible(self.COMPANY)

    @company.setter
    def company(self, val: str):
        self.clear_and_send_keys(self.company, val)

    @property
    def telephone(self):
        return self.is_visible(self.PHONE)

    @telephone.setter
    def telephone(self, val: str):
        self.clear_and_send_keys(self.telephone, val)

    @property
    def street_1(self):
        return self.is_visible(self.STREET_1)

    @street_1.setter
    def street_1(self, val: str):
        self.clear_and_send_keys(self.street_1, val)

    @property
    def street_2(self):
        return self.is_visible(self.STREET_2)

    @street_2.setter
    def street_2(self, val: str):
        self.clear_and_send_keys(self.street_2, val)

    @property
    def street_3(self):
        return self.is_visible(self.STREET_3)

    @street_3.setter
    def street_3(self, val: str):
        self.clear_and_send_keys(self.street_3, val)

    @property
    def city(self):
        return self.is_visible(self.CITY)

    @city.setter
    def city(self, val: str):
        self.clear_and_send_keys(self.city, val)

    @property
    def region(self):
        return self.is_visible(self.REGION)

    @region.setter
    def region(self, val):
        self.clear_and_send_keys(self.region, val)

    @property
    def postcode(self):
        return self.is_visible(self.ZIP)

    @postcode.setter
    def postcode(self, val: str):
        self.clear_and_send_keys(self.postcode, val)

    @property
    def state(self):
        return [x.text for x in Select(self.is_clickable(self.STATE)).options]

    @state.setter
    def state(self, text):
        Select(self.is_clickable(self.STATE)).select_by_visible_text(text)

    @property
    def country(self):
        return [x.get_attribute('value') for x in Select(self.is_clickable(self.COUNTRY)).options]

    @country.setter
    def country(self, val):
        Select(self.is_clickable(self.COUNTRY)).select_by_value(val)

    def button_next(self):
        self.is_invisible(self.LD_PAYMENT_METHOD)
        return self.is_clickable(self.BUTTON_NEXT)
