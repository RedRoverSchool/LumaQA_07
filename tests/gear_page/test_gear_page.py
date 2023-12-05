import allure
import pytest
from selenium.webdriver.common.by import By
from tests.gear_page.conftest import gear_page_precondition_for_test_data
from data.gear_page_urls import BAGS_PAGE, FITNESS_EQ_PAGE, WATCHES_PAGE
from locators.gear_page_locators import GearPageLocators, CategoryPageLocators

total_categories = ["Bags", "Fitness Equipment", "Watches"]
category_list = ["Bags", "Fitness Equipment", "Watches"]
founded_categories = []

list_of_category_url = [
    BAGS_PAGE,
    FITNESS_EQ_PAGE,
    WATCHES_PAGE,
]


class TestGearPageCategory:
    """TC_009.001.001 - TC_009.002.006 for now"""
    
    def find_categories_and_counters_at_the_sidebar():
        """collect test data"""
        test_data = []
        gear_page = gear_page_precondition_for_test_data()
        
        categories = gear_page.find_elements_in_sidebar(locator=GearPageLocators.SIDEBAR_ELEMENTS)
        assert len(categories) == len(
            category_list
        ), f"The number of categories is {len(categories)},(expected = {len(category_list)}).Check, it can be update in category list"
        for category in categories:
            category_xpath = (By.XPATH, f'//dd//a[text()="{category.text}"]')
            counter_xpath = (
                By.XPATH,
                f'{category_xpath[1]}/following-sibling::span[@class="count"]',
            )
            test_data.append([category_xpath, counter_xpath])
        gear_page.driver.quit()
        return test_data
    
   
    def test_find_and_verify_title_of_sidebar(self, gear_page_precondition):
        """
        TC_009.001.001 | Gear page > categories > Shop By Category
        """

        with allure.step("Pre-conditions:A user is on The Gear page"):
            gear_page = gear_page_precondition
        
        with allure.step("Find and verify the title of the sidebar with the text 'Shop By Category'"):
            title_in_the_side_bar = gear_page.find_shop_by_title_in_the_side_bar()
            
            assert (
                title_in_the_side_bar == "Shop By Category"
            ), f"""
                The title of the Sidebar - '{title_in_the_side_bar}'.
                Expected - 'Shop By Category'"""
        
    @pytest.mark.parametrize(
        "category_xpath,counter_xpath", find_categories_and_counters_at_the_sidebar()
    )
    def test_find_and_verify_category_at_the_sidebar(
        self, category_xpath, counter_xpath, gear_page_precondition
    ):
        """TC_009.001.(002-004) | Gear page > categories > category"""

        with allure.step("Pre-conditions: A user is on The Gear page and the sidebar with the text 'Shop By Category' is visible"):
             gear_page = gear_page_precondition

        with allure.step("Find and verify the presence of the category"):
            category,category_name,category_counter,category_url = gear_page.find_category_counter_and_url(category_xpath, counter_xpath)
        
            assert (
                category_name in category_list
            ), f"We found another one category title - '{category_name}', Please check the locators at the Sidebar and list of categories"
            category_list.remove(category_name)
            founded_categories.append(category_name)

    def test_check_category_list(self):
        """Additional step to verify the total list of categories after the previous test cases"""

        missed_category = [
            cat for cat in total_categories if cat not in founded_categories
        ]
        assert (
            not category_list
        ), f"Please check compare the we have found : {founded_categories}, we should found : {total_categories}. we miss {missed_category}"
    

    @pytest.mark.parametrize(
        "category_xpath,counter_xpath", find_categories_and_counters_at_the_sidebar()
    )    
    def test_find_and_verify_location_of_counter_at_the_sidebar(
        self, gear_page_precondition, category_xpath, counter_xpath
    ):
        """
        TC_009.002.(001-003) | Gear page > categories > The counter for the category
        """

        with allure.step("Pre-conditions: User is on The Gear Page and categories are displayed at the 'Shop By Category' sidebar."):
            gear_page = gear_page_precondition

        with allure.step("Verify that the current category is displayed./ Find the counter of this category and verify it's visibility"):
            category,category_name,category_counter,category_url = gear_page.find_category_counter_and_url(category_xpath, counter_xpath)

            assert (
                category_counter
            ), f"We found a counter for {category_name}, but it is empty"


    @pytest.mark.parametrize(
        "category_xpath,counter_xpath", find_categories_and_counters_at_the_sidebar()
    )
    def test_verify_category_counter_on_gear_and_category_page(
        self, driver, wait, gear_page_precondition, category_xpath, counter_xpath
    ):
        """
        TC_009.002.(004-006) | Gear page > categories >
        Verify the counter on the Gear Page for the current category with counter on the Category Page
        """
        with allure.step("Pre-conditions: User is on The Gear Page and categories are displayed at the 'Shop By Category' sidebar."):
            gear_page = gear_page_precondition
        
        with allure.step("Find and verify the counter indicating the quantity of available products in the current category."):
            category,category_name,category_counter,category_url = gear_page.find_category_counter_and_url(category_xpath, counter_xpath)

        with allure.step(f"Click on the {category.text} category to access the category page"):
            category_page = gear_page.rederect_to_the_current_category_page(category,category_url,category_name)
        
        with allure.step(f"Find the counter on the {category_name} category page and note the quantity of available products."):
            counter_on_the_category_page = category_page.is_visible(
                locator=CategoryPageLocators.LAST_ITEM_COUNTER
            ).text

        with allure.step(f"Compare the counter on the Gear page with the counter on the {category_name} category page"):
            assert int(category_counter) == int(
                counter_on_the_category_page
            ), f"""
            The counter of items for the category -{category_name} on the Gear Page {category_counter} 
            not equal to the counter on the category page {counter_on_the_category_page}"""
        