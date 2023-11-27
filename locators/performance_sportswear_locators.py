from selenium.webdriver.common.by import By

class PerformanceSportsWearPageLocators():
    Element_of_Card=(By.CSS_SELECTOR,'li:nth-child(1) > div > a > span > span > img')
    Button_Add_to_Wish=(By.CSS_SELECTOR,'li:nth-child(1) div div a.action.towishlist')
    Button_Add_to_Cart=(By.CSS_SELECTOR,'li:nth-child(1) div.actions-primary button > span')
    Button_Add_to_Compare=(By.CSS_SELECTOR,'li:nth-child(1) div.actions-secondary a.action.tocompare')
    Page_Customer_Login=(By.TAG_NAME,'h1')
    Page_Checkbox_Compare=(By.CSS_SELECTOR,'div[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
    Name_Product_Before=(By.CSS_SELECTOR,'li:nth-child(1)  div strong')
    Name_Product_After=(By.CSS_SELECTOR,'ul.items li.item.product strong')