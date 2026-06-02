from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.feed_page_locators import FeedPageLocators
from urls import FEED_URL

class FeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.long_wait = WebDriverWait(driver, 30)

    def open(self):
        self.driver.get(FEED_URL)

    def click_first_order(self):
        self.click(FeedPageLocators.FIRST_ORDER)

    def order_modal_is_visible(self):
        return self.is_visible(FeedPageLocators.ORDER_MODAL_TITLE)

    def get_total_all_time(self):
        return int(self.get_text(FeedPageLocators.TOTAL_ALL_TIME))

    def get_total_today(self):
        return int(self.get_text(FeedPageLocators.TOTAL_TODAY))
    
    def order_number_in_feed(self, order_number):
        self.long_wait.until(
            EC.text_to_be_present_in_element(FeedPageLocators.ORDER_FEED_SECTION, order_number)
        )
        return True

    def wait_for_order_in_progress(self, order_number):
        # Ждём пока появится номер — сначала отображается текст: "Все текущие заказы готовы"
        self.long_wait.until(
            EC.text_to_be_present_in_element(FeedPageLocators.IN_PROGRESS_SECTION, order_number)
        )
        return True

    def wait_for_counter_increase(self, locator, initial_value):
        WebDriverWait(self.driver, 60).until(
            lambda d: int(d.find_element(*locator).text) > initial_value
        )
        return int(self.get_text(locator))
    