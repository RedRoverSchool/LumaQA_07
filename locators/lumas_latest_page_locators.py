from selenium.webdriver.common.by import By


class LumasPageLocators:
    Item_List=(By.CSS_SELECTOR,'div.block.widget.block-products-list.grid > div > div > ol')
    Lumas_Latest = (By.CSS_SELECTOR, 'h2[class="title"]')
    Just_in_Time = (By.CSS_SELECTOR, 'p[class="info"]')
    Image_of_Item = (By.CSS_SELECTOR, ' li:nth-child(1) > div > a > span > span > img')

    Name_of_Item = (By.CSS_SELECTOR, 'a[title="Phoebe Zipper Sweatshirt"]')
    Prace_of_Item = (By.CSS_SELECTOR, '#old-price-1130-widget-product-grid>span')
    Size_Choice = (By.CSS_SELECTOR, "#option-label-size-143-item-166")
    Color_Choice = (By.CSS_SELECTOR, '#option-label-color-93-item-52')
    Add_to_Cart=(By.CSS_SELECTOR,'li:nth-child(1) > div > div > div.product-item-inner > div > div.actions-primary > form > button > span')
    IMG=(By.CSS_SELECTOR,'img[class="product-image-photo"]')
    Image_of_Wish=(By.CSS_SELECTOR,'ol > li:nth-child(1) > div > div > div.product-item-inner > div > div.actions-secondary > a.action.towishlist')
    Image_of_Compare=(By.CSS_SELECTOR,'ol > li:nth-child(1) > div > div > div.product-item-inner > div > '
                                      'div.actions-secondary > a.action.tocompare')