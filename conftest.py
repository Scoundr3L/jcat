import pytest
from User import User


@pytest.fixture(scope='session')
def a_user():
    return User()
