import pytest
import allure

from api.user_api import RegisterUserAPI, LoginUserAPI
from helper import Helper
from data import UserData, ResponseMessage as RM, ResponseStatus as RS


class TestRegisterUser:

    @allure.title(
        'Verify that user is registered successfully if passing valid email, name and password in the request.')
    @allure.description(
        'Verify that 200 code is returned for POST request for user registration with valid email, password or name.')
    def test_register_user_all_fields_registered_successfully(self, generate_user_data, delete_user):
        response = RegisterUserAPI.register_user(generate_user_data['email'], generate_user_data['password'],
                                                 generate_user_data['name'])
        token = LoginUserAPI.get_token(generate_user_data['email'], generate_user_data['password'])
        delete_user.append(token)
        assert response.status_code == RS.OK and response.json()['success'] == RM.SUCCESSFULL_USER_REGISTRATION

    @allure.title(
        'Verify that user is not registered if trying to create a user with existing email, password or name.')
    @allure.description(
        'Verify that 403 code is returned for POST request for user registration with the existing email, password or name.')
    def test_register_user_existing_user_data_not_registered(self):
        response = RegisterUserAPI.register_user(UserData.EXISTING_USER_EMAIL, UserData.EXISTING_USER_PASSWORD,
                                                 UserData.EXISTING_USER_NAME)
        assert response.status_code == RS.FORBIDDEN and response.json()['message'] == RM.EXISTING_DATA_USER_REGISTRATION

    @allure.title(
        'Verify that user is not registered if any of the the mandatory fields is missed in the request.')
    @allure.description(
        'Verify that 403 code is returned for POST request for user registration if email, password and/or name are missed in the request.')
    @pytest.mark.parametrize(
        'email,password,name',
        [
            ['', Helper.generate_user_password(), ''],
            [Helper.generate_user_email(), '', ''],
            ['', '', Helper.generate_user_name()],
            ['', '', ''],
        ]
    )
    def test_register_user_missed_mandatory_parameter_not_registered(self, email, password, name):
        response = RegisterUserAPI.register_user(email, password, name)
        assert response.status_code == RS.FORBIDDEN and response.json()[
            'message'] == RM.INCOMPLETE_DATA_USER_REGISTRATION
