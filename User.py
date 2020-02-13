from Api import *


class User:
    params = {
        'page': '1',
        'itemsPerPage': '100'
    }

    def __init__(self, name='nkostin@bytewerk.com', password='ytuflzq123'):
        self.name = name
        self.password = password
        self.user_info = Api.login(self.name, self.password)
        self.cookies = self.user_info.cookies
        # print(self.cookies)

    def login(self):
        return self.user_info

    def get_cookies(self):
        result = self.user_info.cookies
        return result

    def get_balance(self, currency_name):
        # print(js[12]['name'])
        js = Api.user_account(self.cookies)
        for i in range(len(js)):
            if currency_name in js[i]['name']:
                # print(js[i]['balance'])
                return js[i]['balance']
