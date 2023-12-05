from data.whats_new_page import NewInWomenLinks as l, WHATS_NEW_PAGE
from locators.whats_new_page_locators import NewInWomenLocators as loc


# TC006.001.002 - 006.001.007 Click to categories New in Women's
class TestNewInWomenLinks:
    def test_hoodies(self, driver):
        driver.get(WHATS_NEW_PAGE)
        hoodies = driver.find_element(*loc.hoodies_title)
        hoodies.click()
        assert driver.current_url == l.hoodies_link

    def test_jackets(self, driver):
        driver.get(WHATS_NEW_PAGE)
        jackets = driver.find_element(*loc.jackets_title)
        jackets.click()
        assert driver.current_url == l.jackets_link

    def test_tees(self, driver):
        driver.get(WHATS_NEW_PAGE)
        tees = driver.find_element(*loc.tees_title)
        tees.click()
        assert driver.current_url == l.tees_link

    def test_bra(self, driver):
        driver.get(WHATS_NEW_PAGE)
        bra = driver.find_element(*loc.bra_title)
        bra.click()
        assert driver.current_url == l.bra_link

    def test_pants(self, driver):
        driver.get(WHATS_NEW_PAGE)
        pants = driver.find_element(*loc.pants_title)
        pants.click()
        assert driver.current_url == l.pants_link

    def test_shorts(self, driver):
        driver.get(WHATS_NEW_PAGE)
        shorts = driver.find_element(*loc.shorts_title)
        shorts.click()
        assert driver.current_url == l.shorts_link
