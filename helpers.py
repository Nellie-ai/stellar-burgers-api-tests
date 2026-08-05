from uuid import uuid4

import allure

from data import USER_NAME
from src.api import StellarBurgersApi


api_client = StellarBurgersApi()


@allure.step("Сгенерировать данные пользователя")
def build_user_payload():
    unique_part = uuid4().hex
    return {
        "email": f"portfolio_{unique_part}@example.com",
        "password": f"Test-{uuid4().hex}-A1!",
        "name": USER_NAME,
    }


@allure.step("Сгенерировать неверный пароль")
def build_invalid_password():
    return f"Invalid-{uuid4().hex}-A1!"


def build_login_payload(user_payload):
    with allure.step("Подготовить данные для авторизации"):
        return {
            "email": user_payload["email"],
            "password": user_payload["password"],
        }


@allure.step("Создать зарегистрированного пользователя для предусловия")
def create_registered_user():
    user_payload = build_user_payload()
    response = api_client.create_user(user_payload)
    response.raise_for_status()

    return {
        "payload": user_payload,
        "token": response.json()["accessToken"],
    }


@allure.step("Удалить созданного пользователя по сохранённому токену")
def delete_user_by_token(token):
    response = api_client.delete_user(token)
    response.raise_for_status()


def delete_user_by_payload(user_payload):
    with allure.step("Удалить созданного пользователя по его данным"):
        login_response = api_client.login_user(build_login_payload(user_payload))

        if login_response.status_code in (401, 403):
            return

        login_response.raise_for_status()
        delete_response = api_client.delete_user(login_response.json()["accessToken"])
        delete_response.raise_for_status()
