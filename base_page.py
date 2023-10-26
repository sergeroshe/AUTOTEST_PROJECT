from typing import List
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from const import TIMEOUTS


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

    def find_elements_by_price(self, locator) -> List[WebElement]:
        elements = self.driver.find_elements(By.CLASS_NAME, 'price-current__from hide')
        return elements
