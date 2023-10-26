import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages import Main_page, Payment_Methods, SellerPage, WomenOuterwear, JacketSearch
from const import BASE_URL, PAYMENT_METHODS_PAGE, SELLER_PAGE, WOMEN_OUTERWEAR_PAGE, JACKETS_SELECT_PAGE


def create_driver():
    # options = Options()
    manager = ChromeDriverManager()
    service = Service(manager.install())
    driver = selenium.webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    return driver


@pytest.fixture(scope='session')
def driver():
    driver_ = create_driver()
    driver_.implicitly_wait(5)
    yield driver_
    driver_.close()


@pytest.fixture(scope='function')
def wildberries_main_page(driver):
    main_page_ = Main_page(driver, BASE_URL)
    return main_page_


@pytest.fixture(scope='function')
def payment_methods(driver):
    payment_methods_ = Payment_Methods(driver, PAYMENT_METHODS_PAGE)
    return payment_methods_


@pytest.fixture(scope='function')
def seller_page(driver):
    seller_page_ = SellerPage(driver, SELLER_PAGE)
    return seller_page_


@pytest.fixture(scope='function')
def women_outerwear(driver):
    women_outerwear_ = WomenOuterwear(driver, WOMEN_OUTERWEAR_PAGE)
    yield women_outerwear_


@pytest.fixture(scope='function')
def jackets_search(driver):
    jackets_search_ = JacketSearch(driver, JACKETS_SELECT_PAGE)
    yield jackets_search_
