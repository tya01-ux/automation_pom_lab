from pages.login_page import LoginPage


class TestLogin:
    def test_login_positive_valid_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = login_page.get_current_url()
        assert actual_url == expected_url, (
            f"Diharapkan '{expected_url}', tetapi berada di '{actual_url}'"
        )
        assert login_page.is_dashboard_displayed() is True, (
            "Logo Swag Labs tidak tampil setelah login valid!"
        )

    def test_login_negative_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        expected_error = "Epic sadface: Sorry, this user has been locked out."
        actual_error = login_page.get_error_message()
        assert expected_error in actual_error, (
            f"Diharapkan: '{expected_error}', Diterima: '{actual_error}'"
        )

    def test_login_negative_empty_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "")

        expected_error = "Epic sadface: Password is required"
        actual_error = login_page.get_error_message()
        assert expected_error in actual_error, (
            f"Diharapkan: '{expected_error}', Diterima: '{actual_error}'"
        )
