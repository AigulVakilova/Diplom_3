# Diplom_3
## Задание 3: UI-тесты

### Автотесты для проверки веб-приложения Stellar Burgers

### Реализованные сценарии

Созданы UI-тесты для проверки основного функционала веб-приложения Stellar Burgers

### Структура проекта

- `tests` — пакет, содержащий тесты, разделённые по классам: `test_constructor.py`, `test_feed.py`, `test_forgot_password.py`, `test_profile.py`
- `pages` — пакет с Page Object классами для каждой страницы
- `locators` — пакет с локаторами элементов страниц
- `helpers.py` — вспомогательные функции
- `conftest.py` — фикстуры
- `browser_factory.py` — фабричный метод для создания драйвера браузера

### Описание реализованных тестов

`TestForgotPassword` — переход на страницу восстановления пароля, ввод email, подсветка поля пароля

`TestProfile` — переход в личный кабинет, история заказов, выход из аккаунта

`TestConstructor` — переход в конструктор и ленту заказов, модальное окно ингредиента, каунтер ингредиента, оформление заказа

`TestFeed` — модальное окно заказа, заказы в ленте, счётчики выполненных заказов, раздел «В работе»

### Запуск автотестов

**Установка зависимостей**

`$ pip install -r requirements.txt`

**Запуск автотестов в Chrome**

`$ pytest --browser=chrome -v --alluredir=allure-results`

**Запуск автотестов в Firefox**

`$ pytest --browser=firefox -v --alluredir=allure-results`

**Просмотр Allure-отчёта**

`$ allure serve allure-results`
