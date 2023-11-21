from selenium.webdriver.common.by import By


class AddressBookLocators:
    FIRST_NAME_FIELD = (By.XPATH, "//*[@name='firstname']")
    LABEL_FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'label[for="firstname"]')
    MESSAGE_ERROR_FIRST_NAME_FIELD = (By.XPATH, "//*[@id='firstname-error']")

    LAST_NAME_FIELD = (By.XPATH, "//*[@name='lastname']")
    LABEL_LAST_NAME_FIELD = (By.CSS_SELECTOR, 'label[for="lastname"]')
    MESSAGE_ERROR_LAST_NAME_FIELD = (By.XPATH, "//*[@id='lastname-error']")

    PHONE_NUMBER_FIELD = (By.XPATH, "//*[@name='telephone']")
    LABEL_PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, 'label[for="telephone"]')
    MESSAGE_ERROR_PHONE_NUMBER_FIELD= (By.XPATH, "//*[@id='telephone-error']")

    STREET_1_FIELD = (By.XPATH, "//*[@id='street_1']")
    LABEL_STREET_FIELD = (By.CSS_SELECTOR, 'div.field.street.required>label[for="street_1"]')
    MESSAGE_ERROR_STREET_1_FIELD=(By.XPATH, "//*[@id='street_1-error']")

    CITY_FIELD = (By.XPATH, "//*[@name='city']")
    LABEL_CITY_FIELD = (By.CSS_SELECTOR, 'label[for="city"]')
    MESSAGE_ERROR_CITY_FIELD=(By.XPATH, "//*[@id='city-error']")

    COUNTRY_FIELD_DROPDOWN = (By.XPATH, "//*[@name='country_id']")
    LABEL_COUNTRY_FIELD = (By.CSS_SELECTOR, 'label[for="country"]')

    STATE_FIELD_DROPDOWN = (By.XPATH, "//*[@name='region_id']")
    LABEL_STATE_FIELD = (By.CSS_SELECTOR, 'label[for="region_id"]')
    MESSAGE_ERROR_STATE_FIELD_DROPDOWN=(By.XPATH, "//*[@id='region_id-error']")

    POSTCODE_FIELD = (By.XPATH, "//*[@name='postcode']")
    LABEL_POSTCODE_FIELD = (By.CSS_SELECTOR, 'label[for="zip"]')
    MESSAGE_ERROR_POSTCODE_FIELD=(By.XPATH, "//*[@id='zip-error']")

    SAVE_ADDRESS_BUTTON = (By.XPATH, "//button/span[text() = 'Save Address']")

    ADDITIONAL_ADDRESS_BLOCK = (By.XPATH, "//div[@class= 'block block-addresses-list']")
    DEFAULT_SHIPPING_ADDRESS_BLOCK = (By.XPATH,"//div[@class='box box-address-shipping']")
    OK_BUTTON_ON_POPUP_WINDOW = (By.XPATH,"//button[@class='action-primary action-accept']")
    ALL_ADDRESSES_BLOCK = (By.XPATH, "//div[@class='column main']")
    ADDITIONAL_ADDRESSES_BLOCK = (By.XPATH, "")

    USE_AS_DEFAULT_SHIPPING_CHECKBOX = (By.XPATH , "//input[@id='primary_shipping']")

    TEXT_SUCCESS_ADD_ADDRESS = "You saved the address."
    TEXT_ERROR_MSG_EMPTY_FIELD = "This is a required field."
    TEXT_ERROR_MSG_STATE = "Please select an option."
    TEXT_SUCCESS_DELETE_ADDRESS = "You deleted the address."

