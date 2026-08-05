import allure
import requests

from src.config import BASE_URL, HTTP_TIMEOUT_SECONDS


class StellarBurgersApi:
    def __init__(
        self,
        base_url=BASE_URL,
        timeout=HTTP_TIMEOUT_SECONDS,
        session=None,
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = session or requests.Session()

    def create_user(self, payload):
        with allure.step("Создать пользователя"):
            return self.session.post(
                f"{self.base_url}/api/auth/register",
                json=payload,
                timeout=self.timeout,
            )

    def login_user(self, payload):
        with allure.step("Авторизовать пользователя"):
            return self.session.post(
                f"{self.base_url}/api/auth/login",
                json=payload,
                timeout=self.timeout,
            )

    def create_order(self, payload, token=None):
        with allure.step("Создать заказ"):
            headers = {}

            if token:
                headers["Authorization"] = token

            return self.session.post(
                f"{self.base_url}/api/orders",
                json=payload,
                headers=headers,
                timeout=self.timeout,
            )

    def delete_user(self, token):
        with allure.step("Удалить пользователя"):
            return self.session.delete(
                f"{self.base_url}/api/auth/user",
                headers={"Authorization": token},
                timeout=self.timeout,
            )
