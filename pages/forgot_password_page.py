from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from urls import FORGOT_URL

class ForgotPasswordPage(BasePage):

    def open(self):
        self.driver.get(FORGOT_URL)

    def enter_email(self, email):
        self.type(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    def click_restore(self):
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON)

    def click_show_hide_password(self):
        self.click(ForgotPasswordPageLocators.SHOW_HIDE_BUTTON)

    def password_field_is_active(self):
        return self.is_visible(ForgotPasswordPageLocators.PASSWORD_INPUT_CONTAINER)
    