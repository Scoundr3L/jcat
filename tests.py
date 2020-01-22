from User import *
from Api import *


def test_login():
    r = Api.login()
    assert r.status_code == 200
