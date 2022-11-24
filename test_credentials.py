import os
import pytest

def test_given_environment(env):
    print(env)

@pytest.fixture(scope='session')
def passwords():
    return os.environ['PASS_1'], os.environ['PASS_2']

def test_credentials(passwords):
    print(passwords)
