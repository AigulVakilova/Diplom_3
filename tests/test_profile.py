import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import PROFILE_URL, ORDER_HISTORY_URL, LOGIN_URL

@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход по клику на 'Личный кабинет'")
    def test_go_to_profile(self, logged_in_browser):
        page = MainPage(logged_in_browser)
        with allure.step("Кликнуть 'Личный кабинет'"):
            page.go_to_profile()
        with allure.step("Проверить URL профиля"):
            page.wait_for_url(PROFILE_URL)
            assert PROFILE_URL in logged_in_browser.current_url

    @allure.title("Переход в раздел 'История заказов'")
    def test_go_to_order_history(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        profile_page = ProfilePage(logged_in_browser)
        with allure.step("Перейти в личный кабинет через клик"):
            main_page.go_to_profile()
        with allure.step("Кликнуть 'История заказов'"):
            profile_page.go_to_order_history()
        with allure.step("Проверить URL"):
            assert ORDER_HISTORY_URL in logged_in_browser.current_url

    @allure.title("Выход из аккаунта")
    def test_logout(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        profile_page = ProfilePage(logged_in_browser)
        with allure.step("Перейти в личный кабинет через клик"):
            main_page.go_to_profile()
        with allure.step("Нажать 'Выход'"):
            profile_page.logout()
        with allure.step("Проверить редирект на логин"):
            profile_page.wait_for_url(LOGIN_URL)
            assert LOGIN_URL in logged_in_browser.current_url
