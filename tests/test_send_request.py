import json
import pytest
import requests

ENDPOINT_SEND_REQUEST = 'https://send-request.me/'
POST_REQUEST_BODY = {"first_name": "James",
                     "last_name": "Bond"}


@pytest.fixture(scope='module')
def post_users_endpoint():
    users_endpoint_: str = f'{ENDPOINT_SEND_REQUEST}api/users/'
    yield users_endpoint_


# - отправка данных на сторону сервера
@pytest.fixture(scope='module')
def post_user_response(post_users_endpoint):
    post_user_response = requests.post(post_users_endpoint,
                                       data=json.dumps(POST_REQUEST_BODY))
    yield post_user_response


@pytest.fixture(scope='module')
def post_user_response_data(post_user_response):
    post_user_response_data_ = post_user_response.json()
    yield post_user_response_data_


def test_is_request_201(post_user_response):
    assert post_user_response.status_code == 201


def test_is_users_last_name_ok(post_user_response_data):
    assert post_user_response_data['last_name'] == 'Bond'
