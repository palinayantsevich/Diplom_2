import requests
import allure
from urls import Urls


class CreateOrderAPI:
    @staticmethod
    @allure.step('Create new order.')
    def create_order(token=None, ingredients=None):
        ingredient_data = {}
        if ingredients:
            ingredient_data = {'ingredients': ingredients}
        if token:
            headers = {'Authorization': token}
            response = requests.post(Urls.CREATE_ORDER, headers=headers, data=ingredient_data)
        else:
            response = requests.post(Urls.CREATE_ORDER, data=ingredient_data)
        return response


class GetOrderAPI:
    @staticmethod
    @allure.step('Get orders for user.')
    def get_orders_for_user(token=None):
        if token:
            headers = {'Authorization': token}
            response = requests.get(Urls.GET_ORDERS, headers=headers)
        else:
            response = requests.get(Urls.GET_ORDERS)
        return response
