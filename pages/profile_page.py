from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):

    def go_to_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)

    def logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

    def get_order_numbers_from_history(self):
        items = self.driver.find_elements(
            *ProfilePageLocators.ORDER_HISTORY_ITEM_NUMBER
        )
        return [item.text for item in items]
