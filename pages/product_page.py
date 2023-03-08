from .base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_show_message(self):
        add_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        assert add_message.text == "The shellcoder's handbook", "Product not found"

    def should_show_basket_value(self):
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VAL)
        assert basket_value.text == "£9.99", "Basket value not found"
