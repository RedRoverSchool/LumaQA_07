from selenium.webdriver.common.by import By


class LoginPageLocators:
    URL = 'https://magento.softwaretestingboard.com/customer/account/login/'
    EMAIL = (By.CSS_SELECTOR, 'input#email')
    PASSWORD = (By.CSS_SELECTOR, 'input#pass')
    BUTTON_SIGN_IN = (By.CSS_SELECTOR, 'button.login')
    BUTTON_FORGOT_PASSWORD = (By.CSS_SELECTOR, 'a.remind')
    CREATE_AN_ACCOUNT_BUTTON = (By.XPATH, "//*[@class='action create primary']")
    TEXT_ERROR_MSG_LOGIN = 'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.'


class ResetPageLocators:
    URL = 'https://magento.softwaretestingboard.com/customer/account/login'
    FORGOT_PASS_URL = 'https://magento.softwaretestingboard.com/customer/account/forgotpassword/'
    LONG_EMAIL = 'longgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg@ya.ru'
    EMAIL = (By.CSS_SELECTOR, 'input#email_address')
    BUTTON_RESET_PASSWORD = (By.CSS_SELECTOR, 'button.submit')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "[data-ui-id=message-success] div")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#email_address-error")
    ERROR_ALERT = (By.CSS_SELECTOR, '[data-ui-id="message-error"]')

class ForgotPasswordPageLocators:
    URL = 'https://magento.softwaretestingboard.com/customer/account/forgotpassword/'
    TEXT = 'Forgot Your Password?'
    TEXT_WRONG_EMAIL= 'Please enter a valid email address (Ex: johndoe@domain.com).'
    FORGOT_PASSWORD_TEXT = (By.CSS_SELECTOR, 'span[data-ui-id="page-title-wrapper"]')
    EMAIL = (By.CSS_SELECTOR, 'input#email_address')
    BUTTON_RESET_MY_PASSWORD = (By.CSS_SELECTOR, 'button.action.submit')
    EMAIL_ERROR_MESS = (By.CSS_SELECTOR, 'div#email_address-error')