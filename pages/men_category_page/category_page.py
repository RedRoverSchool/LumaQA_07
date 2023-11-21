from base.seleniumbase import BasePage
from locators.men_page_locators import MenCategoryPageLocators as MCL


class MenCategoryPage(BasePage):
    '''Page for categories on the "Men" page, e.g. Tops, Bottoms.'''

    def is_products_displayed(self) -> bool:
        """
        Returns True if all products are displayed on the page,
        otherwise False.
        """
        items = self.driver.find_elements(*MCL.ITEM_PHOTO)

        return all([item.is_displayed() for item in items])

    def hover_first_item(self) -> None:
        """
        Hovering the mouse over the first item in the product list.
        """
        self.hold_mouse_on_element(MCL.ITEM)

    def is_shadow(self) -> bool:
        """
        Returns True if the first element has a shadow,
        otherwise False
        """
        first_item = self.driver.find_element(*MCL.ITEM)
        box_property = first_item.value_of_css_property('box-shadow')

        return box_property == 'rgba(0, 0, 0, 0.3) 3px 4px 4px 0px'

    def get_product_options(self) -> dict:
        """
        Returns a dictionary where:
            {'element name': WebElement, ...}
        """

        options = {
            'add_to_cart': self.driver.find_element(*MCL.ADD_TO_CART),
            'add_to_wish_list': self.driver.find_element(*MCL.ADD_TO_WISH_LIST),
            'add_to_compare': self.driver.find_element(*MCL.ADD_TO_COMPARE)
        }

        return options
