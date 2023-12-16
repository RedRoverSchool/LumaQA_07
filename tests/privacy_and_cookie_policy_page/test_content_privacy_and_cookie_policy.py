from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCheck:
    url = 'https://magento.softwaretestingboard.com/privacy-policy-cookie-restriction-mode'
    header_text_xpath = '//h2 [@id="privacy-policy-title-9"]'
    main_text_xpath = '//h2 [@id="privacy-policy-title-9"]/following-sibling::p'

    def get_header_text_obj(self, driver):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.header_text_xpath)))

    def get_main_text_obj(self, driver):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.main_text_xpath)))

    def is_font_family_of_element_correct(self, element):
        font_style_header = element.value_of_css_property("font-family")
        return font_style_header == '"open sans", "helvetica neue", Helvetica, Arial, sans-serif'

    def test_scrolling_page(self, driver):
        """"
        TC_012.007.006 The Font-size of the text of the block titled "Cookies, Web Beacons, and How We Use Them"
        """
        driver.get(self.url)
        header_text_obj = self.get_header_text_obj(driver)

        ActionChains(driver).scroll_to_element(header_text_obj).perform()

        assert header_text_obj.value_of_css_property('font-size') == '26px'
        assert self.is_font_family_of_element_correct(header_text_obj)

        main_text_obj = self.get_main_text_obj(driver)

        ActionChains(driver).scroll_to_element(main_text_obj).perform()

        assert main_text_obj.value_of_css_property('font-size') == '14px'
        assert self.is_font_family_of_element_correct(main_text_obj)
