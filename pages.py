from selenium.webdriver.common.keys import Keys

from base_page import BasePage
from const import INPUT_SEARCH_STRING
from locators import Locators


class Main_page(BasePage):
    TITLE = 'Wildberries — Интернет-магазин модной одежды и обуви'

    def accept_cookies(self):
        self.go_to_site()
        self.click_to(Locators.ACCEPT_COOKIES_BUTTON)

    def is_cookies_popup_not_visible(self):
        is_popup_visible = not self.find_element(Locators.ACCEPT_COOKIES_BUTTON).is_displayed()
        return is_popup_visible

    def is_page_loaded(self):
        page_loaded = self.find_element(Locators.OUTERWEAR_PAGE_BOTTOM)
        return page_loaded

    def check_search_results(self, request_string=INPUT_SEARCH_STRING):
        self.go_to_site()
        search_input = self.find_element(Locators.SEARCH_BUTTON)
        search_input.click()
        search_input.send_keys(request_string)
        search_input.send_keys(Keys.ENTER)

    def page_content(self):
        page_content_ = self.driver.page_source
        return page_content_

    def both_words_present(self, input_string=INPUT_SEARCH_STRING):
        first_word = input_string.split()[0]
        second_word = input_string.split()[1]
        page_content = self.page_content()
        both_words_present = first_word, second_word in page_content
        return both_words_present

    def scroll_page(self, driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def is_page_scrolled(self):
        page_bottom = self.find_element(Locators.MAIN_PAGE_BOTTOM)
        page_bottom_visible = page_bottom.is_displayed()
        return page_bottom_visible

    def open_login_menu(self):
        self.go_to_site()
        login_menu = self.find_element(Locators.PROFILE_ICON)
        login_menu.click()

    def enter_phone_number(self, phone_number='+375 222 22-22-22'):
        phone_number_placeholder = self.find_element(Locators.PHONE_NUMBER_PLACEHOLDER)
        phone_number_placeholder.send_keys(phone_number)
        phone_number_placeholder.send_keys(Keys.ENTER)

    def is_captcha_appeared(self):
        is_captcha_appeared_ = self.is_existing(Locators.CAPTCHA_CODE_PLACEHOLDER)
        return is_captcha_appeared_


class Payment_Methods(BasePage):
    TITLE = 'Способы оплаты'

    def open_bank_card_menu(self):
        self.go_to_site()
        self.click_to(Locators.BANK_CARD_DROPDOWN)

    def visa_present(self):
        visa_present_ = self.find_element(Locators.VISA_ICON)
        return visa_present_


class SellerPage(BasePage):
    TITLE = 'Wildberries'

    def open_country_codes(self):
        self.go_to_site()
        self.click_to(Locators.COUNTRY_CODE_SWITCHER)

    def switch_to_belarus_phone_code(self):
        self.click_to(Locators.BELARUS_PHONE_CODE_SWITCHER)

    def is_belarus_phone_code_appeared(self):
        belarus_country_code = self.is_existing(Locators.BELARUS_PHONE_CODE)
        return belarus_country_code


class WomenOuterwear(BasePage):
    TITLE = 'Верхняя одежда'

    def open_women_outerwear_page(self):
        self.go_to_site()
        self.click_to(Locators.PRODUCT_MENU)
        self.click_to(Locators.ITEMS_FOR_LADIES)
        self.click_to(Locators.OUTERWEAR_FOR_LADIES)

    def get_outerwear_page_content(self):
        self.go_to_site()
        page_content = self.driver.page_source
        return page_content

    def is_page_loaded(self):
        page_loaded = self.find_element(Locators.WOMEN_OUTERWEAR_PAGE_BOTTOM)
        return page_loaded

    def specify_jackets(self):
        self.click_to(Locators.JACKETS_SELECT)
        return JacketSearch(self.driver, self.driver.current_url)


class JacketSearch(BasePage):
    TITLE = 'Верхняя одежда'

    def select_jackets(self):
        self.go_to_site()
        self.click_to(Locators.ACCEPT_COOKIES_BUTTON)
        self.click_to(Locators.FILTER_DROPDOWN)
        self.click_to(Locators.JACKETS_SELECT)
        self.click_to(Locators.CLOSE_FILTER_BUTTON)

    def check_is_sorted_by_price(self):
        self.click_to(Locators.FILTER_PRICE_DROPDOWN)
        elements = self.find_elements_by_price(Locators.OUTERWEAR_PAGE_CONTENT)
        return elements

