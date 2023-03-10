import pytest
from pages.product_page import ProductPage
import time
import pytest

base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{base_link}/?promo=offer{num}" for num in range(10)]

@pytest.mark.xfail(num="bugged_link")
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()
    browser.get(link)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.should_show_message()
    page.should_show_basket_value()

