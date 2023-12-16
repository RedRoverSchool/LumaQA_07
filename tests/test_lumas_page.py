from pages.other_pages.lumas_latest import LumasPage


def test_lumas(driver):
    page = LumasPage(driver, 'https://magento.softwaretestingboard.com/what-is-new.html')
    page.open()
    page.find_lumas()
    page.find_lumas_just()
    assert 'Just in time for the new season!' == page.find_lumas_just()
    page.find_elements_lumas()
    page.hold_mou_on_elementse_img()
    page.find_add_button_cart()
    assert 'Add to Cart' == page.find_add_button_cart()
    page.find_add_wish()
    assert "ADD TO WISH LIST" == page.find_add_wish()
    page.find_add_compare()
    assert "ADD TO COMPARE" == page.find_add_compare()




