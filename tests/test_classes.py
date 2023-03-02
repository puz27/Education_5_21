from src.classes import *


def test_get_item():
    test_case_1 = {"тестовый товар": 10}
    expected = {"тестовый товар": 10}
    test_object = Store(test_case_1)
    assert(test_object.get_items()) == expected


def test_get_free_space_Store():
    test_case_1 = {"тестовый товар": 5}
    expected = 95
    test_object = Store(test_case_1)
    assert(test_object.get_free_space()) == expected


def test_get_free_space_Shop():
    test_case_1 = {"тестовый товар": 5}
    expected = 15
    test_object = Shop(test_case_1)
    assert(test_object.get_free_space()) == expected


def test_add_many_items_to_Shop():
    test_case_1 = {"тестовый товар": 5}
    expected = {"тестовый товар": 10, "тестовый товар 2": 5}

    test_object = Shop(test_case_1, max_diff_items=2)
    test_object.add("тестовый товар", 5)
    test_object.add("тестовый товар 2", 5)
    test_object.add("тестовый товар 2", 1)
    test_object.add("тестовый товар 3", 1)
    assert(test_object.get_items()) == expected