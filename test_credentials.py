# import os
# import pytest

def test_given_environment(env):
    print(env)
    
# @pytest.fixture(scope='session')
# def my_user():
#     return f"{os.environ['MY_USER']}"

# @pytest.fixture(scope='session')
# def my_password():
#     return f"{os.environ['MY_PASS']}"

# def test_credentials(my_user, my_password):
#     print(f"\n>>>>> User: {my_user}, \n>>>>> Password: {my_password}")
#     assert "E2E" in my_user and "as" in my_password
