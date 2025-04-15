import random
import string


class Helper:
    @staticmethod
    def generate_user_email():
        length = 6
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        email_for_registration = 'palina_yant_18_' + random_part + '@' + 'test.com'
        return email_for_registration

    @staticmethod
    def generate_user_password():
        length = 6
        password_for_registration = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return password_for_registration

    @staticmethod
    def generate_user_name():
        length = 4
        name_for_registration = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return name_for_registration
