import pytest


from engine_class import Engine


@pytest.fixture(scope='session')
def engine():
    """Fixture returns the sample of class"""
    return Engine()


@pytest.fixture(autouse=True)
def start_engine(engine):
    """Fixture launches the engine"""
    engine.is_running = True
    yield
    engine.is_running = False
