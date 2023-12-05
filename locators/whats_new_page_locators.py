from selenium.webdriver.common.by import By


class WhatsNewPageLocators:
    SENSE_RENEWAL_WIDGET_TITLE = (By.CSS_SELECTOR, '.block-promo-wrapper .new-eco strong')


class NewInWomenLocators:
    new_in_women_title = (By.CSS_SELECTOR, '.categories-menu strong:nth-child(1) span')
    new_in_women_title_text = "NEW IN WOMEN'S"
    hoodies_title = (By.CSS_SELECTOR, '.categories-menu ul:nth-child(2) li:nth-child(1) a')
    hoodies_text = 'Hoodies & Sweatshirts'
    jackets_title = (By.CSS_SELECTOR, '.categories-menu ul:nth-child(2) li:nth-child(2) a')
    jackets_text = 'Jackets'
    tees_title = (By.CSS_SELECTOR, '.categories-menu ul:nth-child(2) li:nth-child(3) a')
    tees_text = 'Tees'
    bra_title = (By.CSS_SELECTOR, '.categories-menu ul:nth-child(2) li:nth-child(4) a')
    bra_text = 'Bras & Tanks'
    pants_title = (By.CSS_SELECTOR, '.categories-menu ul:nth-child(2) li:nth-child(5) a')
    pants_text = 'Pants'
    shorts_title = (By.CSS_SELECTOR, '.categories-menu ul:nth-child(2) li:nth-child(6) a')
    shorts_text = 'Shorts'
