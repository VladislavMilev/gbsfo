from random import choice
import pytest
import requests


# TODO: -----------------------------------------------------------
#       3.1 Написать тест который будет отправлять POST запрос на "URL/api/auth/login"
#       в зависимости от того какой статус код вернется решать тест прошел или нет.
#       POST, application / json
#       login = any
#       password = any --------------------------------------------


URL = 'http://api.zippopotam.us/us/90210'

user_agents = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
]


def headers():
    return {
        'User-Agent': choice(user_agents),
        'accept-language': 'ru-RU',
        'accept': 'application/json',
    }


user_data = [
    ("random_login", "random_password"),
    ("any", "any")
]


@pytest.mark.parametrize('login, password', user_data)
def test_check_status_code_equals_405(login, password):
    data = {
        'login': login,
        'password': password
    }

    response = requests.post(url=URL, json=data, headers=headers())
    assert response.status_code == 405
