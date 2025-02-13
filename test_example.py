import pytest

from time import sleep


def one_more(x):
    return x + 1


@pytest.mark.parametrize(
        'input_arg, expected_result',
        [(4, 5),
         pytest.param(3, 5, marks=pytest.mark.xfail)],
        ids=['First parameters', 'Second parameters']
)
def test_one_more(input_arg, expected_result):
    assert one_more(input_arg) == expected_result


def get_sort_list(string):
    new_list = sorted(string.split(', '))
    return new_list


def test_sort():
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша']


@pytest.mark.slow
def test_type():
    sleep(3)
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert isinstance(result, int)


def cartesian_product(a, b):
    return a * b


@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', ['one', 'two'])
def test_cartesian_product(x, y):
    assert cartesian_product(x, y) is not None
