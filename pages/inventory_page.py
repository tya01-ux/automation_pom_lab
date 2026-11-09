from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Inventory SauceDemo"""

    ADD_BACKPACK_BUTTON = (
        By.XPATH, "//button[contains(@data-test, 'add-to-cart-sauce-labs-backpack')]"
    )
    CART_LINK = (By.XPATH, "//a[@data-test='shopping-cart-link']")
    CART_BADGE = (
        By.XPATH, "//a[@data-test='shopping-cart-link']/span[@data-test='shopping-cart-badge']"
    )
    BURGER_MENU_BUTTON = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def __init__(self, driver):
        super().__init__(driver)

    # --- Add to cart ---
    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BUTTON)

    def add_product_to_cart(self, product_slug: str):
        """Tambah produk mana saja, mis. 'sauce-labs-bike-light', 'sauce-labs-onesie'."""
        locator = (By.XPATH, f"//button[@data-test='add-to-cart-{product_slug}']")
        self.click(locator)

    def get_cart_badge_count(self) -> str:
        return self.get_text(self.CART_BADGE)

    # --- Keranjang ---
    def open_cart(self):
        self.click(self.CART_LINK)

    # --- Logout ---
    def logout(self):
        self.click(self.BURGER_MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
