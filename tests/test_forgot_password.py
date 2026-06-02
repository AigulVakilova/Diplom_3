import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from urls import FORGOT_URL, RESET_URL

@allure.feature("Восстановление пароля")
class TestForgotPassword:

    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_forgot_password_page(self, browser):
        login_page = LoginPage(browser)
        with allure.step("Открыть страницу логина"):
            login_page.open()
        with allure.step("Кликнуть 'Восстановить пароль'"):
            login_page.go_to_forgot_password()
        with allure.step("Проверить URL страницы восстановления"):
            assert FORGOT_URL in login_page.get_current_url()

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_enter_email_and_click_restore(self, browser):
        page = ForgotPasswordPage(browser)
        with allure.step("Открыть страницу восстановления пароля"):
            page.open()
        with allure.step("Ввести email и нажать 'Восстановить'"):
            page.enter_email("test@test.com")
            page.click_restore()
        with allure.step("Проверить переход на страницу сброса пароля"):
            page.wait_for_url(RESET_URL)
            assert RESET_URL in page.get_current_url()

    @allure.title("Клик по кнопке показать/скрыть пароль подсвечивает поле")
    def test_show_hide_button_activates_password_field(self, browser):
        page = ForgotPasswordPage(browser)
        with allure.step("Открыть страницу восстановления, ввести email, нажать 'Восстановить'"):
            page.open()
            page.enter_email("test@test.com")
            page.click_restore()
        with allure.step("Нажать кнопку показать/скрыть пароль"):
            page.click_show_hide_password()
        with allure.step("Проверить, что поле пароля подсвечено"):
            assert page.password_field_is_active()
