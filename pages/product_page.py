from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_show_message(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_FIRST)
        add_message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADD)
        assert add_message.text == book_name.text , "Product not found"

    def should_show_basket_value(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        basket_value = self.browser.find_element(*ProductPageLocators.BASKET_VAL)
        assert basket_value.text == book_price.text, "Basket value not found"

