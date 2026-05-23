from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from locators.main_page_locators import MainPageLocators
from urls import BASE_URL

class MainPage(BasePage):

    def open(self):
        self.driver.get(BASE_URL)

    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

    def go_to_feed(self):
        self.click(MainPageLocators.FEED_LINK)

    def go_to_profile(self):
        self.click(MainPageLocators.PROFILE_LINK)

    def click_first_ingredient(self):
        element = self.find(MainPageLocators.FIRST_INGREDIENT)
        self.driver.execute_script("arguments[0].click();", element)

    def close_ingredient_modal(self):
        element = self.find(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    def ingredient_modal_is_visible(self):
        return self.is_visible(MainPageLocators.INGREDIENT_MODAL_TITLE)

    def ingredient_modal_is_closed(self):
        try:
            self.wait.until_not(
                lambda d: d.find_elements(*MainPageLocators.INGREDIENT_MODAL_OPENED)
            )
            return True
        except Exception:
            return False

    def get_first_ingredient_counter(self):
        elements = self.driver.find_elements(*MainPageLocators.FIRST_INGREDIENT_COUNTER)
        if not elements:
            return 0
        return int(elements[0].text)

    def add_first_ingredient(self):
        ingredient = self.find(MainPageLocators.FIRST_INGREDIENT)
        drop_zone = self.find(MainPageLocators.CONSTRUCTOR_DROP_ZONE)
        self.driver.execute_script("""
            function simulateDragDrop(source, target) {
                const dataTransfer = new DataTransfer();
                source.dispatchEvent(new DragEvent('dragstart', {bubbles: true, dataTransfer}));
                target.dispatchEvent(new DragEvent('dragover', {bubbles: true, dataTransfer}));
                target.dispatchEvent(new DragEvent('drop', {bubbles: true, dataTransfer}));
                source.dispatchEvent(new DragEvent('dragend', {bubbles: true, dataTransfer}));
            }
            simulateDragDrop(arguments[0], arguments[1]);
        """, ingredient, drop_zone)
        if self.ingredient_modal_is_visible():
            self.close_ingredient_modal()

    def click_checkout(self):
        self.click(MainPageLocators.CHECKOUT_BUTTON)

    def get_order_number_from_modal(self):
        # Во время анимации показывается 9999 — ждём реального номера
        wait = WebDriverWait(self.driver, 30)
        wait.until(
            lambda d: d.find_element(
                *MainPageLocators.ORDER_NUMBER_IN_MODAL
            ).text.isdigit()
            and d.find_element(*MainPageLocators.ORDER_NUMBER_IN_MODAL).text != "9999"
        )
        return self.get_text(MainPageLocators.ORDER_NUMBER_IN_MODAL)
