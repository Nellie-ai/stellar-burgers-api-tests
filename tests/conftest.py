import pytest

from helpers import (
    create_registered_user,
    delete_user_by_payload,
    delete_user_by_token,
)


@pytest.fixture
def registered_user():
    user = create_registered_user()

    yield user
    delete_user_by_token(user["token"])


@pytest.fixture
def users_to_delete():
    user_payloads = []

    yield user_payloads

    for user_payload in user_payloads:
        delete_user_by_payload(user_payload)
