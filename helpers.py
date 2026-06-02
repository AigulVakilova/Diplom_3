import random
import string
import requests
from urls import REGISTER_URL, DELETE_USER_URL, INGREDIENTS_URL

def random_string(length=8):
    """Генерирует случайную строку из строчных букв заданной длины."""
    return "".join(random.choices(string.ascii_lowercase, k=length))

def generate_user():
    """Генерирует данные уникального пользователя: email, пароль, имя."""
    return {
        "email": f"{random_string()}@test.com",
        "password": random_string(10),
        "name": random_string(),
    }

def register_user(user):
    """Регистрирует пользователя через API и возвращает ответ сервера."""
    response = requests.post(REGISTER_URL, json=user)
    return response.json()

def delete_user(token):
    """Удаляет пользователя через API по токену авторизации."""
    requests.delete(
        DELETE_USER_URL,
        headers={"Authorization": token},
    )

def get_token(user):
    """Регистрирует пользователя и возвращает accessToken."""
    response = requests.post(REGISTER_URL, json=user)
    return response.json()["accessToken"]

def get_valid_ingredient():
    """Возвращает id первого валидного ингредиента из базы сервера."""
    response = requests.get(INGREDIENTS_URL)
    return response.json()["data"][0]["_id"]
