from tests.base import BaseTest
from pages.home import HomePage
from pages.product import ProductPage

class TestHomePage(BaseTest):

    def setup_method(self):
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.home_page.open()
        
        
    def test_home_product_page_is_displayed(self):
        self.home_page.click_random_product()
        assert self.product_page.is_product_present, "Product page should be displayed."
                
    def test_cart_is_opened_when_clicking_buy_product_from_product_page(self):
        self.home_page.click_random_product()
        self.product_page.click_add_to_cart()
        assert self.product_page.is_cart_open == True, "Cart should be open."
        
    def test_product_can_be_added_to_cart_from_product_page(self):
        self.home_page.click_random_product().click_add_to_cart()
        self.product_page.click_close_cart_button()
        assert self.product_page.total_items_in_cart > 0, "Product should be in cart."
        
    