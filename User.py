import requests


class User():
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def get_cookies(self):
        auth = {
            "login": "nkostin@bytewerk.com",
            "password": "Ytuflzq123",
            "recaptcha": "string"
        }

        r = requests.post('https://beta.jetcrypto.com/api/User/login', json=auth)

        return r.cookies
