import requests


def get_cookies():
    auth = {
        "login": "nkostin@bytewerk.com",
        "password": "Ytuflzq123",
        "recaptcha": "string"
    }

    r = requests.post('https://beta.jetcrypto.com/api/User/login', json=auth)

    return r.cookies

# TODO cookies можно брать из юзера, не передавая в функцию
# TODO currency_name передавать пару
def get_balance(cookies, currency_name):
    params = {
        'page': '1',
        'itemsPerPage': '100'
    }

    r = requests.get('https://beta.jetcrypto.com/api/UserAccount', params=params, cookies=cookies)
    js = r.json()
    print(js)
    # print(js[12]['name'])
    for i in range(len(js)):
        if currency_name in js[i]['name']:
            return js[i]['balance']


currency_to = 'USDC'
currency_from = 'LTC'
c = get_cookies()

currency_to_balance = get_balance(c, currency_to)
print('fiat balance = ', currency_to_balance)

currency_from_balance = get_balance(c, currency_from)
print('crypto balance = ', currency_from_balance)

def create_order(cookies):

    pass