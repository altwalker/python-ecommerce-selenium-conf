import time
from selenium.webdriver.common.by import By
from pages.base import BasePage


class CartPage(BasePage):
    """Interact with element on the cart page."""

    _content_cart_next_step_button_locator = (By.CSS_SELECTOR, "#snipcart-main-content #snipcart-actions a")
    _billing_address_next_step_button_locator = (By.ID, "snipcart-next")
    _payment_next_step_button_locator = (By.ID, "snipcart-paymentmethod-pay")
    _order_confirmation_place_order_button_locator = (By.CSS_SELECTOR, "a.js-submit")
    _billing_address_form_locator = (By.ID, "snipcart-billingaddress-form")

    _billing_name_locator = (By.ID, "snip-name")
    _billing_city_locator = (By.ID, "snip-city")
    _billing_email_locator = (By.ID, "snip-email")
    _billing_street_address1_locator = (By.ID, "snip-address1")
    _billing_postal_code_locator = (By.ID, "snip-postalCode")

    @property
    def is_content_next_button_present(self):
        return self.is_element_present(*self._content_cart_next_step_button_locator)

    @property
    def is_billing_next_button_present(self):
        return self.is_element_present(*self._billing_address_next_step_button_locator)

    @property
    def is_payment_next_button_present(self):
        return self.is_element_present(*self._payment_next_step_button_locator)

    @property
    def is_order_confirmation_present(self):
        return self.is_element_present(*self._order_confirmation_place_order_button_locator)

    def wait_to_load(self):
        time.sleep(0.5)
        self.driver.find_element(*self._cart_holder)

    def click_content_cart_next_step_button(self):
        self.wait_for_snipcart()
        self.driver.find_element(*self._content_cart_next_step_button_locator).click()
        return self

    def click_billing_address_next_step_button(self):
        self.wait_for_snipcart()
        self.driver.find_element(*self._billing_address_next_step_button_locator).click()
        return self

    def click_payment_next_step_button(self):
        self.wait_for_snipcart()
        self.driver.find_element(*self._payment_next_step_button_locator).click()
        return self

    def click_order_confirmation_place_order_button(self):
        self.wait_for_snipcart()
        self.driver.find_element(*self._order_confirmation_place_order_button_locator).click()
        return self

    def fill_in_billing_address_form(self, name="", city="", email="", street_address1="", postal_code=""):
        print("Fill Billing Form")

        if name != "":
            self.driver.find_element(*self._billing_name_locator).clear()
            self.driver.find_element(*self._billing_name_locator).send_keys(name)
        if city != "":
            self.driver.find_element(*self._billing_city_locator).clear()
            self.driver.find_element(*self._billing_city_locator).send_keys(city)
        if email != "":
            self.driver.find_element(*self._billing_email_locator).clear()
            self.driver.find_element(*self._billing_email_locator).send_keys(email)
        if street_address1 != "":
            self.driver.find_element(*self._billing_street_address1_locator).clear()
            self.driver.find_element(*self._billing_street_address1_locator).send_keys(street_address1)
        if postal_code != "":
            self.driver.find_element(*self._billing_postal_code_locator).clear()
            self.driver.find_element(*self._billing_postal_code_locator).send_keys(postal_code)
        return self