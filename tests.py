from User import User
from Api import Api


def test_ping():
    ping = Api.ping()
    assert ping.status_code == 200


def test_login(a_user):
    U = a_user
    user_id = U.login().json()['id']
    assert user_id != 0


def test_balance(a_user):
    # balance = User().get_balance('USDC')
    U = a_user
    balance = U.get_balance('USDC')
    balance2 = U.get_balance('LTC')
    print(balance)
    print(balance2)
