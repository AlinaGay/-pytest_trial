import pytest


from engine_class import Engine


@pytest.fixture
def engine():
    """Fixture returns the sample of class"""
    return Engine()


@pytest.fixture
def start_engine(engine):
    """Fixture launches the engine"""
    engine.is_running = True


@pytest.mark.usefixtures('start_engine')
def test_engine_is_running(engine, start_engine):
    """Test checks the engine launch"""
    assert engine.is_running
