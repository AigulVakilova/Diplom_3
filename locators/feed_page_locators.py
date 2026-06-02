from selenium.webdriver.common.by import By

class FeedPageLocators:
    FIRST_ORDER = (By.XPATH, "(//a[contains(@class,'OrderHistory_link')])[1]")
    ORDER_MODAL_OPENED = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]")
    ORDER_MODAL_TITLE = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//h2")
    TOTAL_ALL_TIME = (By.XPATH, "(//p[contains(@class,'OrderFeed_number')])[1]")
    TOTAL_TODAY = (By.XPATH, "(//p[contains(@class,'OrderFeed_number')])[2]")
    IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class,'OrderFeed_orderList__cBvyi')]")
    ORDER_FEED_SECTION = (By.XPATH, "//section[contains(@class,'OrderFeed')]")
    