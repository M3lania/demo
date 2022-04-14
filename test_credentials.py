import os
import pytest

@pytest.fixture(scope='session')
def my_user():
    # return f"{os.getenv('MY_USER')}"
    return f"{os.environ['MY_USER']}"

@pytest.fixture(scope='session')
def my_password():
    # return f"{os.getenv('MY_PASS')}"
    return f"{os.environ['MY_PASS']}"

def test_credentials(my_user, my_password):
    print(my_user, my_password)
    assert "E2E" in my_user and "as" in my_password
