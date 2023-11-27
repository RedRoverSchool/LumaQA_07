from selenium.webdriver.common.by import By


class MyAccountPageLocators:
    MY_ACCOUNT_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[1]")
    MY_ORDERS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[2]")
    MY_DOWNLOADABLE_PRODUCTS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[3]")
    MY_WISH_LIST_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[4]")
    ADDRESS_BOOK_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[6]")
    ACCOUNT_INFORMATION_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[7]")
    STORED_PAYMENT_METHODS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[8]")
    MY_PRODUCT_REVIEWS_BUTTON = (By.XPATH, "(//ul[@class='nav items']/li)[10]")
    CHANGE_PASSWORD_BUTTON = (By.XPATH, '//a[@class="action change-password"]')
    MANAGE_ADDRESSES_BUTTON = (By.XPATH, '//div[@class="block-title"]/a[@class="action edit"]')
    EDIT_BUTTON = (By.XPATH, '//div[@class="box box-information"]//a[@class="action edit"]')

    MY_ACCOUNT_TITLE = (By.XPATH,"//span[@data-ui-id='page-title-wrapper']")
    ACCOUNT_INFORMATION_BLOCK_TITLE = (By.XPATH,"//div[@class='block block-dashboard-info']/div[@class='block-title']")
    CONTACT_INFORMATION_BOX_TITLE = (By.XPATH,"//div[@class='block block-dashboard-info']//strong[@class='box-title']")
    ADDRESS_BOOK_BLOCK_TITLE = (By.XPATH,"//div[@class='block block-dashboard-addresses']//strong")
    DEFAULT_BILLING_ADDRESS_BOX_TITLE = (By.XPATH,"//div[@class='box box-billing-address']/strong[@class='box-title']")
    DEFAULT_SHIPPING_ADDRESS_BOX_TITLE = (By.XPATH,"//div[@class='box box-shipping-address']/strong[@class='box-title']")

