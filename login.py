import requests


def cookies():
    auth = {
        "login": "nkostin@bytewerk.com",
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
    print(js)
    print(js[0]['name'])
    for i in js:
        print(i)


balance(cookies())
