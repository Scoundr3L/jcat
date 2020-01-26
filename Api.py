import requests


class Api:
    BASE_URL = 'https://beta.jetcrypto.com'
    params = dict(page='1', itemsPerPage='100')

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
    def user_account(currency_name, cookies):
        r = requests.get(Api.BASE_URL + '/api/UserAccount', params=Api.params, cookies=cookies)
        js = r.json()
        print(js)
        # print(js[12]['name'])
        for i in range(len(js)):
            if currency_name in js[i]['name']:
                return js[i]['balance']
