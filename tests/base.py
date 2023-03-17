import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.base import BasePage
from pages.home import HomePage
from pages.cart import CartPage
from pages.product import ProductPage


HEADLESS = False

class BaseTest:
    """Contains common methods for all models."""
    driver: webdriver.Firefox

    @classmethod
    def setup_class(cls):
        """Setup the webdriver."""
        options = Options()
        if HEADLESS:
            options.add_argument('-headless')

        print("Create a new Firefox session")
        cls.driver = webdriver.Firefox(options=options)

        print("Set implicitly wait")
        cls.driver.implicitly_wait(15)
        print("Window size: {width}x{height}".format(**cls.driver.get_window_size()))

    @classmethod
    def teardown_class(cls):
        """Close the webdriver."""
        
        print("Close the Firefox session")
        cls.driver.quit()

  