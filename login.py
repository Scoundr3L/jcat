import requests


def cookies():
    auth = {
        "login": "790403463460",
        "password": "Ytuflzq123",
        "recaptcha": "string"
    }

    r = requests.post('https://beta.jetcrypto.com/api/User/login', json=auth)

    return r.cookies


def balance(c):
    params = {
        'page': '1',
        'itemsPerPage': '100'
    }
    r = requests.get('https://beta.jetcrypto.com/api/UserAccount', params=params, cookies=c)
    #print(r.json())
    js = r.json()
    print(js[0]['account']['currency'])


balance(cookies())
