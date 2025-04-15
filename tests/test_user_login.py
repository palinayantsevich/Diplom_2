import pytest
import allure

from api.user_api import LoginUserAPI
from helper import Helper
from data import UserData, ResponseMessage as RM, ResponseStatus as RS


class TestLoginUser:

    @allure.title(
        'Verify that user is logged-in successfully if passing valid email and password in the request.')
    @allure.description(
        'Verify that 200 code is returned for POST request for user logged-in with valid email and password.')
    def test_login_user_valid_data_logged_successfully(self, generate_user_data, register_and_delete_user):
        response = LoginUserAPI.login_user(generate_user_data['email'], generate_user_data['password'])
        assert response.status_code == RS.OK and response.json()['success'] == RM.SUCCESSFULL_USER_LOGIN

    @allure.title(
        'Verify that user is not logged-in if login or password are missed or invalid in the request.')
    @allure.description(
        'Verify that 401 code is returned for POST request for user logged-in with missed or invalid email or password (or both).')
    @pytest.mark.parametrize(
        'email,password',
        [
            ['', UserData.EXISTING_USER_PASSWORD],
            [UserData.EXISTING_USER_EMAIL, ''],
            ['', ''],
            [Helper.generate_user_email(), Helper.generate_user_password()],
            [UserData.EXISTING_USER_EMAIL, Helper.generate_user_password()],
            [Helper.generate_user_email(), UserData.EXISTING_USER_PASSWORD]
        ]
    )
    def test_login_user_missed_or_invalid_parameter_not_logged_in(self, email, password):
        response = LoginUserAPI.login_user(email, password)
        assert response.status_code == RS.UNAUTHORIZED and response.json()[
            'message'] == RM.INCOMPLETE_OR_INVALID_DATA_USER_LOGIN
