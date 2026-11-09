import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    # Matikan popup "Change your password" / password manager Chrome
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })
    # options.add_argument("--headless=new")  # aktifkan untuk CI/tanpa GUI

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
