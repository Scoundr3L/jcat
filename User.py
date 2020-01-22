import requests
from Api import *


class User:
    params = {
        'page': '1',
        'itemsPerPage': '100'
    }

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def get_cookies(self):
        return Api.login().cookies

    def get_balance(self):
        pass
