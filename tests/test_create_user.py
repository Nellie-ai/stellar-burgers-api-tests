import allure
import pytest

from data import (
    REQUIRED_FIELDS_RESPONSE,
    REQUIRED_USER_FIELDS,
    USER_ALREADY_EXISTS_RESPONSE,
)
from helpers import api_client, build_user_payload


class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    def test_create_user_success(self, users_to_delete):
        user_payload = build_user_payload()
        users_to_delete.append(user_payload)
        response = api_client.create_user(user_payload)
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["success"] is True
        assert response_body["user"]["email"] == user_payload["email"]
        assert response_body["user"]["name"] == user_payload["name"]
        assert response_body["accessToken"].startswith("Bearer ")

    @allure.title("Нельзя создать двух пользователей с одинаковыми данными")
    def test_create_user_with_existing_email(self, registered_user):
        response = api_client.create_user(registered_user["payload"])
        response_body = response.json()

        assert response.status_code == 403
        assert response_body == USER_ALREADY_EXISTS_RESPONSE

    @allure.title("Нельзя создать пользователя без поля {missing_field}")
    @pytest.mark.parametrize("missing_field", REQUIRED_USER_FIELDS)
    def test_create_user_without_required_field(self, missing_field):
        incomplete_payload = build_user_payload()
        incomplete_payload.pop(missing_field)
        response = api_client.create_user(incomplete_payload)
        response_body = response.json()

        assert response.status_code == 403
        assert response_body == REQUIRED_FIELDS_RESPONSE
