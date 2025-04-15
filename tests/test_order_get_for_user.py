import allure

from api.user_api import LoginUserAPI
from api.order_api import CreateOrderAPI, GetOrderAPI
from data import IngredientData, ResponseMessage as RM, ResponseStatus as RS


class TestGetOrders:

    @allure.title(
        'Verify that list of orders is returned for logged-in user.')
    @allure.description(
        'Verify that 200 code is returned for GET request for logged-in user.')
    def test_get_orders_for_logged_user_orders_returned_successfully(self, register_and_delete_user,
                                                                     generate_user_data):
        token = LoginUserAPI.get_token(generate_user_data['email'], generate_user_data['password'])
        order_number = CreateOrderAPI.create_order(token, IngredientData.VALID_INGREDIENTS).json()['order']['_id']
        response = GetOrderAPI.get_orders_for_user(token)
        assert response.status_code == RS.OK and response.json()['orders'][0]['_id'] == order_number

    @allure.title(
        'Verify that list of orders is not returned for guest user.')
    @allure.description(
        'Verify that 401 code is returned for GET request for guest user.')
    def test_get_orders_for_guest_user_orders_not_returned(self):
        response = GetOrderAPI.get_orders_for_user()
        assert response.status_code == RS.UNAUTHORIZED and response.json()[
            'message'] == RM.UNSUCCESSFUL_GUEST_USER_GET_ORDERS
