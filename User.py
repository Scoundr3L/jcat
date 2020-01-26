from Api import *


class User:
    params = {
        'page': '1',
        'itemsPerPage': '100'
    }

    def __init__(self, name='nkostin@bytewerk.com', password='ytuflzq123'):
        self.name = name
        self.password = password

    def login(self):
        return Api.login(self.name, self.password)

    def get_cookies(self):
        return Api.login(self.name, self.password).cookies

    def get_balance(self):
        pass
