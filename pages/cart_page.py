from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page keranjang belanja"""

    CART_ITEM_NAMES = (By.XPATH, "//div[@data-test='inventory-item-name']")
    CART_ITEMS = (By.XPATH, "//div[@data-test='cart-list']//div[@data-test='inventory-item']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_item_names(self) -> list:
        self.find_element(self.CART_ITEM_NAMES)  # explicit wait sampai item muncul
        return [e.text for e in self.driver.find_elements(*self.CART_ITEM_NAMES)]
