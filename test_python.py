import math


def test_pi():
    assert round(math.pi, 2) == 3.14


def test_sqrt():
    assert math.sqrt(5) == 5 ** 0.5


def test_pow():
    assert math.pow(4, 5) == 4 ** 5


def test_hypot():
    assert math.hypot(6, 7) == math.sqrt(6*6 + 7*7)


def test_filter():
    assert list(filter(lambda x: x >= 10, [1, 5, 15, 10, 20, 8])) == [15, 10, 20]


def test_map():
    assert list(map(int, ['1', '2', '3', '4'])) == [1, 2, 3, 4]


def test_sorted():
    assert sorted([5, 2, 6, 7, 1, 5]) == [1, 2, 5, 5, 6, 7]