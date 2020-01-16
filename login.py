import requests


def cookies():
    auth = {
        "login": "nkostin@bytewerk.com",
        "password": "Ytuflzq123",
        "recaptcha": "string"
    }

    r = requests.post('https://beta.jetcrypto.com/api/User/login', json=auth)

    return r.cookies


def get_balance(cookies, currency_name):
    params = {
        'page': '1',
        'itemsPerPage': '100'
    }

    r = requests.get('https://beta.jetcrypto.com/api/UserAccount', params=params, cookies=cookies)
    js = r.json()
    print(js)
    # print(js[12]['name'])
    print(len(js))
    for i in range(1, len(js)):
        if currency_name in js[i]['name']:
            print(js[i]['balance'])
            return js[i]['balance']


print(get_balance(cookies(), 'USDC'))
