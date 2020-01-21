import requests
from User import *


# TODO cookies можно брать из юзера, не передавая в функцию
# TODO currency_name передавать пару
def get_balance(cookies, currency_name):
    params = dict(page='1', itemsPerPage='100')
    r = requests.get('https://beta.jetcrypto.com/api/UserAccount', params=params, cookies=cookies)
    js = r.json()
    print(js)
    # print(js[12]['name'])
    for i in range(len(js)):
        if currency_name in js[i]['name']:
            return js[i]['balance']


c = User('nkostin@bytewerk.com', 'Ytuflzq123')
currency_to = 'USDC'
currency_from = 'LTC'

currency_to_balance = get_balance(c.get_cookies(), currency_to)
print('fiat balance = ', currency_to_balance)

currency_from_balance = get_balance(d.get_cookies(), currency_from)
print('crypto balance = ', currency_from_balance)


def create_order(cookies):
    pass
