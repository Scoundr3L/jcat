import requests


class Api:
    BASE_URL = 'https://beta.jetcrypto.com'
    params = dict(page='1', itemsPerPage='100')

    @staticmethod
    def login(login='nkostin@bytewerk.com', password='ytuflzq123'):
        auth = {
            "login": login,
            "password": password,
            "recaptcha": "string"
        }
        return requests.post(Api.BASE_URL + '/api/User/login', json=auth)

    def user_account(self, currency_name, cookies):
        r = requests.get(Api.BASE_URL + '/api/UserAccount', params=Api.params, cookies=cookies)
        js = r.json()
        print(js)
        # print(js[12]['name'])
        for i in range(len(js)):
            if currency_name in js[i]['name']:
                return js[i]['balance']
