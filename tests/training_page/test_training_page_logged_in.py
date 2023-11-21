import time

from pages.account.create_account import CreateAccountPage
from locators.training_page_locators import TrainingPageLocators as tpl


"""TC_010.002.001 | Training > Category "Video Download" > Visibility"""
"""Pre-conditions:
        User is logged in
        Training page is opened

    Steps:
        Verify if the ”Video download” link is displayed on the left menu of the page

    Expected results:
        ”Video Download” link is visible (and contains correct text)"""

"""TC_010.002.002 | Training > Category "Video Download" > Link hovering appearance"""
"""Pre-conditions:
        User is logged in
        Training page is opened
    
    Steps:
        Hover over “Video Download” link
    
    Expected results:
        Cursor changes the appearance
        “Video Download” link is underlined"""

"""TC_010.005.001 | Training > Block 2 ("Block-promo training-erin") > Block visibility"""
"""Pre-conditions:
        User is logged in
        Training page is opened
    
    Steps:
        Verify if the Block 2 ("Block-promo training-erin") is displayed on the page
    
    Expected results:
        Block 2 ("Block-promo training-erin") is visible"""

"""TC_010.005.002 | Training > Block 2 ("Block-promo training-erin") > Text_1 visibility"""
"""Pre-conditions:
        User is logged in
        Training page is opened
    
    Steps:
        Verify if the text "Before creating Luma, pro trainer Erin Renny helped world-class athletes reach peak fitness." is visible
    
    Expected results:
        The text "Before creating Luma, pro trainer Erin Renny helped world-class athletes reach peak fitness." is visible"""

"""TC_010.005.003 | Training > Block 2 ("Block-promo training-erin") > Text_2 visibility"""
"""Pre-conditions:
        User is logged in
        Training  page is opened
    
    Steps:
        Verify if the text "Hand-selected by Erin, our training downloads reflect a commitment to yoga, health and wellness." is visible
    
    Expected results:
        The text "Hand-selected by Erin, our training downloads reflect a commitment to yoga, health and wellness." is visible"""

"""TC_010.005.004 | Training > Block 2 ("Block-promo training-erin") > Cursor hovering appearance"""
"""Pre-conditions:
        User is logged in
        Training page is opened
    
    Steps:
        Hover over Block 2
    
    Expected results:
        The cursor changes its appearance when hovering over the Block 2"""

"""TC_010.007.001 | Training >Block 3 ("Training on demand") > Visibility"""
"""Pre-conditions:
        User is logged in
        Training page is opened
    
    Steps:
        Verify if the Block 3 ("Training on demand") is displayed on the page
    
    Expected results:
        Block 3 ("Training on demand") is visible"""

"""TC_010.007.002 | Training > Block 3 ("Training on demand") > Cursor hovering appearance"""
"""Pre-conditions:
        User is logged in
        Training page is opened
    
    Steps:
     Hover over Block 3 ("Training on demand")
    
    Expected results:
        The cursor changes its appearance when hovering over the Block 3"""

"""TC_010.009.001 | Training > Block 4 ("Top Videos") > Visibility"""
"""Pre-conditions:
        User is logged in
        Training page is opened

    Steps:
        Verify "Top Videos Stream free with subscription" text is displayed

    Expected results:
        "Top Videos Stream free with subscription" text is visible"""


class TestTrainingPageLoggedIn:
    def test_training_page_elements_visibility(self, driver):
        page = CreateAccountPage(driver)
        page.is_clickable(tpl.TRAINING_MENU).click()

        """TC_010.002.001 | Training > Category "Video Download" > Visibility"""
        assert page.is_visible(tpl.VIDEO_DOWNLOAD), "Video download link is not displayed"

        """TC_010.005.001 | Training > Block 2 ("Block-promo training-erin") > Block visibility"""
        assert page.is_visible(tpl.BLOCK2), "Block 2 is not displayed"

        """TC_010.005.002 | Training > Block 2 ("Block-promo training-erin") > Text_1 visibility"""
        assert page.is_visible(tpl.BLOCK2_TEXT_1).text == 'Before creating Luma, pro trainer Erin Renny helped world-class athletes reach peak fitness', "Block 2 Text 1 is not visible"

        """TC_010.005.003 | Training > Block 2 ("Block-promo training-erin") > Text_2 visibility"""
        assert page.is_visible(tpl.BLOCK2_TEXT_2).text == 'Hand-selected by Erin, our training downloads reflect a commitment to yoga, health and wellness.', "Block 2 Text 2 is not visible"

        """TC_010.007.001 | Training >Block 3 ("Training on demand") > Visibility"""
        assert page.is_visible(tpl.BLOCK3), 'Block 3 is not displayed'

        """TC_010.009.001 | Training > Block 4 ("Top Videos") > Visibility"""
        assert page.is_visible(tpl.BLOCK4).text == 'Top Videos\nStream free with subscription', "Block 3 Text is not visible"

    def test_training_page_elements_hovering(self, driver):
        page = CreateAccountPage(driver)
        page.is_clickable(tpl.TRAINING_MENU).click()
        # Выполнение JavaScript-скрипта для получения стандартного стиля курсора
        cursor_style_script = """var cursorStyle = getComputedStyle(document.body).cursor;
                                 return cursorStyle;"""
        init_cursor_style = driver.execute_script(cursor_style_script)

        """TC_010.002.002 | Training > Category "Video Download" > Link hovering appearance"""
        page.hold_mouse_on_element(tpl.VIDEO_DOWNLOAD)
        cursor_style = page.is_visible(tpl.VIDEO_DOWNLOAD).value_of_css_property("cursor")
        video_download_link_style_2 = page.is_visible(tpl.VIDEO_DOWNLOAD).value_of_css_property("text-decoration").split(' ')
        assert init_cursor_style != cursor_style and cursor_style == 'pointer', "Cursor didn't change appearance after hovering over “Video Download” link"
        assert video_download_link_style_2[0] == 'underline', "“Video Download” link is not underlined after cursor hovering"

        """TC_010.005.004 | Training > Block 2 ("Block-promo training-erin") > Cursor hovering appearance"""
        page.hold_mouse_on_element(tpl.BLOCK2)
        cursor_style = page.is_visible(tpl.BLOCK2).value_of_css_property("cursor")
        assert init_cursor_style != cursor_style and cursor_style == 'pointer', "Cursor didn't change appearance after hovering over Block 2"

        """TC_010.007.002 | Training > Block 3 ("Training on demand") > Cursor hovering appearance"""
        page.hold_mouse_on_element(tpl.BLOCK3)
        cursor_style = page.is_visible(tpl.BLOCK3).value_of_css_property("cursor")
        assert init_cursor_style != cursor_style and cursor_style == 'pointer', "Cursor didn't change appearance after hovering over Block 3"

