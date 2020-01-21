from User import *


def test_login():
    user1 = User('nkostin@bytewerk.com', 'Ytuflzq123')
    # TODO сделать класс АПИ с запросами
    r = requests.get('https://beta.jetcrypto.com/api/UserAccount', cookies=user1.get_cookies())
    assert r.status_code == 200
