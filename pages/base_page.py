import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_url_contains(self, text, timeout=20):
        """
        Waits for the URL to contain a specific text.
        :param text:
        :param timeout:
        :return:
        """
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def wait_for_element_visible(self, locator, timeout=10):
        """
        Waits for an element to be visible on the page.
        :param locator:
        :param timeout:
        :return:
        """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))