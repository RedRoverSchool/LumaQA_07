from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base.seleniumbase import BasePage


class AddressAddPage(BasePage):
    WITH_REGIONS = ["AU", "BR", "CA", "CH", "CN", "CO", "EE", "ES",
                    "HR", "IN", "LT", "LV", "MX", "PL", "RO", "US",
                    "DE", "BE"]
    URL = "https://magento.softwaretestingboard.com/customer/address/new/"
    URL_DONE = "https://magento.softwaretestingboard.com/customer/address/index/"

    FIRST_NAME = (By.CSS_SELECTOR, "input#firstname")
    LAST_NAME = (By.CSS_SELECTOR, "input#lastname")

    COMPANY = (By.CSS_SELECTOR, "input#company")
    PHONE = (By.CSS_SELECTOR, "input#telephone")

    STREET_1 = (By.CSS_SELECTOR, "input#street_1")
    STREET_2 = (By.CSS_SELECTOR, "input#street_2")
    STREET_3 = (By.CSS_SELECTOR, "input#street_3")

    CITY = (By.CSS_SELECTOR, "input#city")
    # select STATE is for WITH_REGIONS country's else input REGION (share same place)
    STATE = (By.CSS_SELECTOR, "select#region_id")
    REGION = (By.CSS_SELECTOR, "input#region")
    ZIP = (By.CSS_SELECTOR, "input#zip")
    COUNTRY = (By.CSS_SELECTOR, "select#country")

    SET_BILLING = (By.CSS_SELECTOR, "input#primary_billing")
    SET_SHIPPING = (By.CSS_SELECTOR, "input#primary_shipping")

    SAVE = (By.CSS_SELECTOR, "button.save")

    SUCCESS = "You saved the address."
    REQUIRED_FIELD_ERROR = 'This is a required field.'
    PLEASE_SELECT_ERROR = 'Please select an option.'
    MESSAGE_STREET_1_ERROR = (By.XPATH, '//div[@for="street_1"]')
    MESSAGE_CITY_ERROR = (By.XPATH, '//div[@for="city"]')
    MESSAGE_STATE_ERROR = (By.XPATH, '//div[@for="region_id"]')
    MESSAGE_POSTAL_ERROR = (By.XPATH, '//div[@for="zip"]')
    MESSAGE_PHONE_ERROR = (By.XPATH, '//div[@for="telephone"]')

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)
        self.current_url = url

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

    @property
    def set_billing(self):
        return self.is_clickable(self.SET_BILLING)

    @property
    def set_shipping(self):
        return self.is_clickable(self.SET_SHIPPING)

    def save(self):
        return self.is_clickable(self.SAVE)

    def message_street_1_error(self):
        message_street_1_error = self.is_visible(self.MESSAGE_STREET_1_ERROR).text
        return message_street_1_error

    def message_city_error(self):
        message_city_error = self.is_visible(self.MESSAGE_CITY_ERROR).text
        return message_city_error

    def message_state_error(self):
        message_state_error = self.is_visible(self.MESSAGE_STATE_ERROR).text
        return message_state_error

    def message_postal_error(self):
        message_postal_error = self.is_visible(self.MESSAGE_POSTAL_ERROR).text
        return message_postal_error

    def message_phone_error(self):
        message_phone_error = self.is_visible(self.MESSAGE_PHONE_ERROR).text
        return message_phone_error

