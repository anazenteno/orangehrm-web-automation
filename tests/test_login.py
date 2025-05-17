from pages.login_page import LoginPage

def test_login_success(driver):
    """
    This test checks if the login is successful.
    :param driver:
    """
    login = LoginPage(driver)
    login.enter_username("admin")
    login.enter_password("admin123")
    login.click_login()
    login.wait_for_url_contains("dashboard")
    assert "dashboard" in driver.current_url, f"Login did not redirect to the dashboard."
