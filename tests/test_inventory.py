import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def inventory_page(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_dashboard_displayed() is True
    return InventoryPage(driver)


class TestInventory:
    def test_add_to_cart_flow(self, inventory_page):
        """Kasus Uji 1: Add Backpack -> badge '1'."""
        inventory_page.add_backpack_to_cart()
        badge = inventory_page.get_cart_badge_count()
        assert badge == "1", f"Badge diharapkan '1', tetapi '{badge}'"

    def test_logout_flow(self, driver, inventory_page):
        """Kasus Uji 2: Logout -> URL login & tombol login tampil."""
        inventory_page.logout()
        login_page = LoginPage(driver)
        assert login_page.get_current_url() == "https://www.saucedemo.com/"
        assert login_page.is_login_button_displayed() is True

    # --- Tambahan ---
    def test_add_multiple_items_and_open_cart(self, driver, inventory_page):
        """Tambah 2 produk -> badge '2' -> buka keranjang -> kedua produk ada."""
        inventory_page.add_backpack_to_cart()
        inventory_page.add_product_to_cart("sauce-labs-bike-light")
        assert inventory_page.get_cart_badge_count() == "2"

        inventory_page.open_cart()
        assert driver.current_url == "https://www.saucedemo.com/cart.html"
        names = CartPage(driver).get_item_names()
        assert "Sauce Labs Backpack" in names
        assert "Sauce Labs Bike Light" in names

    def test_logout_after_add_to_cart(self, driver, inventory_page):
        """Add Backpack lalu logout -> kembali ke halaman login."""
        inventory_page.add_backpack_to_cart()
        inventory_page.logout()
        login_page = LoginPage(driver)
        assert login_page.get_current_url() == "https://www.saucedemo.com/"
        assert login_page.is_login_button_displayed() is True
