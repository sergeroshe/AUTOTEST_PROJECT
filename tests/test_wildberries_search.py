from pages import Main_page, WomenOuterwear, JacketSearch


def test_is_search_result_relevant(wildberries_main_page: Main_page):
    wildberries_main_page.check_search_results()
    assert wildberries_main_page.both_words_present()


def test_is_main_page_loaded(women_outerwear):
    women_outerwear.open_women_outerwear_page()
    assert women_outerwear.is_page_loaded()


def test_jackets_presented(women_outerwear: WomenOuterwear):
    searched_item = 'Куртка'
    outerwear_page_content = women_outerwear.get_outerwear_page_content()
    assert searched_item in outerwear_page_content


def test_is_page_loaded(women_outerwear):
    assert women_outerwear.is_page_loaded()


def test_jackets_search(jackets_search: JacketSearch):
    jackets_search.select_jackets()
    assert jackets_search.check_is_sorted_by_price()