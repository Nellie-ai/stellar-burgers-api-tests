import allure

from data import (
    INGREDIENTS_REQUIRED_RESPONSE,
    INVALID_INGREDIENT_HASH,
    VALID_INGREDIENTS,
)
from helpers import api_client


class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_authorization(self, registered_user):
        response = api_client.create_order(
            {"ingredients": [VALID_INGREDIENTS[0]]},
            registered_user["token"],
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["success"] is True
        assert response_body["order"]["number"] > 0

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization(self):
        response = api_client.create_order(
            {"ingredients": [VALID_INGREDIENTS[0]]},
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["success"] is True
        assert response_body["order"]["number"] > 0

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, registered_user):
        response = api_client.create_order(
            {"ingredients": VALID_INGREDIENTS},
            registered_user["token"],
        )
        response_body = response.json()

        assert response.status_code == 200
        assert response_body["success"] is True
        assert response_body["order"]["number"] > 0

    @allure.title("Нельзя создать заказ без ингредиентов")
    def test_create_order_without_ingredients(self, registered_user):
        response = api_client.create_order(
            {"ingredients": []},
            registered_user["token"],
        )
        response_body = response.json()

        assert response.status_code == 400
        assert response_body == INGREDIENTS_REQUIRED_RESPONSE

    @allure.title("Нельзя создать заказ с неверным хешем ингредиента")
    def test_create_order_with_invalid_ingredient_hash(self, registered_user):
        response = api_client.create_order(
            {"ingredients": [INVALID_INGREDIENT_HASH]},
            registered_user["token"],
        )

        assert response.status_code == 400
