from engine_class import Engine


def test_engine_is_running(engine):
    """Test checks the engine launch"""
    assert engine.is_running


def test_check_engine_class(engine):
    """Test checks the class of object"""
    assert isinstance(engine, Engine)
