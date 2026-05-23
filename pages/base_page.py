from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].click();", element)
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def current_url(self):
        return self.driver.current_url

    def wait_for_url(self, url):
        self.wait.until(EC.url_contains(url))
