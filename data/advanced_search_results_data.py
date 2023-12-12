def get_advanced_search_results_url(product_name='', sku='', description='',
                                    short_description='', price_from='', price_to=''):
    return (f'https://magento.softwaretestingboard.com/catalogsearch/advanced/result/'
            f'?name={product_name}&sku={sku}&description={description}&short_description={short_description}'
            f'&price%5Bfrom%5D={price_from}&price%5Bto%5D={price_to}')


ERROR_MESSAGE_ON_ADVANCED_SEARCH_RESULTS_PAGE = "We can't find any items matching these search criteria."
PAGE_TITLE = 'Advanced Search Results'
