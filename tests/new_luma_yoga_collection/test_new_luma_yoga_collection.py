import pytest
import allure
from selenium.webdriver.common.by import By
from locators.new_luma_yoga_collection_locators import PriceTabLocators
from tests.new_luma_yoga_collection.conftest import (
    new_luma_yoga_collection_page_precondition_for_test_data,
)

PRICE_LEVELS = [
    "$10.00 - $19.99",
    "$20.00 - $29.99",
    "$30.00 - $39.99",
    "$40.00 - $49.99",
    "$50.00 - $59.99",
    "$60.00 - $69.99",
    "$70.00 - $79.99",
    "$80.00 - $89.99",
    "$90.00 and above",
]
UPDATABLE_PRICE_LEVEL_LIST = PRICE_LEVELS[:]


class TestPriceLevelsVisibleClickable:
    PARAMETERS = [
        "visibility",
        "clickability",
    ]
    
    def collect_test_data():
        test_data = []
        with allure.step("Open the New Luma Yoga Collection Page"):
            collection_page = new_luma_yoga_collection_page_precondition_for_test_data()
        with allure.step('Locate and open the "Price" tab on the sidebar'):
            price_tab = collection_page.find_price_tab()
            price_tab.click()
        with allure.step("Find Price Levels in the Price Tab"):
            price_levels = collection_page.find_price_list(
                locator=PriceTabLocators.PRICE_LIST
            )
            with allure.step(
                "Collecting titles of each Price Level and collecting Locators"
            ):
                for idx, price_level in enumerate(price_levels):
                    price_level_link = price_level.get_attribute("href")
                    link_locator = (
                        By.XPATH,
                        PriceTabLocators.PRICE_LIST[1]
                        + f"[@href='{price_level_link}']",
                    )
                    spans = price_level.find_elements(
                        *PriceTabLocators.PRICE_TITLES_LOCATOR
                    )
                    titles = [span.text for span in spans]
                    separator = price_level.get_property("childNodes")[2]["nodeValue"]
                    combined_titles_text = (
                        f"{titles[0]+separator}".rstrip(" ")
                        if idx == len(price_levels) - 1
                        else f"{separator}".join(titles)
                    )
                    with allure.step(
                        "Verify the precense of the current Price Level in requiered price levels list"
                    ):
                        assert combined_titles_text == PRICE_LEVELS[idx]
                        UPDATABLE_PRICE_LEVEL_LIST.remove(combined_titles_text)
                    test_data.append([link_locator, combined_titles_text])

        with allure.step("Comparison between collected and expected price lists"):
            assert (
                not UPDATABLE_PRICE_LEVEL_LIST
            ), "The Price List isn't full filled in according to specification"
        collection_page.driver.quit()
        return test_data
    
    TEST_DATA = collect_test_data()

    @pytest.mark.parametrize("param", PARAMETERS)
    @pytest.mark.parametrize("price_level_locator,price_level", TEST_DATA)
    def test_check_visibility_or_clickability_of_price_levels_in_the_price_tab(
        self,
        param,
        price_level_locator,
        price_level,
        new_luma_yoga_collection_page_precondition,
    ):
        """
        TC_006.010.001-TC_006.010.002  | New Luma Yoga Collection > Price levels> Verify Visibility/Clickability of Price levels in the Price tab
        """
        with allure.step("Open the New Luma Yoga Collection Page"):
            collection_page = new_luma_yoga_collection_page_precondition
        with allure.step('Locate and open the "Price" tab on the sidebar'):
            price_tab = collection_page.find_price_tab()
            price_tab.click()
        with allure.step(
            f'Confirm the presence({param}) of the curren price level({price_level}) in the "Price" tab.'
        ):
            collection_page.verify_visability_or_clickability_of_the_element_in_location(
                param=param,
                element_value=f"The Price Level({price_level})'",
                element_locator=price_level_locator,
                location="price table",
            )
            
    @pytest.mark.parametrize("price_level_locator,price_level", TEST_DATA)
    def test_verify_ability_to_filter_the_page_by_price_level(
        self,
        price_level_locator,
        price_level,
        new_luma_yoga_collection_page_precondition,
    ):
        """
        TC_006.010.003 | New Luma Yoga Collection > Price levels> Verify ability to Filter the page by Price level
        """

        with allure.step("Open the New Luma Yoga Collection Page"):
            collection_page = new_luma_yoga_collection_page_precondition
        with allure.step('Locate and open the "Price" tab on the sidebar'):
            price_tab = collection_page.find_price_tab()
            price_tab.click()
        with allure.step(f'Clicking on the specified price level("{price_level}")'):
            price_tab.find_element(*price_level_locator).click()

        with allure.step(
            f'Verifying that after the filtering there is a label "Now Shopping by" in the top left corner and under this label user can see the current price level ({price_level})'
        ):
            assert (
                collection_page.find_title_now_shoping_by() == "Now Shopping by"
            ), "Missing the title(Now Shopping by) in the side bar. Please check it manually, or take a look at the page loading delay"
            assert (
                collection_page.find_price_level_after_filter() == price_level
            ), f"Mismatch between price level({price_level}) filter and title"
