import data.men_page_url as mp_url
from locators.men_page_locators import MenCategoryPageLocators as MCL


class TestHoodiesSweatshirtsFilter:
    def test_product_are_visible(self, page_with_hs_filter):
        """
        TC_008.014.001 | Men > Tops > Hoodies & Sweatshirts filter
                        > Products are visible on the page
        """

        page = page_with_hs_filter

        assert page.is_products_displayed(), "Element is not displayed on the page"

    def test_item_is_highlighted(self, page_with_hs_filter):
        """
        TC_008.014.002 | Men > Tops > Hoodies & Sweatshirts filter
                        > The item is highlighted with a shadow
        """

        page = page_with_hs_filter

        page.hover_first_item()

        assert page.is_shadow(), "The product is not highlighted with a shadow"

    def test_options_appear_on_the_products(self, page_with_hs_filter):
        """
        TC_008.014.003 | Men > Tops > Hoodies & Sweatshirts filter
                         > Options appear on the product item
        """

        page = page_with_hs_filter

        page.hover_first_item()

        for name, element in page.get_product_options().items():
            assert element.is_displayed(), f"The '{name}' option is not displayed"

    def test_redirect_by_product_image(self, page_with_hs_filter):
        """
        TC_008.014.004 | Men > Tops > Hoodies & Sweatshirts filter
                        > Redirect to the product page by product image
        """

        page = page_with_hs_filter

        page.driver.find_element(*MCL.ITEM_PHOTO).click()

        current_url = page.driver.current_url

        assert (
                current_url == mp_url.MARCO_LIGHTWEIGHT
        ), "Failed to go to the product page by image"

    def test_redirect_by_product_title(self, page_with_hs_filter):
        """
        TC_008.014.005 | Men > Tops > Hoodies & Sweatshirts filter
                        > Redirect to the product page by product title
        """

        page = page_with_hs_filter

        page.driver.find_element(*MCL.ITEM_TITLE).click()

        current_url = page.driver.current_url

        assert (
                current_url == mp_url.MARCO_LIGHTWEIGHT
        ), "Failed to go to the product page by title"


class TestTeesFilter:
    def test_product_are_visible(self, page_with_tees_filter):
        """
        TC_008.017.001 | Men > Tops > Tees filter
                        > Products are visible on the page

        """

        page = page_with_tees_filter

        assert page.is_products_displayed(), "Element is not displayed on the page"

    def test_item_is_highlighted(self, page_with_tees_filter):
        """
        TC_008.017.002 | Men > Tops > Tees filter
                        > The item is highlighted with a shadow

        """
        page = page_with_tees_filter

        page.hover_first_item()

        assert page.is_shadow(), "The product is not highlighted with a shadow"

    def test_options_appear_on_the_products(self, page_with_tees_filter):
        """
        TC_008.017.003 | Men > Tops > Tees filter
                        > Options appear on the product item
        """
        page = page_with_tees_filter

        page.hover_first_item()

        for name, element in page.get_product_options().items():
            assert element.is_displayed(), f"The '{name}' option is not displayed"
