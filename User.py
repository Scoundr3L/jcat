from Api import *


class User:
    params = {
        'page': '1',
        'itemsPerPage': '100'
    }

    def __init__(self, name='nkostin@bytewerk.com', password='ytuflzq123'):
        self.name = name
        self.password = password
        self.user_info = Api.login(self.name, self.password)
        self.cookies = self.user_info.cookies

    # uselees метод(потом удалить)
    def login(self):
        """Инфо о залогиненном пользователе"""
        return self.user_info

    # uselees метод(потом удалить)
    def get_cookies(self):
        result = self.user_info.cookies
        return result

    def get_balance(self, currency_name):
        """Получене баланса конкретного кошелька по currencyIso"""
        js = Api.user_account(self.cookies)
        for i in range(len(js)):
            if currency_name in js[i]['name']:
                # print(js[i]['balance'])
                return js[i]['balance']

    def get_trading_fee(self, currency_name):
        """Получени терйдинг Фии по currencyIso"""
        result = Api.trading_info()
        for i in range(len(result)):
            if result[i]['currencyFrom'] == currency_name:
                # print(result[i])
                return result[i]['fee']

    def get_price(self, currency_from, currency_to):
        """
        Получем Sell и Buy цены по currencyIso
        пока только при наличии цены
        """
        mo = Api.market_orders(currency_from, currency_to)
        prices = {
            # 'buy': mo['buy'][0]['price'],
            'sell': mo['sell'][0]['price']
        }
        return prices
