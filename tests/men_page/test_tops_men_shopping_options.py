from pages.men_category_page.men_tops_page import MenTops
from data.men_page_url import TOPS_MEN_PAGE


def test_shopping_menu(driver):
    page = MenTops(driver, TOPS_MEN_PAGE)
    page.open()
    data = page.check_menu_shopping_options()
    assert data == ['CATEGORY', 'STYLE', 'SIZE', 'PRICE', 'COLOR', 'MATERIAL', 'ECO COLLECTION',
                    'PERFORMANCE FABRIC', 'ERIN RECOMMENDS', 'NEW', 'SALE', 'PATTERN',
                    'CLIMATE'], 'menu items do not exist'
