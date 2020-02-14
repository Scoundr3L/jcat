from Api import Api

def test_balance(a_user):
    """Получение балансов по КОДу валют"""
    U = a_user
    balance = U.get_balance('USDC')
    balance2 = U.get_balance('LTC')
    print(balance)
    print(balance2)
    Api.market_orders('LTC', 'USDC')