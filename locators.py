from selenium.webdriver.common.by import By


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

    FILTER_DROPDOWN = By.XPATH, '//div[@class="filter-more"]//button[@aria-label="Фильтры"]'
    JACKETS_SELECT = By.XPATH, '//span[@class="filter__item-in"][contains(text(), "Куртка")]'
    OUTERWEAR_PAGE_BOTTOM = By.XPATH, '//div[@class="footer-copyright"]'
    FILTER_PRICE_DROPDOWN = By.XPATH, '//button[@class="switcher__item has-alternate"]'
    OUTERWEAR_PAGE_CONTENT = By.XPATH, '//div[@class="catalog"]'
    WOMEN_OUTERWEAR_PAGE_BOTTOM = By.XPATH, '//button[@class="btn--show-more btn btn--secondary-gradient"]'
    CLOSE_FILTER_BUTTON = By.XPATH, '//button[@class="filters-sidebar__close"][@data-tag="sidebarClose"]'
