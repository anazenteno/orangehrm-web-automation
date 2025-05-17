from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    username_input = "username"
    password_input = "password"
    button_login = "//button[contains(@class,'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button') and contains(@type,'submit')]"

    def enter_username(self, username):
        """
        this method enters the username into the username input field.
        :param username:
        :return:
        """
        self.driver.find_element(By.NAME, self.username_input).send_keys(username)

    def enter_password(self, password):
        """
        This method enters the password into the password input field.
        :param password:
        :return:
        """
        self.driver.find_element(By.NAME, self.password_input).send_keys(password)

    def click_login(self):
        """
        this method clicks the login button.
        :return:
        """
        self.driver.find_element(By.XPATH, self.button_login).click()