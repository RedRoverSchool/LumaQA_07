from selenium.webdriver.common.by import By


class CartPageLocators:
    MULTI_ADDRESS_CHECKOUT_LINK = (By.XPATH, "//a[@class = 'action multicheckout']")
    DELIVERY_CHOICE_BLOCK = (By.XPATH, "//*[@class='fieldset rate']")
    GRAND_TOTAL = (By.XPATH, "//tr[@class='grand totals']")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//button/span[text()='Proceed to Checkout']")
