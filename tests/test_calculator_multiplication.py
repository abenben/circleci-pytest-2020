# -*- coding: utf-8 -*-

import calculator
import pytest


def func_ids(params):
    return 'Param1={},Param2={}, Result={}'. \
        format(params[0], params[1], params[2])


multiplication_lists = (
    [0, 0, 0],
    [1, 1, 1],
    [5, 1, 5],
    [10, 10, 10000])


@pytest.fixture(params=multiplication_lists, ids=func_ids)
def multiplication_task(request):
    return request.param


def test_multiplication_normal(multiplication_task):
    cal = calculator.Calculator()
    result = cal.multiplication(multiplication_task[0], multiplication_task[1])
    assert result == multiplication_task[2]
