import pytest

from playmove.application import create_app


@pytest.yield_fixture(scope='session')
def app():
    # setup and return flask test app
    params = {
        'DEBUG': False,
        'TESTING': True
    }

    _app = create_app(settings_override=params)

    # establish application context before running tests
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    # setup app client and run once for each function
    yield app.test_client()
