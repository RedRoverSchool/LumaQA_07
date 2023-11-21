from data.fake_data import FakeData
from locators.base_page_locators import BasePageLocators
from locators.orders_and_returns_locators import OrdersAndReturnsPageLocators
from pages.checkout_page import CheckoutPage
from pages.footer.orders_and_returns import OrdersAndReturnsPage


class TestIncorrectEmailFill(FakeData):

    def test_email_without_dot(self, driver):
        """TC_012.009.001 | Footer > 'Orders and Returns' > Email incorrect format\n
        Pre-conditions:
            User not logged into the account and is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
        Steps:
            User enters email in incorrect format in the 'Email' field and clicks the 'Continue' button
        Expected results:
            Under the 'Email' field, an error message appears:
            'Please enter a valid email address (Ex: johndoe@domain.com).' """
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(self.fake_order_id, self.last_name, 'dadqweq3@mailcom')
        page.go_to_continue_button().click()
        assert page.is_invisible(BasePageLocators.MSG_ERROR)
        assert page.error_msg_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_EMAIL_TYPE, "Не появилась ошибка про неправильный формат email"

    def test_email_without_at(self, driver):
        """TC_012.009.001 | Footer > 'Orders and Returns' > Email incorrect format\n
        Pre-conditions:
            User not logged into the account and is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
        Steps:
            User enters email in incorrect format in the 'Email' field and clicks the 'Continue' button
        Expected results:
            Under the 'Email' field, an error message appears:
            'Please enter a valid email address (Ex: johndoe@domain.com).' """
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(self.fake_order_id,self.last_name, 'dadqweq3amail.com')
        page.go_to_continue_button().click()
        assert page.is_invisible(BasePageLocators.MSG_ERROR)
        assert page.error_msg_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_EMAIL_TYPE, "Не появилась ошибка про неправильный формат email"


class TestFieldsNotFilled(FakeData):
    def test_order_id_field_not_filled(self, driver):
        """TC_012.009.002 | Footer > “Orders and Returns” > Order_ID field\n
        Pre-conditions:
            User not logged into the account and is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
        Steps:
            The user filled in all fields except 'Order_id' and clicks the "Continue" button
        Expected results:
            Error message 'This is a required field.' appeared under the "Order ID" field."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(self.fake_order_id, self.last_name, self.email, )
        page.order_id_field().clear()
        page.continue_button().click()
        assert page.is_invisible(BasePageLocators.MSG_ERROR)
        assert page.error_msg_order_id_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле order_id не заполнено , а ошибка не показана"

    def test_billing_lastname_field_not_filled(self, driver):
        """TC_012.009.003 | Footer > “Orders and Returns” > Billing_Last_Name_field\n
        Pre-conditions:
            User not logged into the account and is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
        Steps:
            The user filled in all fields except "Billing Last Name" and clicks the "Continue" button
        Expected results:
            Error message 'This is a required field.' appeared under the "Billing Last Name" field."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(self.fake_order_id, self.last_name, self.email)
        page.billing_lastname_field().clear()
        page.continue_button().click()
        assert page.is_invisible(BasePageLocators.MSG_ERROR)
        assert page.error_msg_billing_lastname_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле billing lastname не заполнено , а ошибка не показана"

    def test_email_field_not_filled(self, driver):
        """TC_012.009.004 | Footer > “Orders and Returns” > Email_field\n
        Pre-conditions:
            User not logged into the account and is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
        Steps:
            The user filled in all fields except 'Email' and clicks the "Continue" button
        Expected results:
            Error message 'This is a required field.' appeared under the "Email" field."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(self.fake_order_id, self.last_name , self.email)
        page.email_field().clear()
        page.continue_button().click()
        assert page.is_invisible(BasePageLocators.MSG_ERROR)
        assert page.error_msg_email_not_filled_or_incorrect_type().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле email не заполнено , а ошибка не показана"

    def test_zip_field_not_filled(self, driver):
        """TC_012.009.005 | Footer > “Orders and Returns” > ZIP code field\n
        Pre-conditions:
            User not logged into the account and is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
        Steps:
            1)The user selects "ZIP Code" in the "Find Order By" field\n
            2)The user filled in all fields except "Billing ZIP Code" and clicks the "Continue" button
        Expected results:
            Error message 'This is a required field.' appeared under the "Billing ZIP Code" field."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_postcode(self.fake_order_id, self.last_name,self.postcode)
        page.billing_postcode_field().clear()
        page.continue_button().click()
        assert page.is_invisible(BasePageLocators.MSG_ERROR)
        assert page.error_msg_billing_postcode_not_filled().text == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_FIELD_NOT_FIELD, "Поле zipcode не заполнено , а ошибка не показана"


class TestCheckNonExistentOrder(FakeData):

    def test_by_email(self, driver):
        """TC_012.009.006 | Footer > “Orders and Returns” > Search for a non-existent order\n
        Pre-conditions:
            User not logged into the account and is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
        Steps:
            The user fills in all fields with data for a non-existent order and clicks the "Continue" button
        Expected results:
            Error message -  'You entered incorrect data. Please try again.'
            appeared below the "Orders and Returns" heading."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_email(self.fake_order_id,self.last_name,self.email)
        page.continue_button().click()
        assert page.message_error == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_INCORRECT_DATA, "Не появилась ошибка о том что введены неправильные данные заказа"

    def test_by_postcode(self, driver):
        """TC_012.009.008 | Footer > “Orders and Returns” > Search for a non-existent order\n
        Pre-conditions:
            User not logged into the account and is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
        Steps:
            1)The user selects "ZIP Code" in the "Find Order By" field\n
            2)The user fills in all fields with data for a non-existent order and clicks the "Continue" button\n
        Expected results:
            Error message -  'You entered incorrect data. Please try again.'
            appeared below the "Orders and Returns" heading."""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.fill_all_field_with_postcode(self.fake_order_id,self.last_name,self.postcode)
        page.continue_button().click()
        assert page.message_error == OrdersAndReturnsPageLocators.TEXT_ERROR_MESSAGE_INCORRECT_DATA, "Не появилась ошибка о том что введены неправильные данные заказа"


class TestCheckExistingOrder(FakeData):

    def test_by_email(self, driver , add_3_item_to_cart):
        """TC_012.009.007 | Footer > “Orders and Returns” > Search for an existing order By Email or ZIP Code\n
        Pre-conditions:
            The user must place an order on the website.
            User not logged into the account and is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
        Steps:
            The user enters the correct data for the existing order in all required fields
            and clicks the “Continue” button.
        Expected results:
            There was a redirect to a page with information about the required order
            (url = https://magento.softwaretestingboard.com/sales/guest/view/ ) The header says "Order # 'NUMBER'",
             instead of the word 'NUMBER' the number of the order you are looking for should be displayed.
             The user sees all available information about the order, including status"""
        email = self.email
        last_name = self.last_name
        state = self.state

        page = CheckoutPage(driver, CheckoutPage.URL)
        page.open()
        order_id = page.full_guest_place_order_us_address_flat_shipping(state, email, self.first_name,
                                                                        last_name, self.street_address, self.city,
                                                                        self.us_postcode_state(state),
                                                                        self.phone_number)

        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.find_order_by_email(order_id, last_name, email)

        assert page.text_order_number_on_view_order_page().text == f"Order # {order_id}", 'Не удалось отследить существующий заказ'
        assert page.order_status(), 'У заказа отсутствует статус'

    def test_by_postcode(self, driver, add_3_item_to_cart):
        """TC_012.009.007 | Footer > “Orders and Returns” > Search for an existing order By Email or ZIP Code\n
        Pre-conditions:
            The user must place an order on the website.
            User not logged into the account and is on the page
             (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
        Steps:
            1)The user selects "ZIP Code" in the "Find Order By" field
            2)The user enters the correct data for the existing order in all required fields
            and clicks the “Continue” button.
        Expected results:
            There was a redirect to a page with information about the required order.
            The header says "Order # 'NUMBER'",instead of the word 'NUMBER' the number
            of the order you are looking for should be displayed.
            The user sees all available information about the order, including status"""
        state = self.state
        postcode = self.us_postcode_state(state)
        last_name = self.last_name

        page = CheckoutPage(driver, CheckoutPage.URL)
        page.open()
        order_id = page.full_guest_place_order_us_address_best_way_shipping(state, self.email, self.first_name,
                                                                            last_name, self.street_address, self.city,
                                                                            postcode,
                                                                            self.phone_number)
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.find_order_by_postcode(order_id, last_name, postcode)

        assert page.text_order_number_on_view_order_page().text == f"Order # {order_id}", 'Не удалось отследить существующий заказ'
        assert page.order_status(), 'У заказа отсутствует статус'


class TestChangeFindOrderBy:

    def test_switch_to_zip(self, driver):
        """TC_012.008.004 | Footer > “Orders and Returns” > Visibility and clickability > Verify the finding
         criterion is "Billing ZIP code" upon choosing "ZIP code" in "Find Order By" field/n
            Preconditions:
                User not logged into the account and is on the page  (url = https://magento.softwaretestingboard.com/sales/guest/form/).
            Steps:
                Select 'ZIP Code' in the 'Find Order By' dropdown
            Expected result:
                The name of the fourth field is 'Billing ZIP Code'"""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.select_find_order_by_postcode_dropdown()
        assert page.billing_postcode_field_name().text == OrdersAndReturnsPageLocators.TEXT_NAME_POSTCODE_FIELD, 'не произошло переключение поиска заказа с Email на ZIP'

    def test_switch_to_email(self, driver):
        """TC_012.008.005 | Footer > “Orders and Returns” > Visibility and clickability > Verify the finding
        criterion is "Email" upon choosing "Email" in "Find Order By" field/n
            Preconditions:
                User not logged into the account and is on the page (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
            Steps:
                1)Select 'ZIP Code' in the 'Find Order By' dropdown
                2)Make sure the "Find Order By" field is "ZIP code"
                3)Select 'Email' in the 'Find Order By' dropdown
            Expected result:
                The name of the fourth field is 'Email'"""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        page.select_find_order_by_postcode_dropdown()
        assert page.billing_postcode_field_name().text == OrdersAndReturnsPageLocators.TEXT_NAME_POSTCODE_FIELD, 'не произошло переключение поиска заказа с Email на ZIP'
        page.select_find_order_by_email_dropdown()
        assert page.email_field_name().text == OrdersAndReturnsPageLocators.TEXT_NAME_EMAIL_FIELD, 'не произошло переключение поиска заказа с ZIP на Email'


class TestFieldsAreSavedInputData(FakeData):

    def test_filling_fields_with_email(self, driver):
        """TC_012.008.006 | Footer > “Orders and Returns” > Visibility and clickability > Saving entered
         information in fields/n
         Preconditions:
                User not logged into the account and is on the page
                (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
         Steps:
                The user fills in all required fields ( Order ID , Billing Last Name , Email )
         Expected result:
                All information entered by the user is saved in the input fields and is displayed correctly
                *The same result should be if you select Find Order By ZIP Code
                and instead of email indicate zip code"""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        order_id = self.fake_order_id
        billing_last_name = self.last_name
        email = self.email
        page.fill_all_field_with_email(order_id, billing_last_name, email)

        assert page.get_value_order_id_field() == str(
            order_id), 'ВВеденая информация в поле Order ID, отображается некорректно'
        assert page.get_value_billing_lastname_field() == billing_last_name, 'ВВеденая информация в поле Billing Last Name, отображается некорректно'
        assert page.get_value_email_field() == email, 'ВВеденая информация в поле Email , отображается некорректно'

    def test_filling_fields_with_postcode(self, driver):
        """TC_012.008.006 | Footer > “Orders and Returns” > Visibility and clickability > Saving entered
        information in fields/n
        Preconditions:
            User not logged into the account and is on the page
            (url = https://magento.softwaretestingboard.com/sales/guest/form/ ) .
        Steps:
            The user fills in all required fields ( Order ID , Billing Last Name , Email )
        Expected result:
            All information entered by the user is saved in the input fields and is displayed correctly
            *The same result should be if you select Find Order By ZIP Code
            and instead of email indicate zip code"""
        page = OrdersAndReturnsPage(driver, url=OrdersAndReturnsPage.URL)
        page.open()
        order_id = self.fake_order_id
        billing_last_name = self.last_name
        postcode = self.postcode
        page.fill_all_field_with_postcode(order_id, billing_last_name, postcode)

        assert page.get_value_order_id_field() == str(
            order_id), 'ВВеденая информация в поле Order ID, отображается некорректно'
        assert page.get_value_billing_lastname_field() == billing_last_name, 'ВВеденая информация в поле Billing Last Name , отображается некорректно'
        assert page.get_value_postcode_field() == postcode, 'ВВеденая информация в поле Billing Zip Code, отображается некорректно'
