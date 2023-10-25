from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from const import TIMEOUTS, PAYMENT_METHODS_PAGE, INPUT_SEARCH_STRING, SELLER_PAGE, BASE_URL, OUTERWEAR_PAGE


class Locators:
    ACCEPT_COOKIES_BUTTON = By.XPATH, '//button[contains(text(), "Принять")]'
    SEARCH_BUTTON = By.XPATH, '//input[@class="search-component-input"]'
    SEARCH_INPUT = By.XPATH, '//label[@type="button"]'
    BANK_CARD_DROPDOWN = By.XPATH, '//div[@class="collapse-list"]/div[@class="collapse"]/h2[@class="collapse__title"]'
    VISA_ICON = By.XPATH, '//img[@src="/assets/images/visa.svg"]'
    MAIN_PAGE_BOTTOM = By.XPATH, '//ul[@class="footer-brand"]'
    PROFILE_ICON = By.CSS_SELECTOR, 'svg.svg-icon.icon-account'
    PHONE_NUMBER_PLACEHOLDER = By.XPATH, '//input[@id="phone-input"]'
    AGREEMENT_CHECKBOX = By.XPATH, '//div[@class="agreement agreement--check"]'
    GET_CODE_BUTTON = By.XPATH, '//button[@data-tag="nextBtn"]'
    CAPTCHA_CODE_PLACEHOLDER = By.CSS_SELECTOR, 'input#captcha-input.form-input'
    COUNTRY_CODE_SWITCHER = By.CSS_SELECTOR, 'div svg'
    BELARUS_PHONE_CODE_SWITCHER = By.XPATH, '//span[contains(text(), "Беларусь")]'
    BELARUS_PHONE_CODE = By.XPATH, '//span[contains(text(), "375")]'
    PRODUCT_MENU = By.CSS_SELECTOR, 'svg.svg-icon.icon-search-catalog-desktop'
    ITEMS_FOR_LADIES = By.CSS_SELECTOR, 'span.menu-item__title'
    OUTERWEAR_FOR_LADIES = By.XPATH, '//li[@data-id="63010"]/span[@class="menu-item__title"]'
    FILTER_DROPDOWN = By.XPATH, '//button[@type="button"][@class="filter-more__btn"][@data-tag="btn"]'
    JACKETS_SELECT = By.XPATH, 'span.filter__itemIn'
    OUTERWEAR_PAGE_BOTTOM = By.XPATH, '//div[@class="footer-copyright"]'
    FILTER_PRICE_DROPDOWN = By.CSS_SELECTOR, 'button.switcher__item.has-alternate'
    OUTERWEAR_PAGE_CONTENT = By.CSS_SELECTOR, 'div.catalog__content'


class BasePage:
    TITLE = None

    def __init__(self, driver: Chrome, url: str):
        self.driver = driver
        self.url = url

    def go_to_site(self, timeout=TIMEOUTS.GET_URL):
        self.driver.get(self.url)
        condition = EC.title_is(self.TITLE)
        return WebDriverWait(self.driver, timeout).until(condition)

    def get_page_content(self, driver):
        self.driver.get(self.url)
        page_content = driver.page_source
        return page_content

    def find_element(self, locator: tuple[str, str], timeout=TIMEOUTS.FIND_ELEMENT):
        condition = EC.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until(condition)

    def find_elements(self, locator: tuple[str, str], timeout=TIMEOUTS.FIND_ELEMENT):
        condition = EC.presence_of_all_elements_located(locator)
        return WebDriverWait(self.driver, timeout).until(condition)

    def is_element_clickable(self, locator: tuple[str, str], timeout=TIMEOUTS.FIND_ELEMENT):
        condition = EC.element_to_be_clickable(locator)
        return WebDriverWait(self.driver, timeout).until(condition)

    def is_not_existing(self, locator: tuple[str, str], timeout=TIMEOUTS.FIND_ELEMENT):
        condition = EC.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until_not(condition)

    def is_existing(self, locator: tuple[str, str], timeout=TIMEOUTS.FIND_ELEMENT):
        condition = EC.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until(condition)

    def click_to(self, locator: tuple[str, str], timeout=TIMEOUTS.FIND_ELEMENT):
        element = self.find_element(locator, timeout)
        element.click()
        return element


class Main_page(BasePage):
    TITLE = 'Wildberries — Интернет-магазин модной одежды и обуви'

    def accept_cookies(self):
        self.go_to_site()
        accept_cookies_ = self.find_element(Locators.ACCEPT_COOKIES_BUTTON)
        accept_cookies_.click()

    def is_cookies_popup_not_visible(self):
        is_popup_visible = not self.find_element(Locators.ACCEPT_COOKIES_BUTTON).is_displayed()
        return is_popup_visible

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

    def init(self, driver):
        super().__init__(driver, PAYMENT_METHODS_PAGE)
        self.driver = driver

    def open_bank_card_menu(self):
        self.go_to_site()
        self.click_to(Locators.BANK_CARD_DROPDOWN)

    def visa_present(self):
        visa_present_ = self.find_element(Locators.VISA_ICON)
        return visa_present_


class SellerPage(BasePage):
    TITLE = 'Wildberries'

    def init(self, driver):
        super().__init__(driver, SELLER_PAGE)
        self.driver = driver

    def open_country_codes(self):
        self.go_to_site()
        self.click_to(Locators.COUNTRY_CODE_SWITCHER)

    def switch_to_belarus_phone_code(self):
        self.click_to(Locators.BELARUS_PHONE_CODE_SWITCHER)

    def is_belarus_phone_code_appeared(self):
        belarus_country_code = self.is_existing(Locators.BELARUS_PHONE_CODE)
        return belarus_country_code


#
class ProductsForWomen(BasePage):
    TITLE = 'Wildberries — Интернет-магазин модной одежды и обуви'

    def init(self, driver):
        super().__init__(driver, BASE_URL)
        self.driver = driver

    def open_women_outerwear_page(self):
        self.go_to_site()
        self.click_to(Locators.PRODUCT_MENU)
        self.click_to(Locators.ITEMS_FOR_LADIES)
        self.click_to(Locators.OUTERWEAR_FOR_LADIES)

    def is_page_loaded(self):
        page_loaded = self.find_element(Locators.OUTERWEAR_PAGE_BOTTOM)
        return page_loaded


class WomenOuterwear(BasePage):
    TITLE = 'Верхняя одежда'

    def init(self, driver):
        super().__init__(driver, OUTERWEAR_PAGE)
        self.driver = driver

    def get_outerwear_page_content(self):
        self.go_to_site()
        page_content = self.driver.page_source
        return page_content
