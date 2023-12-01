from selenium.webdriver.common.by import By

class PrivacyCookiePolicyPageLocators:
    YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_HEADER_LOCATOR = "//h2[@id='privacy-policy-title-7']"
    YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT_CONTENT_LOCATOR = "//*[preceding::h2[text()='Your Choices Regarding Use Of The Information We Collect']][following::h2[text()='Your California Privacy Rights']]"
    LIST_OF_COOKIE_FILES_WE_COLLECT_CONTENT_LOCATOR = "//h2[@id='privacy-policy-title-10']/ ../table[@class='data-table']"
    LIST_OF_COOKIE_FILES_WE_COLLECT_LINK_IN_TEXT_BLOCK = "//p//a[text()='List of cookies we collect']"
    CONTACT_US_LINK_LOCATOR = (By.XPATH, "//p//a[text()='Contact Us']")

class PrivacyCookiePolicyAnchorLinksLocators:
    LUMA_SECURITY = "//a[@href='#privacy-policy-title-1']"
    LUMA_PRIVACY_POLICY = "//a[@href='#privacy-policy-title-2']"
    THE_INFORMATION_WE_COLLECT = "//a[@href='#privacy-policy-title-3']"
    HOW_WE_USE_THE_INFORMATION_WE_COLLECT = "//a[@href='#privacy-policy-title-4']"
    SECURITY = "//a[@href='#privacy-policy-title-5']"
    OTHERS_WITH_WHOM_WE_SHARE_YOUR_INFORMATION = "//a[@href='#privacy-policy-title-6']"
    YOUR_CHOICES_REGARDING_USE_OF_THE_INFORMATION_WE_COLLECT = "//a[@href='#privacy-policy-title-7']"
    YOUR_CALIFORNIA_PRIVACY_RIGHTS = "//a[@href='#privacy-policy-title-8']"
    COOKIES_WEB_BEACONS_AND_HOW_WE_USE_THEM = "//a[@href='#privacy-policy-title-9']"
    LIST_OF_COOKIES_WE_COLLECT = "//a[@href='#privacy-policy-title-10']"
    ONLINE_ACCOUNT_REGISTRATION = "//a[@href='#privacy-policy-title-11']"
    EMAILS = "//a[@href='#privacy-policy-title-12']"
    ACCEPTANCE = "//a[@href='#privacy-policy-title-13']"
    QUESTIONS_FOR_LUMA = "//a[@href='#privacy-policy-title-14']"
