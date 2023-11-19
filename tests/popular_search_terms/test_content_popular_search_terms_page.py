from pages.popular_search_terms.popular_search_terms_page import PopularSearchTermsPage
from data.popular_search_terms_page_data import POPULAR_SEARCH_TERMS_PAGE_URL, HEADING_TEXT


class TestContentPopularSearchTermsPage:

    @staticmethod
    def get_keyword_font_size(keyword):
        return float(keyword.get_attribute('style').split(':')[-1].replace('%;', ''))

    def test_verify_heading_on_popular_search_terms_page(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        assert driver.current_url == POPULAR_SEARCH_TERMS_PAGE_URL
        assert page.get_heading().text == HEADING_TEXT, 'Heading is invisible'

    def test_verify_number_of_keywords(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        assert len(page.get_keywords_list()) == 100

    def test_verify_there_are_at_least_5_keywords_with_font_size_larger_88_percent(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        keywords_filtered_list = [keyword for keyword in page.get_keywords_list() if self.get_keyword_font_size(keyword) > 88]

        assert len(keywords_filtered_list) >= 5

    def test_verify_among_keywords_with_enlarged_font_size_are_defined_words(self, driver):
        page = PopularSearchTermsPage(driver, POPULAR_SEARCH_TERMS_PAGE_URL)
        page.open()

        keywords_dict = {keyword.text: self.get_keyword_font_size(keyword) for keyword in page.get_keywords_list()}

        keywords_filtered_list = []
        i = 1
        while i <= 10:
            keyword_name = [key for (key, value) in keywords_dict.items() if value == max(keywords_dict.values())][0]
            keywords_filtered_list.append(keyword_name)
            del keywords_dict[keyword_name]
            i += 1

        assert {'bag', 'HOODIE', 'jacket', 'pants', 'shirt'}.issubset(keywords_filtered_list)
