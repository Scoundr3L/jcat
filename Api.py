import requests


class Api:
    BASE_URL = 'https://beta.jetcrypto.com'
    PARAMS = dict(page='1', itemsPerPage='100')

    @staticmethod
    def login(login, password):
        auth = {
            "login": login,
            "password": password,
            "recaptcha": "string"
        }
        request = requests.post(Api.BASE_URL + '/api/User/login', json=auth)
        return request

    @staticmethod
    def ping():
        return requests.get(Api.BASE_URL + '/api/Ping')

    @staticmethod
    def user_account(cookies, params=PARAMS):
        request = requests.get(Api.BASE_URL + '/api/UserAccount', params=params, cookies=cookies)
        js = request.json()
        # print(js)
        return js

    @staticmethod
    def market_orders(currency_from, currency_to):
        request = requests.get(Api.BASE_URL + '/api/Trading/MarketOrders?tradingPair=' + currency_from + ',' + currency_to)
        print(request.json())
