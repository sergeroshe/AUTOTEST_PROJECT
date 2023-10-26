import json
import pytest
import requests

ENDPOINT_SEND_REQUEST = 'https://send-request.me/'
POST_REQUEST_USERS_BODY = {"first_name": "James",
                           "last_name": "Bond"}
POST_REQUEST_BODY_AUTH = {
    "login": "string",
    "password": "qwerty12345",
    "timeout": 360
}


@pytest.fixture(scope='module')
def post_user_response_data(post_user_response):
    post_user_response_data_ = post_user_response.json()
    return post_user_response_data_


@pytest.fixture(scope='module')
def post_user_response():
    post_user_response = requests.post(f'{ENDPOINT_SEND_REQUEST}api/users',
                                       data=json.dumps(POST_REQUEST_USERS_BODY))
    return post_user_response


@pytest.fixture(scope='module')
def post_auth_response():
    post_auth_response_ = requests.post(f'{ENDPOINT_SEND_REQUEST}api/auth/authorize',
                                        data=json.dumps(POST_REQUEST_BODY_AUTH))
    return post_auth_response_


@pytest.fixture(scope='function')
def company_localization():
    headers = {"Accept-Language": 'EN'}
    company_localization_info = requests.get(f'{ENDPOINT_SEND_REQUEST}api/companies/1',
                                             headers=headers).json()
    return company_localization_info


# checks that data has been sent successfully
def test_is_post_request_201(post_user_response):
    assert post_user_response.status_code == 201


# checks that user's last name is the same as in the data submitted
def test_is_users_last_name_ok(post_user_response_data):
    assert post_user_response_data['last_name'] == 'Bond'


# checks that submitted password is correct ("qwerty12345")
def test_authorization(post_auth_response):
    assert post_auth_response.status_code == 200


# checks that company info supports English
def test_company_localization(company_localization):
    assert 'description' in company_localization

