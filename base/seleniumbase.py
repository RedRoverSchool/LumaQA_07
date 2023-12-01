from os import path, pardir
from time import strftime

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

from locators.base_page_locators import BasePageLocators


class BasePage:
    TIMEOUT = 15
    ATTEMPTS = 10
    MESSAGE = (By.CSS_SELECTOR, "[data-ui-id^='message-']")
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, "[data-ui-id='message-success']")
    MESSAGE_NOTICE = (By.CSS_SELECTOR, "[data-ui-id='message-notice']")
    MESSAGE_ERROR = (By.CSS_SELECTOR, "[data-ui-id='message-error']")
    """
    Базовый класс для страниц веб-приложения, использующий Selenium для взаимодействия с элементами на странице.

    Args:
        driver: WebDriver, экземпляр Selenium WebDriver для управления браузером.
        url (str): URL страницы, которую необходимо открыть при инициализации объекта.

    Methods:
        open(): Открывает URL страницы в браузере, связанном с данным объектом.
        
        is_visible(locator: tuple, timeout: int = 10) -> WebElement: Ожидает видимость элемента, заданного локатором, в течение указанного времени. Возвращает WebElement, если элемент видим, или вызывает исключение TimeoutException, если элемент не появился.
        
        is_clickable(locator, timeout: int = 10): Ожидает, что элемент, заданный локатором, станет кликабельным в течение указанного времени. Если элемент становится кликабельным, функция возвращает элемент, иначе вызывает исключение TimeoutException.

    Note:
        Для использования этого класса необходимо импортировать соответствующие модули и создать экземпляр WebDriver перед его инициализацией.
    """

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """
        Открывает URL страницы в браузере.
        """
        self.driver.execute_cdp_cmd("Network.enable", {})
        self.driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {'accept-language': 'en-US,en;q=0.9'}})
        self.driver.get(self.url)
        self.the_presence_of_element_located((By.CSS_SELECTOR, "div.modals-wrapper"))

    def is_visible(self, locator: tuple, timeout: int = TIMEOUT) -> WebElement:
        """
        Ожидает видимость элемента, заданного локатором, в течение указанного времени.

        Args:
            locator (tuple): Локатор элемента, который необходимо найти (например, 'id', 'name', 'css selector', 'xpath', и т.д.).
            timeout (int): Максимальное время ожидания в секундах (по умолчанию 10).

        Returns:
            WebElement: Элемент, если он видим.

        Raises:
            TimeoutException: Если элемент не появился в течение указанного времени.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator: tuple, timeout: int = TIMEOUT) -> WebElement:
        """
        Ожидает, что элемент, заданный локатором, станет кликабельным в течение указанного времени.

        Args:
            locator: Локатор элемента, который необходимо найти (например, 'id', 'name', 'css selector', 'xpath', и т.д.).
            timeout (int): Максимальное время ожидания в секундах (по умолчанию 10).

        Returns:
            WebElement: Элемент, если он становится кликабельным.

        Raises:
            TimeoutException: Если элемент не становится кликабельным в течение указанного времени.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def header(self) -> WebElement:
        return self.is_visible(BasePageLocators.HEADER)

    def wait_overlay_closed(self):
        return self.is_invisible(BasePageLocators.OVERLAY)

    def wait_url_redirection(self, redirect_url, timeout: int = TIMEOUT):
        return wait(self.driver, timeout).until(EC.url_to_be(redirect_url))

    def hold_mouse_on_element(self, locator):
        ActionChains(self.driver).move_to_element(self.is_visible(locator)).perform()

    def hold_mouse_on_element_and_click(self, locator):
        ActionChains(self.driver).move_to_element(self.is_visible(locator)).move_by_offset(40, 0).click().perform()

    def is_invisible(self, locator: tuple, timeout: int = TIMEOUT) -> WebElement:
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))


    def clear_and_send_keys(self, el: WebElement, val: str) -> None:
        el.clear()
        el.send_keys(val)

    @property
    def current_url(self):
        return self.driver.current_url

    @current_url.setter
    def current_url(self, val) -> None:
        self.driver.delete_cookie("mage-messages")
        self.driver.execute_cdp_cmd("Network.enable", {})
        self.driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {'headers': {'accept-language': 'en-US,en;q=0.9'}})
        self.driver.get(val)
        self.the_presence_of_element_located((By.CSS_SELECTOR, "div.modals-wrapper"))

    @property
    def message(self) -> str:
        return self.is_visible(self.MESSAGE).text

    @property
    def message_success(self) -> str:
        return self.is_visible(self.MESSAGE_SUCCESS).text

    @property
    def message_notice(self) -> str:
        return self.is_visible(self.MESSAGE_NOTICE).text

    @property
    def message_error(self) -> str:
        return self.is_visible(self.MESSAGE_ERROR).text

    @property
    def messages_error_list(self):
        return [x.text for x in self.driver.find_elements(*self.MESSAGE_ERROR)]

    def verify_visability_or_clickability_of_the_element_in_location(self, param: str, element_value: str,
                                                                     element_locator: tuple, location: str):
        """ 
        Метод для упрощения проверки нахождения или кликабильности элемента на любой странице в пределах нужной нам локации
        Args:
            param -  параметр, который мы проверяем
            element_value - описание элемента, который мы ищем
            location - если мы ищем элемент в пределах какой то локации, будь то футер, или сайдбар или хэдер...можно описать как вам это нужно

        пример использования можно найти : test/footer/test_verification_footer_elements
        """
        if param == 'visibility':
            assert self.is_visible(
                locator=element_locator), f"'{element_value}' isn't visible in {location} of page with the url = '{self.url}'"
        else:
            assert self.is_clickable(
                locator=element_locator), f"'{element_value}' isn't clickable in {location} of page with the url = '{self.url}'"

    def visible(self, locator: (str, str), timeout: int = TIMEOUT) -> WebElement:
        try:
            return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.shot("visible_timeout")
            raise TimeoutException(f"{timeout}s wait to be visible of {locator}")

    def clickable(self, locator: tuple[str, str], timeout: int = TIMEOUT) -> WebElement:
        try:
            return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.shot("clickable_timeout")
            raise TimeoutException(f"{timeout}s wait to be clickable of {locator}")

    def redirect(self, url, timeout: int = TIMEOUT):
        try:
            return wait(self.driver, timeout).until(EC.url_to_be(url))
        except TimeoutException:
            self.shot("redirect_timeout")
            raise TimeoutException(f"{timeout}s wait to be redirected to {url}")

    def shot(self, file_name='shot'):
        self.driver.save_screenshot(
            path.join(path.dirname(path.abspath(__file__)),
                      pardir, "screenshots", f'{strftime("%H%M%S")}_{file_name}.png'))

    def item_count(self, locator):
        return len(self.driver.find_elements(*locator))

    def scroll_to_element(self, locator) -> WebElement:
        ActionChains(self.driver).scroll_to_element(self.driver.find_element(*locator)).perform()
        return self.driver.find_element(*locator)

    def is_visible_all_elements(self, locator, timeout: int = TIMEOUT) -> list[WebElement]:
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def the_presence_of_element_located(self, locator, timeout: int = TIMEOUT) -> WebElement:
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def get_text(self, locatorOrWebelement) -> str:
        if type(locatorOrWebelement) == WebElement:
            return locatorOrWebelement.text
        else:
            return self.is_visible(locatorOrWebelement).text


    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

