# -*- coding: utf-8 -*-
# @Time      :2021/3/26 5:10 下午
# @Author    :jxd
# @File      :conftest.py


from python_practice.course_1.core.Calc import Calc

#scope='module'方法级别 'classes'类级别  'packages'包级别
import pytest

@pytest.fixture(scope='module')
def calc_init():
    print("setup_class")
    return Calc()

