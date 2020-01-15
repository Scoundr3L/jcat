import requests


def test_rq():
    auth = {
        "login": "790403463460",
        "password": "Ytuflzq123",
        "recaptcha": "string"
    }

    r = requests.post('https://beta.jetcrypto.com/api/User/login', json=auth)
    cookies = r.cookies
    print(cookies)
    assert r.status_code == 200
