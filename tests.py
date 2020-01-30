from User import User
from Api import Api


def test_ping():
    ping = Api.ping()
    assert ping.status_code == 200


def test_login():
    user_data = User().login()
    assert user_data.json()['id'] != 0
