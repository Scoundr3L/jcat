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
        return requests.post(Api.BASE_URL + '/api/User/login', json=auth)

    @staticmethod
    def ping():
        return requests.get(Api.BASE_URL + '/api/Ping')

    @staticmethod
    def user_account(cookies, params=PARAMS):
        r = requests.get(Api.BASE_URL + '/api/UserAccount', params=params, cookies=cookies)
        js = r.json()
        print(js)
        return js
