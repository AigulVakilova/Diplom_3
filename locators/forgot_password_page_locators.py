from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_HIDE_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon-action')]")
    PASSWORD_INPUT_CONTAINER = (By.XPATH, "//div[contains(@class,'input_status_active')]")
    