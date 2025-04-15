class ResponseMessage:
    SUCCESSFULL_USER_REGISTRATION = True
    EXISTING_DATA_USER_REGISTRATION = 'User already exists'
    INCOMPLETE_DATA_USER_REGISTRATION = 'Email, password and name are required fields'
    SUCCESSFULL_USER_LOGIN = True
    INCOMPLETE_OR_INVALID_DATA_USER_LOGIN = 'email or password are incorrect'
    UNSUCCESSFUL_GUEST_USER_DATA_CHANGE = 'You should be authorised'
    EMPTY_INGREDIENT_LIST = 'Ingredient ids must be provided'
    UNSUCCESSFUL_GUEST_USER_GET_ORDERS = 'You should be authorised'


class ResponseStatus:
    OK = 200
    FORBIDDEN = 403
    UNAUTHORIZED = 401
    BAD_REQUEST = 400
    INTERNAL_SERVER_ERROR = 500


class UserData:
    EXISTING_USER_NAME = 'Test_name'
    EXISTING_USER_EMAIL = 'palina_yantsevich_18_987@gmail.com'
    EXISTING_USER_PASSWORD = '123456'


class IngredientData:
    VALID_INGREDIENTS = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa70', '61c0c5a71d1f82001bdaaa6e',
                         '61c0c5a71d1f82001bdaaa6c']
    INVALID_INGREDIENTS = ['0', '1']
