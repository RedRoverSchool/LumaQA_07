from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    EMAIL_FIELD = (By.XPATH, "//div[@class='field required']//*[@id='customer-email']")
    FIRST_NAME_FIELD = (By.XPATH, "//*[@name='firstname']")
    LAST_NAME_FIELD = (By.XPATH, "//*[@name='lastname']")
    STREET_1_FIELD = (By.XPATH, "//*[@name='street[0]']")
    CITY_FIELD = (By.XPATH, "//*[@name='city']")
    COUNTRY_FIELD_DROPDOWN = (By.XPATH, "//*[@name='country_id']")
    STATE_FIELD_DROPDOWN = (By.XPATH, "//*[@name='region_id']")
    POSTCODE_FIELD = (By.XPATH, "//*[@name='postcode']")
    PHONE_NUMBER_FIELD = (By.XPATH, "//*[@name='telephone']")

    SHIPPING_BEST_WAY = (By.XPATH, "//*[@id='label_carrier_bestway_tablerate']")
    SHIPPING_FLAT_RATE = (By.XPATH, "//*[@id='label_carrier_flatrate_flatrate']")

    ORDER_NUMBER_GUEST = (By.XPATH, "//div[@class='checkout-success']/p/span")
    ORDER_NUMBER_AS_USER = (By.XPATH, "//div[@class='checkout-success']//strong")
    EMAIL_ORDER = (By.XPATH, "//*[@data-bind='text: getEmailAddress()']")

    SUCCESS_PLACE_ORDER_MESSAGE = (By.XPATH, "//*[@data-ui-id='page-title-wrapper']")

    CHECKOUT_STEP_2_NEXT_BUTTON = (By.XPATH, "//*[@class='button action continue primary']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@title='Place Order']")
    ADDITIONAL_ADDRESS = (By.XPATH,"//div[@class='shipping-address-item not-selected-item']")
    CURRENT_DELIVERY_ADDRESS = (By.XPATH,"//div[@class='shipping-address-item selected-item']")
    STATE_OF_ADDITIONAL_ADDRESS = (By.XPATH, "//div[@class='shipping-address-item not-selected-item']/span")
    SHIP_HERE_BUTTON = (By.XPATH,"//*[text()='Ship Here']")

    OVERLAY = (By.XPATH, "//*[@data-role='loader']")

    EMAIL_FIELD_ERROR = (By.XPATH, "//div[@id='customer-email-error']")
    FIRST_NAME_FIELD_ERROR = (By.XPATH, "//*[@name='firstname']//following-sibling::div[@class='field-error']")
    LAST_NAME_FIELD_ERROR = (By.XPATH, "//*[@name='lastname']//following-sibling::div[@class='field-error']")
    STREET_1_FIELD_ERROR = (By.XPATH, "//*[@name='street[0]']//following-sibling::div[@class='field-error']")
    CITY_FIELD_ERROR = (By.XPATH, "//*[@name='city']//following-sibling::div[@class='field-error']")
    POSTCODE_FIELD_ERROR = (By.XPATH, "//*[@name='postcode']//following-sibling::div[@class='field-error']")
    POSTCODE_FIELD_ALERT = (By.XPATH, "//*[@name='postcode']//following-sibling::div[@class='field-error']//following-sibling::div[@class='message warning']")
    PHONE_NUMBER_FIELD_ERROR = (By.XPATH, "//*[@name='telephone']//following-sibling::div[@class='field-error']")
    SHIPPING_METHOD_ALERT = (By.XPATH, "//span[@data-bind='text: errorValidationMessage()']")


class MultipleAddressesPageLocators:
    ENTER_A_NEW_ADDRESS_BUTTON = (By.XPATH, "//button[@title='Enter a New Address']")
    UPDATE_QTY_AND_ADDRESS_BUTTON = (By.XPATH, "//button[@class='action update']")
    BACK_TO_CART_LINK = (By.XPATH, "//span[text()='Back to Shopping Cart']")
    GO_TO_SHIPPING_INFO_BUTTON = (By.XPATH, "//button[@class='action primary continue']")
    SELECT_SHIPPING_METHOD_BLOCK = (By.XPATH,"//*[@id='shipping_method_form']")

    TEXT_HEADER_USER_HAS_AN_ADDRESS = 'Ship to Multiple Addresses'
    TEXT_HEADER_USER_HAS_NO_ONE_ADDRESS = 'Create Shipping Address'
    TEXT_SUCCESSFUL_MSG_SAVE_NEW_ADDRESS = 'You saved the address.'
