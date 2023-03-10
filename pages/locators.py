from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK_NAME_FIRST = (By.TAG_NAME, "h1")
    BOOK_NAME_ADD = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    BASKET_VAL = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")




