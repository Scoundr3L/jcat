import requests


class User:
    params = {
        'page': '1',
        'itemsPerPage': '100'
    }

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def get_cookies(self):
        auth = {
            "login": self.login,
            "password": self.password,
            "recaptcha": "string"
        }

        r = requests.post('https://beta.jetcrypto.com/api/User/login', json=auth)

        return r.cookies
