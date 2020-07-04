# -*- coding: utf-8 -*-

import calculator
import pytest


def func_ids(params):
    return 'Param1={},Param2={}, Result={}'. \
        format(params[0], params[1], params[2])


division_lists = (
    [0, 1, 0],
    [1, 1, 1],
    [10, 5, 2])


@pytest.fixture(params=division_lists, ids=func_ids)
def division_task(request):
    return request.param


def test_division_normal(division_task):
    cal = calculator.Calculator()
    result = cal.division(division_task[0], division_task[1])
    assert result == division_task[2]
