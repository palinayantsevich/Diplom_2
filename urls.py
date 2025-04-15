class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/api/'

    REGISTER_USER = f'{MAIN_URL}auth/register'
    LOGIN_USER = f'{MAIN_URL}auth/login'
    DELETE_USER = f'{MAIN_URL}auth/user'
    CHANGE_USER_DATA = f'{MAIN_URL}auth/user'

    CREATE_ORDER = f'{MAIN_URL}orders'
    GET_ORDERS = f'{MAIN_URL}orders'
