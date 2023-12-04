from selenium.webdriver.common.by import By


class OrdersAndReturnsPageLocators:
    ORDER_ID_FIELD = (By.XPATH, "//*[@id='oar-order-id']")
    ORDER_ID_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar-order-id-error']")

    BILLING_LASTNAME_FIELD = (By.XPATH, "//*[@id='oar-billing-lastname']")
    BILLING_LASTNAME_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar-billing-lastname-error']")

    FIND_ORDER_BY_DROPDOWN = (By.XPATH, "//*[@id='quick-search-type-id']")
    FIND_ORDER_BY_EMAIL_DROPDOWN = (By.XPATH, "//option[@value='email']")
    FIND_ORDER_BY_POSTCODE_DROPDOWN = (By.XPATH, "//option[@value='zip']")

    ORDER_STATUS = (By.XPATH, "//span[@class='order-status']")

    EMAIL_FIELD = (By.XPATH, "//*[@id='oar_email']")
    EMAIL_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar_email-error']")
    EMAIL_FIELD_NAME = (By.XPATH, "//label[@for='oar_email']")

    POSTCODE_FIELD = (By.XPATH, "//*[@id='oar_zip']")
    POSTCODE_FIELD_MESSAGE_ERROR = (By.XPATH, "//*[@id='oar_zip-error']")
    POSTCODE_FIELD_NAME = (By.XPATH, "//label[@for='oar_zip']")

    INCORRECT_DATA_MESSAGE = (By.XPATH, "//*[@data-ui-id='message-error']")
    CONTINUE_BUTTON = (By.XPATH, "//*[@title='Continue']")

    ORDER_NUMBER_ON_VIEW_ORDER_PAGE = (By.XPATH, "//span[@class='base']")

    TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD = "This is a required field."
    TEXT_ERROR_MESSAGE_EMAIL_TYPE = "Please enter a valid email address (Ex: johndoe@domain.com)."
    TEXT_ERROR_MESSAGE_INCORRECT_DATA = "You entered incorrect data. Please try again."
    TEXT_NAME_POSTCODE_FIELD = "Billing ZIP Code"
    TEXT_NAME_EMAIL_FIELD = "Email"
