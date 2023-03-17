from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://altwalker.github.io/jekyll-ecommerce/"

class snipcart_initialized_and_ready():
    """An expectation for checking if snipcart is initialized."""

    def __call__(self, driver):
        return driver.execute_script("return typeof Snipcart !== 'undefined' && typeof Snipcart._initialized !== 'undefined' && typeof Snipcart.ready !== 'undefined' && Snipcart._initialized && Snipcart.ready;")  # noqa: E501


class BasePage:
    """Interact with elements common on every page."""

    _cart_holder = (By.CSS_SELECTOR, ".snip-open")
    _home_button_locator = (By.CSS_SELECTOR, "header .site-title")
    _cart_button_locator = (By.CSS_SELECTOR, "header .snipcart-checkout")
    _cart_locator = (By.ID, "snipcart-main-content")
    _cart_close_button_locator = (By.ID, "snipcart-close")
    _total_items_in_cart_locator = (By.CSS_SELECTOR, ".snipcart-total-items")
    _cart_items_list_holder_locator = (By.CSS_SELECTOR, "#snipcart-sub-content")

    def __init__(self, driver, base_url=BASE_URL):
        self.driver = driver
        self.base_url = base_url

    @property
    def is_cart_button_present(self):
        return self.is_element_present(*self._cart_button_locator)

    @property
    def is_cart_open(self):
        return self.is_element_present(*self._cart_holder)

    @property
    def total_items_in_cart(self):
        return int(self.driver.find_element(*self._cart_button_locator).find_element(*self._total_items_in_cart_locator).text)
    
    def wait_to_load(self):
        self.driver.find_element(*self._cart_button_locator)
        self.driver.find_element(*self._home_button_locator)
        return self

    def wait_for_snipcart(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(snipcart_initialized_and_ready())

    def wait_for_cart_reload(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self._cart_items_list_holder_locator)
        )
        from pages.cart import CartPage
        return CartPage(self.driver)
        
    def click_cart_button(self):
        self.wait_for_snipcart()
        self.driver.find_element(*self._cart_button_locator).click()
        from pages.cart import CartPage
        return CartPage(self.driver).wait_for_snipcart()

    def click_close_cart_button(self):
        self.wait_for_element_to_be_clickable(self._cart_close_button_locator)
        self.driver.find_element(*self._cart_close_button_locator).click()
        return self

    def click_home_button(self):
        self.driver.find_element(*self._home_button_locator).click()
        from pages.home import HomePage
        return HomePage(self.driver)


    def is_element_present(self, *locator):
        self.driver.implicitly_wait(0)
        try:
            self.driver.find_element(*locator)
            return True
        except:
            return False
        finally:
            self.driver.implicitly_wait(15)
            
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )