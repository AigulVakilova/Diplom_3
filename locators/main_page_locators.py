from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//a[@href='/']//p[text()='Конструктор']")
    FEED_LINK = (By.XPATH, "//a[@href='/feed']//p[text()='Лента Заказов']")
    PROFILE_LINK = (By.XPATH, "//a[@href='/account']//p[text()='Личный Кабинет']")
    FIRST_INGREDIENT = (By.XPATH, "(//a[contains(@class,'BurgerIngredient_ingredient')])[1]")
    FIRST_INGREDIENT_COUNTER = (By.XPATH, "(//a[contains(@class,'BurgerIngredient_ingredient')])[1]//div[contains(@class,'counter_counter')]")
    CONSTRUCTOR_DROP_ZONE = (By.XPATH, "//span[contains(@class,'BurgerConstructor_basket__listContainer')]")
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class,'Modal_modal__close')]")
    INGREDIENT_MODAL_OPENED = (By.XPATH, "//section[contains(@class,'Modal_modal_opened')]")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//h2[contains(@class,'Modal_modal__title') and contains(@class,'digits')]")
