import allure

from api.user_api import LoginUserAPI
from api.order_api import CreateOrderAPI
from data import IngredientData, ResponseMessage as RM, ResponseStatus as RS


class TestCreateOrder:

    @allure.title(
        'Verify that order is created successfully for logged-in user with valid ingredients.')
    @allure.description(
        'Verify that 200 code is returned for POST request for order creation for logged-in user with valid ingredients.')
    def test_create_order_for_logged_user_valid_ingredients_order_created_successfully(self, register_and_delete_user,
                                                                                       generate_user_data):
        token = LoginUserAPI.get_token(generate_user_data['email'], generate_user_data['password'])
        response = CreateOrderAPI.create_order(token, IngredientData.VALID_INGREDIENTS)
        assert response.status_code == RS.OK and response.json()['order']['number'] > 0

    @allure.title(
        'Verify that order is not created for logged-in user with empty ingredient list.')
    @allure.description(
        'Verify that 400 code is returned for POST request for order creation for logged-in user with empty ingredient list.')
    def test_create_order_for_logged_user_empty_ingredients_order_not_created(self, register_and_delete_user,
                                                                              generate_user_data):
        token = LoginUserAPI.get_token(generate_user_data['email'], generate_user_data['password'])
        response = CreateOrderAPI.create_order(token=token)
        assert response.status_code == RS.BAD_REQUEST and response.json()['message'] == RM.EMPTY_INGREDIENT_LIST

    @allure.title(
        'Verify that order is not created for logged-in user with invalid ingredient list.')
    @allure.description(
        'Verify that 500 code is returned for POST request for order creation for logged-in user with invalid ingredient list.')
    def test_create_order_for_logged_user_invalid_ingredients_order_not_created(self, register_and_delete_user,
                                                                                generate_user_data):
        token = LoginUserAPI.get_token(generate_user_data['email'], generate_user_data['password'])
        response = CreateOrderAPI.create_order(token, IngredientData.INVALID_INGREDIENTS)
        assert response.status_code == RS.INTERNAL_SERVER_ERROR

    @allure.title(
        'Verify that order is created successfully for guest user with valid ingredients.')
    @allure.description(
        'Verify that 200 code is returned for POST request for order creation for guest user with valid ingredients.')
    def test_create_order_for_guest_user_valid_ingredients_order_created_successfully(self):
        response = CreateOrderAPI.create_order(ingredients=IngredientData.VALID_INGREDIENTS)
        assert response.status_code == RS.OK and response.json()['order']['number'] > 0

    @allure.title(
        'Verify that order is not created for guest user with empty ingredient list.')
    @allure.description(
        'Verify that 400 code is returned for POST request for order creation for guest user with empty ingredient list.')
    def test_create_order_for_guest_user_empty_ingredients_order_not_created(self):
        response = CreateOrderAPI.create_order()
        assert response.status_code == RS.BAD_REQUEST and response.json()['message'] == RM.EMPTY_INGREDIENT_LIST

    @allure.title(
        'Verify that order is not created for guest user with invalid ingredient list.')
    @allure.description(
        'Verify that 500 code is returned for POST request for order creation for guest user with invalid ingredient list.')
    def test_create_order_for_guest_user_invalid_ingredients_order_not_created(self):
        response = CreateOrderAPI.create_order(ingredients=IngredientData.INVALID_INGREDIENTS)
        assert response.status_code == RS.INTERNAL_SERVER_ERROR
