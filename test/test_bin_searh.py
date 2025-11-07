import pytest
from src.bin_search import binSearch


def test_middle():
    assert binSearch([1, 2, 3, 4, 5], 4) == 3


def test_start():
    assert binSearch([1, 2, 3, 4], 2) == 1


def test_not_in_list():
    assert binSearch([1, 2, 3, 4], 5) == -1


def test_unsorted():
    with pytest.raises(ValueError, match="Массив не отсортирован"):
        binSearch([8, 3, 6, 1], 6)


def test_unsorted():
    with pytest.raises(ValueError, match="такого элемента нет"):
        binSearch([1, 2, 3], 9)
