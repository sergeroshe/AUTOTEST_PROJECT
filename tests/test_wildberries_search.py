from pages import Main_page, ProductsForWomen, WomenOuterwear


def test_is_search_result_relevant(wildberries_main_page, driver):
    wildberries_main_page: Main_page
    wildberries_main_page.check_search_results()
    assert wildberries_main_page.both_words_present()


def test_product_menu(women_outerwear_page, driver):
    women_outerwear_page: ProductsForWomen
    women_outerwear_page.open_women_outerwear_page()
    assert women_outerwear_page.is_page_loaded()


def test_search_jackets(jackets_search, driver):
    searched_item = 'Куртка'
    jackets_search: WomenOuterwear
    jackets_search.go_to_site()
    outerwear_page_content = jackets_search.get_outerwear_page_content()
    assert searched_item in outerwear_page_content
