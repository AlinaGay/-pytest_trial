import pytest


from engine_class import Engine


@pytest.fixture(scope='session')
def engine():
    """Fixture returns the sample of class"""
    print('Engine factory')
    return Engine()


@pytest.fixture(autouse=True)
def start_engine(engine):
    """Fixture launches the engine"""
    engine.is_running = True
    print(f'Before test engine.is_running {engine.is_running}') 
    yield
    engine.is_running = False
    print(f'After test engine.is_running {engine.is_running}')


def test_engine_is_running(engine):
    """Test checks the engine launch"""
    print('test_engine_is_running')
    assert engine.is_running


def test_check_engine_class(engine):
    """Test checks the class of object"""
    print('test_check_engine_class')
    assert isinstance(engine, Engine)
