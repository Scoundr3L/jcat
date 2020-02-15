from Api import Api

def test_balance(a_user):
    """Получение балансов по КОДу валют"""
    currency_from = 'LTC'
    currency_to = 'USDC'

    U = a_user

    balance = U.get_balance(currency_from)
    balance2 = U.get_balance(currency_to)
    print(balance)
    print(balance2)

    fee = U.get_trading_fee(currency_from)
    print('fee', fee)

    sell_price = U.get_price(currency_from, currency_to)['sell']
    print('sell price', sell_price)