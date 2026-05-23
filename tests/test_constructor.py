import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from urls import BASE_URL, FEED_URL

@allure.feature("Основной функционал")
class TestConstructor:

    @allure.title("Переход по клику на 'Конструктор'")
    def test_go_to_constructor(self, browser):
        feed_page = FeedPage(browser)
        main_page = MainPage(browser)
        with allure.step("Перейти в ленту заказов"):
            feed_page.open()
        with allure.step("Кликнуть 'Конструктор'"):
            main_page.go_to_constructor()
        with allure.step("Проверить URL главной страницы"):
            assert BASE_URL in browser.current_url

    @allure.title("Переход по клику на 'Лента заказов'")
    def test_go_to_feed(self, browser):
        main_page = MainPage(browser)
        with allure.step("Открыть главную страницу"):
            main_page.open()
        with allure.step("Кликнуть 'Лента заказов'"):
            main_page.go_to_feed()
        with allure.step("Проверить URL ленты заказов"):
            assert browser.current_url == FEED_URL

    @allure.title("Клик на ингредиент открывает модальное окно с деталями")
    def test_click_ingredient_opens_modal(self, browser):
        main_page = MainPage(browser)
        with allure.step("Открыть главную страницу"):
            main_page.open()
        with allure.step("Кликнуть на первый ингредиент"):
            main_page.click_first_ingredient()
        with allure.step("Проверить, что модальное окно с деталями видно"):
            assert main_page.ingredient_modal_is_visible()

    @allure.title("Модальное окно ингредиента закрывается кликом по крестику")
    def test_close_ingredient_modal(self, browser):
        main_page = MainPage(browser)
        with allure.step("Открыть главную страницу и кликнуть на ингредиент"):
            main_page.open()
            main_page.click_first_ingredient()
        with allure.step("Кликнуть крестик закрытия"):
            main_page.close_ingredient_modal()
        with allure.step("Проверить, что модальное окно закрыто"):
            assert main_page.ingredient_modal_is_closed()

    @allure.title("Добавление ингредиента увеличивает каунтер")
    def test_add_ingredient_increases_counter(self, browser):
        main_page = MainPage(browser)
        with allure.step("Открыть главную страницу"):
            main_page.open()
        with allure.step("Запомнить начальное значение каунтера"):
            counter_before = main_page.get_first_ingredient_counter()
        with allure.step("Добавить ингредиент в заказ"):
            main_page.add_first_ingredient()
        with allure.step("Проверить, что каунтер увеличился"):
            counter_after = main_page.get_first_ingredient_counter()
            assert counter_after > counter_before

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_place_order(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        with allure.step("Открыть главную страницу и добавить ингредиент"):
            main_page.open()
            main_page.add_first_ingredient()
        with allure.step("Нажать 'Оформить заказ'"):
            main_page.click_checkout()
        with allure.step("Проверить, что появилось модальное окно с номером заказа"):
            assert main_page.get_order_number_from_modal()
