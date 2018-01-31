import pytest


from core.app import create_app
from core.config import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)