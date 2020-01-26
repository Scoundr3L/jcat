from User import User
from Api import Api


def test_ping():
    r = Api.ping()
    assert r.status_code == 200


def test_login():
    user1 = User()
    r = user1.login()
    print(r)
    assert r.status_code == 200
