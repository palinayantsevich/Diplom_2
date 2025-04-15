import pytest
import allure

from api.user_api import RegisterUserAPI, LoginUserAPI, DeleteUserAPI
from helper import Helper


@pytest.fixture(scope='function')
def generate_user_data():
    email = Helper.generate_user_email()
    password = Helper.generate_user_password()
    name = Helper.generate_user_name()

    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    return payload


@pytest.fixture(scope='function')
def register_and_delete_user(generate_user_data):
    with allure.step('Register new user.'):
        register_user = RegisterUserAPI.register_user(generate_user_data['email'], generate_user_data['password'],
                                                      generate_user_data['name'])
    token = LoginUserAPI.get_token(generate_user_data['email'], generate_user_data['password'])
    yield register_user
    with allure.step('Delete user.'):
        DeleteUserAPI.delete_user(token)


@pytest.fixture(scope='function')
def delete_user():
    token = []
    yield token
    with allure.step('Delete user.'):
        DeleteUserAPI.delete_user(*token)
