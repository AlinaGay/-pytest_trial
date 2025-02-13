import pytest


@pytest.fixture
def give_me_a_string():
    return 'Какой чудесный день!'


@pytest.fixture
def pack_to_list(give_me_a_string):
    return [give_me_a_string]


def test_string_fixture(pack_to_list, give_me_a_string):
    assert pack_to_list != [give_me_a_string]