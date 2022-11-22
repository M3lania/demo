import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        dest="env",
        default="staging",
        choices=("production", "staging"),
        help="The environment for the application under test."
    )
    
@pytest.fixture(scope="session")
def env(request):
    """
    E.g.: staging, production
    :param request:
    :return: The environment for the application under test.
    """
    e = request.config.getoption("env")
    return e.lower()
