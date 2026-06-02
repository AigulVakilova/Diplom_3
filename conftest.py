import pytest
from browser_factory import WebdriverFactory
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_user, register_user, delete_user
from pages.login_page import LoginPage
from urls import BASE_URL, LOGIN_URL

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests: chrome or firefox",
    )

@pytest.fixture
def browser(request):
    """Запускает браузер согласно параметру --browser, после теста закрывает его."""
    browser_name = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def user():
    """Регистрирует пользователя через API, после теста удаляет его."""
    data = generate_user()
    response = register_user(data)
    assert response["success"] is True, f"Регистрация не прошла: {response}"
    token = response["accessToken"]
    yield data
    delete_user(token)

@pytest.fixture
def logged_in_browser(browser, user):
    """Открывает браузер и выполняет вход под зарегистрированным пользователем."""
    login_page = LoginPage(browser)
    login_page.open()
    login_page.login(user["email"], user["password"])
    WebDriverWait(browser, 15).until(
        EC.url_changes(LOGIN_URL)
    )
    return browser
