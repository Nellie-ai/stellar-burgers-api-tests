import allure

from data import INVALID_CREDENTIALS_RESPONSE
from helpers import api_client, build_invalid_password, build_login_payload


class TestLoginUser:
    @allure.title("Авторизация существующего пользователя")
    def test_login_user_success(self, registered_user):
        response = api_client.login_user(
            build_login_payload(registered_user["payload"]),
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["success"] is True
        assert response_body["accessToken"].startswith("Bearer ")
        assert response_body["user"]["email"] == registered_user["payload"]["email"]

    @allure.title("Нельзя авторизоваться с неверными учётными данными")
    def test_login_user_with_invalid_credentials(self, registered_user):
        invalid_credentials = build_login_payload(registered_user["payload"])
        invalid_credentials["password"] = build_invalid_password()
        response = api_client.login_user(invalid_credentials)
        response_body = response.json()

        assert response.status_code == 401
        assert response_body == INVALID_CREDENTIALS_RESPONSE
