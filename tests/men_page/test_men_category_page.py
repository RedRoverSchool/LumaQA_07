import pytest

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

    def test_redirect_by_product_image(self, page_with_tees_filter):
        """
        TC_008.017.004 | Men > Tops > Tees filter
                        > Redirect to the product page by product image
        """

        page = page_with_tees_filter

        page.driver.find_element(*MCL.ITEM_PHOTO).click()

        assert (
                page.driver.current_url == mp_url.STRIKE_ENDURANCE
        ), "Failed to go to the product page by image"

    def test_redirect_by_product_title(self, page_with_tees_filter):
        """
        TC_008.017.005 | Men > Tops > Tees filter
                        > Redirect to the product page by product title
        """

        page = page_with_tees_filter

        page.driver.find_element(*MCL.ITEM_TITLE).click()

        assert (
                page.driver.current_url == mp_url.STRIKE_ENDURANCE
        ), "Failed to go to the product page by title"

    def test_redirect_after_clear(self, page_with_tees_filter):
        """
        TC_008.018.001 | Men > Tops > Tees filter > Clear all
                           > Redirected to Tops page
        """

        page = page_with_tees_filter

        page.click_clear_all()

        assert (
            page.driver.current_url == mp_url.TOPS_MEN_PAGE
        ), "The page didn't redirect to the Tops page"


class TestMenTopsPage:
    def test_redirect_to_tees(self, page_tops):
        """
        TC_008.016.001 | Tops Page > select "Tees" > redirected to Tees Page
        """

        page = page_tops

        page.driver.find_element(*MCL.CATEGORY_BUTTON).click()
        page.driver.find_element(*MCL.TEES_FILTER).click()

        assert (
            page.driver.current_url == mp_url.TEES_FILTER
        ), "The page didn't redirect to the Tees page"


class TestMenBottomsPage:
    def test_grid_is_options_displayed(self, page_bottoms):
        """TC_008.034.001 | Men > Bottoms > Grid mode > Limit controller
                           > Limit elements are displayed
        """

        page = page_bottoms

        page.click_limit_button()

        for name, element in page.get_limit_options():
            assert element.is_displayed(), f'Option "{name}" is not displayed'

    def test_list_is_options_displayed(self, page_bottoms):
        """
        TC_008.034.002 | Men > Bottoms > List mode > Limit controller
                        > Limit elements are displayed
        """

        page = page_bottoms

        page.click_list_mode()
        page.click_limit_button()

        for name, element in page.get_limit_options(mode='list'):
            assert element.is_displayed(), f'Option "{name}" is not displayed'

    @pytest.mark.parametrize('option', ['12', '24', '36'])
    def test_grid_choosing_limit_option(self, page_bottoms, option):
        """
        TC_008.034.003 | Men > Bottoms > Grid mode > Limit controller
                        > Choosing of quantity displaying items on the page
        """

        page = page_bottoms

        page.click_limit_button()
        page.click_option(option)

        assert (
            len([el for el in page.get_all_products() if el.is_displayed()]) <= int(option)
            ), f'The number of items exceeds the limit: {option}'

    @pytest.mark.parametrize('option', ['5', '10', '15', '20', '25'])
    def test_list_choosing_limit_option(self, page_bottoms, option):
        """
        TC_008.034.004 | Men > Bottoms > List mode > Limit controller
                        > Choosing of quantity displaying items on the page
        """

        page = page_bottoms

        page.click_list_mode()
        page.click_limit_button()
        page.click_option(option)

        assert (
                len([el for el in page.get_all_products() if el.is_displayed()]) <= int(option)
        ), f'The number of items exceeds the limit: {option}'
