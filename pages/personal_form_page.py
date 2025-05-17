import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class PersonalFormPage(BasePage):
    
    NAME_INPUT = "//input[@name='firstName']"
    MIDDLE_NAME_INPUT="//input[@name='middleName']"
    LAST_NAME_INPUT = "//input[@name='lastName']"
    PIM_BUTTON = "//span[contains(@class, 'oxd-text oxd-text--span oxd-main-menu-item--name') and text()='PIM']"
    ADD_BUTTON = "//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--secondary')]//i"
    SAVE_BUTTON = "//button[contains(@class, 'oxd-button--secondary') and contains(@class, 'orangehrm-left-space') and contains(text(), Save)]"
    ERROR_MESSAGE = "//input[@name='firstName']/following::span[contains(@class, 'oxd-input-field-error-message')][1]"
    NAME_SHOWN = "//h6[text()='{}']"
    def enter_name(self, name):
        """
        This method enters the name into the name input field.
        :param name:
        :return:
        """
        self.driver.find_element(By.XPATH, self.NAME_INPUT).send_keys(name)

    def enter_middle_name(self, middle_name):
        """
        This method enters the middle name into the middle name input field.
        :param middle_name:
        :return:
        """
        self.driver.find_element(By.XPATH, self.MIDDLE_NAME_INPUT).send_keys(middle_name)

    def enter_lastname(self, lastname):
        """
        This method enters the lastname into the lastname input field.
        :param lastname:
        :return:
        """
        self.driver.find_element(By.XPATH, self.LAST_NAME_INPUT).send_keys(lastname)

    def submit_form(self):
        """
        This method clicks the save button to submit the form.
        """
        time.sleep(3)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE_BUTTON))
        ).click()

    def select_pim_with_add_employee(self):
        """
        This method clicks the PIM button and then the Add Employee button.
        """
        self.driver.find_element(By.XPATH,self.PIM_BUTTON).click()

    def add_employee(self):
        """
        This method clicks the Add Employee button.
        """
        self.driver.find_element(By.XPATH,self.ADD_BUTTON).click()

    def get_error_message_for_field(self, expected_error):
        """
        This method retrieves the error message for a specific field.
        :param expected_error:
        :return:
        """
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.ERROR_MESSAGE))
            )
            actual_error = error_element.text.strip()
            assert actual_error == expected_error, (
                f"❌ Incorrect error message for the field. "
                f"Expected: '{expected_error}', but got: '{actual_error}'"
            )
        except:
            assert False, f"❌ No error message was displayed for the field. Expected: '{expected_error}'"

    def is_employee_name_displayed(self, expected_name):
        """
        This method checks if the employee name is displayed on the page.
        :param expected_name:
        :return:
        """
        actual_name = self.driver.find_element(By.XPATH, self.NAME_SHOWN.format(expected_name)).text
        return actual_name == expected_name
