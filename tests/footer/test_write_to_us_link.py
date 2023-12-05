from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDriver:
    url = 'https://magento.softwaretestingboard.com/'
    write_for_us_link_xpath = '//a[text()="Write for us"]'

    def get_write_for_us_link(self, driver):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.write_for_us_link_xpath)))

    def test_web_page(self, driver):
        """
        TC_012.002.001 | Footer > "Write for us" link > Visibility and clickability
        """
        driver.get(self.url)
        link_obj = self.get_write_for_us_link(driver)

        assert link_obj.is_displayed()
        assert link_obj.is_enabled()

    def test_redirection(self, driver):
        """
        TC_012.002.002 | Footer > "Write for us" link > Redirection
        """
        driver.get(self.url)
        redirection_link = self.get_write_for_us_link(driver)

        redirection_link.click()

        WebDriverWait(driver, 10).until(EC.url_to_be('https://softwaretestingboard.com/write-for-us/'))
