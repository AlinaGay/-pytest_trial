def one_more(x):
    return x + 1


def test_correct():
    print("Правильный тест!")
    assert one_more(4) == 5


def test_fail():
    print('Неправильный тест!')
    assert one_more(3) == 5


def get_sort_list(string):
    new_list = sorted(string.split(', '))
    return new_list


def test_sort():
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша']


def test_type():
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert isinstance(result, int)
