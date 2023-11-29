from selenium.webdriver.common.by import By


class CartPageLocators:
    MULTI_ADDRESS_CHECKOUT_LINK = (By.XPATH, "//a[@class = 'action multicheckout']")
    DELIVERY_CHOICE_BLOCK = (By.XPATH, "//*[@class='fieldset rate']")
    GRAND_TOTAL = (By.XPATH, "//tr[@class='grand totals']")
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//button/span[text()='Proceed to Checkout']")
    URL_CART_PAGE = 'https://magento.softwaretestingboard.com/checkout/cart/'
    BUTTON_EDIT_ITEM = (By.XPATH, '//*[@title="Deirdre Relaxed-Fit Capri"]/../../..//*[@title="Edit item parameters"]')
    COLOR_BLUE = (By.XPATH, '//*[@id="option-label-color-93-item-50"]')
    BUTTON_UPDATE_CART = (By.XPATH, '//*[@id="product-updatecart-button"]')
    ITEM_OPTIONS = (By.XPATH, '//*[@title="Deirdre Relaxed-Fit Capri"]/..//*[@class="item-options"]')
    SIZE_UPDATE_29 = (By.XPATH, '//*[@id="option-label-size-143-item-172"]')

    URL_ITEM_DEIRDRE_RELAXED = 'https://magento.softwaretestingboard.com/deirdre-relaxed-fit-capri.html'
    BUTTON_ADD_TO_CART = (By.XPATH, '//*[@id="product-addtocart-button"]')
    COLOR_GREY = (By.XPATH, '//*[@id="option-label-color-93-item-52"]')
    SIZE_28 = (By.XPATH, '//*[@id="option-label-size-143-item-171"]')







