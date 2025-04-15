import allure

from api.user_api import ChangeUserDataAPI, LoginUserAPI
from helper import Helper
from data import ResponseMessage as RM, ResponseStatus as RS


class TestChangeUserData:

    @allure.title(
        'Verify that logged-in user can change email and name.')
    @allure.description(
        'Verify that 200 code is returned for PATCH request for logged-in user when changing email and name.')
    def test_change_user_data_with_auth_user_data_changes_successfully(self, generate_user_data,
                                                                       register_and_delete_user):
        new_user_data = {'email': Helper.generate_user_email(), 'name': Helper.generate_user_name()}
        token = LoginUserAPI.get_token(generate_user_data['email'], generate_user_data['password'])
        response = ChangeUserDataAPI.change_user_data(token, new_user_data)
        assert response.status_code == RS.OK and response.json()['user'] == new_user_data

    @allure.title(
        'Verify that guest user unable to change email and name.')
    @allure.description(
        'Verify that 401 code is returned for PATCH request for guest user when changing email and name.')
    def test_change_user_data_wo_auth_user_error_returned(self):
        new_user_data = {'email': Helper.generate_user_email(), 'name': Helper.generate_user_name()}
        response = ChangeUserDataAPI.change_user_data(new_user_data=new_user_data)
        assert response.status_code == RS.UNAUTHORIZED and response.json()[
            'message'] == RM.UNSUCCESSFUL_GUEST_USER_DATA_CHANGE
