import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage

@pytest.fixture()
def driver():
    """
    This fixture sets up the Chrome WebDriver for the tests.
    :return:
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def logged_in_driver():
    """
    This fixture logs in to the application using the provided credentials.
    :param driver:
    :return:
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.implicitly_wait(5)
    login = LoginPage(driver)
    login.enter_username("admin")
    login.enter_password("admin123")
    login.click_login()
    login.wait_for_url_contains("dashboard")
    yield driver
    driver.quit()