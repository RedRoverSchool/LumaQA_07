from base.seleniumbase import BasePage
from locators.base_page_locators import BasePageLocators


class FooterPage(BasePage):
    locators = BasePageLocators()

    def check_visibility_advanced_search_link(self):
        """This method verifies if the advanced search link is visible on the footer"""
        return self.is_visible(self.locators.LINK_ADVANCED_SEARCH)

    def check_clickability_advanced_search_link(self):
        """This method verifies if the advanced search link is clickable"""
        return self.is_clickable(self.locators.LINK_ADVANCED_SEARCH)

    def click_advanced_search_link(self):
        """This method clicks on the advanced search link"""
        self.check_clickability_advanced_search_link().click()


    def check_visibility_footer_diabled_link(self):
        """This method heck if an element with <strong> tag in footer is visible"""
        return self.is_visible(self.locators.LINK_DISABLED)

    def chech_visibility_footer_sign_in_link(self):
        return self.is_visible(BasePageLocators.LINK_HEADER_SIGN_IN).click()

    def have_first_footer_block_links_href(self):
        """The method checks if the first footer block consists of links"""
        for element in self.are_elements_visible(BasePageLocators.FIRST_FOOTER_LINKS_BLOCK):
            assert element.get_attribute("href") is not None and element.get_attribute("href").strip() != ""

    def have_second_footer_block_links_href(self):
        """The method checks if the second footer block consists of links"""
        for element in self.are_elements_visible(BasePageLocators.SECOND_FOOTER_LINKS_BLOCK):
            assert element.get_attribute("href") is not None and element.get_attribute("href").strip() != ""

    def get_first_footer_links_block_length(self):
        """The method gets the first footer block links numbers"""
        return self.get_elements_list_length(BasePageLocators.FIRST_FOOTER_LINKS_BLOCK)

    def get_second_footer_links_block_length(self):
        """The method gets the second footer block links numbers"""
        return self.get_elements_list_length(BasePageLocators.SECOND_FOOTER_LINKS_BLOCK)

    def get_first_footer_links_block_texts(self):
        """The method gets the first footer block links texts"""
        first_footer_links_block = self.are_elements_visible(BasePageLocators.FIRST_FOOTER_LINKS_BLOCK)
        return [link.text for link in first_footer_links_block]

    def get_second_footer_links_block_texts(self):
        """The method gets the second footer block links texts"""
        second_footer_links_block = self.are_elements_visible(BasePageLocators.SECOND_FOOTER_LINKS_BLOCK)
        return [link.text for link in second_footer_links_block]

    def get_first_footer_block_links_urls(self):
        """The method gets the first footer block links URLs"""
        urls_list = []
        for url in self.are_elements_visible(BasePageLocators.FIRST_FOOTER_LINKS_BLOCK):
            urls_list.append(url.get_attribute("href"))

        return urls_list

    def get_second_footer_block_links_urls(self):
        """The method gets the second footer block links URLs"""
        urls_list = []
        for url in self.are_elements_visible(BasePageLocators.SECOND_FOOTER_LINKS_BLOCK):
            urls_list.append(url.get_attribute("href"))

        return urls_list
