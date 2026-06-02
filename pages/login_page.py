from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from urls import LOGIN_URL

class LoginPage(BasePage):

    def open(self):
        self.driver.get(LOGIN_URL)
        self.find(LoginPageLocators.EMAIL_INPUT)

    def login(self, email, password):
        self.type(LoginPageLocators.EMAIL_INPUT, email)
        self.type(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def go_to_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)
