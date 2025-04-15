import requests
import allure
from urls import Urls


class RegisterUserAPI:
    @staticmethod
    @allure.step('Register new user.')
    def register_user(email: str, password: str, name: str):
        response = requests.post(Urls.REGISTER_USER,
                                 json={"email": email, "password": password, "name": name})
        return response


class LoginUserAPI:
    @staticmethod
    @allure.step('Login user.')
    def login_user(email: str, password: str):
        response = requests.post(Urls.LOGIN_USER, json={"email": email, "password": password})
        return response

    @staticmethod
    @allure.step('Get user token.')
    def get_token(email: str, password: str):
        response = requests.post(Urls.LOGIN_USER, json={"email": email, "password": password})
        token = response.json()['accessToken']
        return token


class DeleteUserAPI:
    @staticmethod
    @allure.step('Delete user.')
    def delete_user(token: str):
        headers = {'Authorization': token}
        response = requests.delete(Urls.DELETE_USER, headers=headers)
        return response


class ChangeUserDataAPI:
    @staticmethod
    @allure.step('Change user data.')
    def change_user_data(token=None, new_user_data=None):
        if token:
            headers = {'Authorization': token}
            response = requests.patch(Urls.CHANGE_USER_DATA, headers=headers, data=new_user_data)
        else:
            response = requests.patch(Urls.CHANGE_USER_DATA, data=new_user_data)
        return response
