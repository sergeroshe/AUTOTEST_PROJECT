import time
from pages import Main_page, Payment_Methods, SellerPage, ProductsForWomen


def test_is_all_cookies_accepted(wildberries_main_page, driver):
    wildberries_main_page: Main_page
    wildberries_main_page.accept_cookies()
    time.sleep(1)
    assert wildberries_main_page.is_cookies_popup_not_visible()


def test_is_search_result_relevant(wildberries_main_page, driver):
    wildberries_main_page.check_search_results()
    assert wildberries_main_page.both_words_present()


def test_is_page_scrollable(wildberries_main_page, driver):
    wildberries_main_page: Main_page
    wildberries_main_page.scroll_page(driver)
    assert wildberries_main_page.is_page_scrolled()


def test_is_possible_to_authorize_until_captcha(wildberries_main_page):
    wildberries_main_page: Main_page
    wildberries_main_page.open_login_menu()
    wildberries_main_page.enter_phone_number()
    assert wildberries_main_page.is_captcha_appeared()


def test_is_visa_card_presented(payment_methods, driver):
    payment_methods: Payment_Methods
    payment_methods.open_bank_card_menu()
    assert payment_methods.visa_present()


def test_is_sales_available_in_belarus(seller_page, driver):
    seller_page: SellerPage
    seller_page.open_country_codes()
    seller_page.is_belarus_phone_code_appeared()
    seller_page.switch_to_belarus_phone_code()
    assert seller_page.is_belarus_phone_code_appeared()



