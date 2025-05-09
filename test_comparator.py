import pytest
from comparator import ListComparator

@pytest.mark.parametrize("l1,l2,expected", [
    ([1,2,3], [1,2,3], "Средние значения равны"),
    ([3,4,5], [1,2,3], "Первый список имеет большее среднее значение"),
    ([1,1,1], [2,2,2], "Второй список имеет большее среднее значение"),
    ([1.5,2.5], [2.0,2.0], "Средние значения равны"),
])
def test_compare_averages_parametrized(l1, l2, expected):
    comp = ListComparator(l1, l2)
    assert comp.compare_averages() == expected

def test_average_empty():
    comp = ListComparator([], [])
    with pytest.raises(ZeroDivisionError):
        comp.average([])
