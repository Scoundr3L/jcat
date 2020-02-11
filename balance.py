from User import User


def test_balance():
    U = User()
    balance = U.get_balance('USDC')
    balance2 = U.get_balance('LTC')
    print(balance)
    print(balance2)
