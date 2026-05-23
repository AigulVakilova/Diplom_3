import random
import string
import requests
from urls import API_URL

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
    response = requests.post(f"{API_URL}/auth/register", json=user)
    return response.json()

def delete_user(token):
    """Удаляет пользователя через API по токену авторизации."""
    requests.delete(
        f"{API_URL}/auth/user",
        headers={"Authorization": token},
    )
