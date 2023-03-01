from src.classes import *


def test_get_item():
    test_case_1 = {"тестовый товар": 10}
    expected = {"тестовый товар": 10}
    test_object = Store(test_case_1)
    assert(test_object.get_items()) == expected


def test_get_free_space_Store():
    test_case_1 = {"тестовый товар": 57}
    expected = 43
    test_object = Store(test_case_1)
    assert(test_object.get_free_space()) == expected


def test_get_free_space_Shop():
    test_case_1 = {"тестовый товар": 5}
    expected = 15
    test_object = Shop(test_case_1)
    assert(test_object.get_free_space()) == expected
