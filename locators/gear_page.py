from selenium.webdriver.common.by import By

# Categories on Gear page
side_bar_elements = (By.XPATH,'//dd//a')
sidebar_main = (By.XPATH,'//div[@class="sidebar sidebar-main"]')
shop_by_title = (By.XPATH,'.//div[@class="title"]/strong')
category_title = (By.XPATH,'//dl[@id="narrow-by-list2"]/dt')

# category page
last_item_counter = (By.XPATH,'//p[@id="toolbar-amount"]//span[last()]')

item_on_the_page = (By.XPATH,'//a[@class="product-item-link"]')
next_button = (By.XPATH,'//div[@class="pages"]//a[@class="action  next"][last()]')