import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from locators.feed_page_locators import FeedPageLocators
from urls import PROFILE_URL, ORDER_HISTORY_URL


@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("Клик на заказ открывает модальное окно с деталями")
    def test_click_order_opens_modal(self, browser):
        feed_page = FeedPage(browser)
        with allure.step("Открыть ленту заказов"):
            feed_page.open()
        with allure.step("Кликнуть на первый заказ"):
            feed_page.click_first_order()
        with allure.step("Проверить, что модальное окно с деталями открылось"):
            assert feed_page.order_modal_is_visible()

    @allure.title("Заказы из истории пользователя отображаются в ленте заказов")
    def test_user_orders_appear_in_feed(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        feed_page = FeedPage(logged_in_browser)
        profile_page = ProfilePage(logged_in_browser)

        with allure.step("Создать заказ"):
            main_page.open()
            main_page.add_first_ingredient()
            main_page.click_checkout()
            main_page.get_order_number_from_modal()
            main_page.close_ingredient_modal()

        with allure.step("Перейти в историю заказов через UI"):
            main_page.go_to_profile()
            profile_page.wait_for_url(PROFILE_URL)
            profile_page.go_to_order_history()
            profile_page.wait_for_url(ORDER_HISTORY_URL)
            history_orders = profile_page.get_order_numbers_from_history()

        with allure.step(
            "Открыть ленту заказов и проверить наличие заказов из истории"
        ):
            feed_page.open()
            for order in history_orders:
                assert feed_page.order_number_in_feed(order)

    @allure.title("При создании заказа счётчик 'Выполнено за всё время' увеличивается")
    def test_total_all_time_counter_increases(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        feed_page = FeedPage(logged_in_browser)

        with allure.step("Запомнить счётчик 'Выполнено за всё время'"):
            feed_page.open()
            counter_before = feed_page.get_total_all_time()

        with allure.step("Создать новый заказ"):
            main_page.open()
            main_page.add_first_ingredient()
            main_page.click_checkout()
            main_page.get_order_number_from_modal()
            main_page.close_ingredient_modal()

        with allure.step("Проверить, что счётчик увеличился"):
            feed_page.open()
            feed_page.find(FeedPageLocators.TOTAL_ALL_TIME)
            counter_after = feed_page.wait_for_counter_increase(
                FeedPageLocators.TOTAL_ALL_TIME, counter_before
            )
            assert counter_after > counter_before

    @allure.title("При создании заказа счётчик 'Выполнено за сегодня' увеличивается")
    def test_total_today_counter_increases(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        feed_page = FeedPage(logged_in_browser)

        with allure.step("Запомнить счётчик 'Выполнено за сегодня'"):
            feed_page.open()
            counter_before = feed_page.get_total_today()

        with allure.step("Создать новый заказ"):
            main_page.open()
            main_page.add_first_ingredient()
            main_page.click_checkout()
            main_page.get_order_number_from_modal()
            main_page.close_ingredient_modal()

        with allure.step("Проверить, что счётчик увеличился"):
            feed_page.open()
            feed_page.find(FeedPageLocators.TOTAL_TODAY)
            counter_after = feed_page.wait_for_counter_increase(
                FeedPageLocators.TOTAL_TODAY, counter_before
            )
            assert counter_after > counter_before

    @allure.title("После оформления заказа его номер появляется в разделе 'В работе'")
    def test_new_order_appears_in_progress(self, logged_in_browser):
        main_page = MainPage(logged_in_browser)
        feed_page = FeedPage(logged_in_browser)

        with allure.step("Создать заказ и получить его номер"):
            main_page.open()
            main_page.add_first_ingredient()
            main_page.click_checkout()
            order_number = main_page.get_order_number_from_modal()
            main_page.close_ingredient_modal()

        with allure.step("Открыть ленту заказов"):
            feed_page.open()
            # Ждём загрузки ленты
            feed_page.find(FeedPageLocators.FIRST_ORDER)

        with allure.step("Проверить, что номер заказа есть в разделе 'В работе'"):
            assert feed_page.wait_for_order_in_progress(order_number)
