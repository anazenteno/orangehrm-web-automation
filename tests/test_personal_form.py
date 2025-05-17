import pytest
from pages.personal_form_page import PersonalFormPage

@pytest.mark.parametrize("invalid_input, expected_error", [
    ("A" * 31, "Should not exceed 30 characters"),
    ("", "Required"),
    ("Juan123", "The name must not contain numbers."),
    ("@Juan!", "Only letters are allowed."),
])
def test_name_field_rejects_invalid_inputs(logged_in_driver, invalid_input, expected_error):
    """
    This test checks if the name field rejects invalid inputs.
    :param logged_in_driver: object of the driver
    :param invalid_input:
    :param expected_error:
    :return:
    """
    form = PersonalFormPage(logged_in_driver)
    form.select_pim_with_add_employee()
    form.add_employee()
    form.enter_name(invalid_input)
    form.enter_lastname("Golbert")
    form.submit_form()
    form.get_error_message_for_field(expected_error)

@pytest.mark.parametrize("first_name, middle_name,last_name", [("Johny", "Deep", "Golden"),])
def test_employee_creation_(logged_in_driver, first_name, middle_name, last_name):
    """
    This test checks if the employee creation is successful.
    :param logged_in_driver:
    :param first_name:
    :param middle_name:
    :param last_name:
    :return:
    """
    form = PersonalFormPage(logged_in_driver)
    form.select_pim_with_add_employee()
    form.add_employee()
    form.enter_name(first_name)
    form.enter_middle_name(middle_name)
    form.enter_lastname(last_name)
    form.submit_form()
    form.wait_for_url_contains("viewPersonalDetails")
    add_employee_name = form.is_employee_name_displayed(first_name+" "+last_name)
    assert  add_employee_name, (f"Employee name not found. Make sure the creation process completed successfully and "
                                f"that the page redirected to the employee details view.")