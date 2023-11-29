from selenium.webdriver.common.by import By

class PrivacyCookiePolicyPageLocators:
    YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_HEADER_LOCATOR = "//h2[@id='privacy-policy-title-7']"
    YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_CONTENT_LOCATOR = "//*[preceding::h2[text()='Your Choices Regarding Use Of The Information We Collect']][following::h2[text()='Your California Privacy Rights']]"
    LIST_OF_COOKIE_FILES_WE_COLLECT_CONTENT_LOCATOR = "//h2[@id='privacy-policy-title-10']/ ../table[@class='data-table']"
    LIST_OF_COOKIE_FILES_WE_COLLECT_LINK_IN_TEXT_BLOCK = "//p//a[text()='List of cookies we collect']"
    CONTACT_US_LINK_LOCATOR = "//p//a[text()='Contact Us']"