from Api import *


class User:
    params = {
        'page': '1',
        'itemsPerPage': '100'
    }

    def __init__(self, name='nkostin@bytewerk.com', password='ytuflzq123'):
        self.name = name
        self.password = password
        self.cookies = Api.login(self.name, self.password).cookies
        # print(self.cookies)

    def login(self):
        return Api.login(self.name, self.password)

    def get_cookies(self):
        result = Api.login(self.name, self.password).cookies
        return result

    def get_balance(self, currency_name):
        # print(js[12]['name'])
        js = Api.user_account(self.cookies)
        for i in range(len(js)):
            if currency_name in js[i]['name']:
                # print(js[i]['balance'])
                return js[i]['balance']
