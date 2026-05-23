from selenium.webdriver.common.by import By

class ProfilePageLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(@class,'Account_button')]")
    ORDER_HISTORY_ITEM_NUMBER = (By.XPATH, "//p[contains(@class,'text_type_digits-default')]")
    