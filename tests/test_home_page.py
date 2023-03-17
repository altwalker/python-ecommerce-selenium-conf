from tests.base import BaseTest
from pages.home import HomePage

class TestHomePage(BaseTest):

    def setup_method(self):
        self.home_page = HomePage(self.driver)
        self.home_page.open()
        
    def test_home_page_is_displayed(self):
        assert self.home_page.is_displayed, "Home page should be displayed."
        
    def test_home_page_has_3_products(self):
        assert self.home_page.products_count == 3, "Home page should have 3 products."
        
    def test_cart_is_opened_when_clicking_buy_product_from_home_page(self):
        self.home_page.add_to_cart_random_product()
        assert self.home_page.is_cart_open == True, "Cart should be open."
        
    def test_product_can_be_added_to_cart_from_home_page(self):
        self.home_page.add_to_cart_random_product()
        self.home_page.click_close_cart_button()
        assert self.home_page.total_items_in_cart > 0, "Product should be in cart."
        
    