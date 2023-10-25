import requests
import pytest
import re

ENDPOINT = 'https://randomuser.me/api/'


@pytest.fixture(scope='module')
def user_data():
    response = requests.get(ENDPOINT)
    data = response.json()
    user_data_ = data['results'][0]
    yield user_data_


@pytest.fixture(scope='module')
def results():
    response = requests.get(ENDPOINT)
    data = response.json()
    results_ = data['results']
    yield results_


#  1) Проверка что количество результатов == 1
def test_results_amount(results):
    expected_result_amount = 1
    result_amount = len(results)
    assert result_amount == 1, (
        result_amount, expected_result_amount,
        f'Results amount is not {expected_result_amount}')
    print(f' Results amount is {result_amount}.')


#  2) Проверка что gender может быть только (male, female)
def test_is_gender_valid(user_data):
    expected_gender_list = ['male', 'female']
    gender = user_data['gender']
    assert gender in expected_gender_list, 'Unexpected gender!'
    print(f' Gender is {gender}.')


#  3) Проверить корректность email по шаблону (<some letters>@<sub domain>.<valid domain>)
def test_is_email_correct(user_data):
    valid_email_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    email = user_data['email']
    assert re.fullmatch(valid_email_pattern, email), f' The e-mail address "{email}" is not valid!'
    print(f' The e-mail address "{email}" is valid.')


#  4) Проверить что location/postcode является целым числом
def test_is_postcode_int(user_data):
    postcode = user_data['location']['postcode']
    assert postcode, isinstance(postcode, int)
    f' The postcode "{postcode}" is not an integer value!'
    print(f' The location postcode: {postcode} is an integer value.')


#  5) Проверить что dob/age < 120
def test_is_age_valid(user_data):
    expected_age_limit = 120
    age = user_data['dob']['age']
    assert age < expected_age_limit, 'Age limit of 120 yrs. exceeded!'
    print(f' Age is: {age}.')


#  6) Проверить что name словарь содержит ключи title, first, last и что у них есть значения
def test_is_dict_contains_keys(user_data):
    expected_key_list = ['title', 'first', 'last']
    name_dict = user_data['name']
    for key in expected_key_list:
        assert key in name_dict, f'The data container "name" does not contain expected key: "{key}"!'
        assert name_dict.get(key, 0) != 0, f' The key: {key} of "name" does not contain any value!'

    print(f' The given data contains all expected keys and all of them have values.')

