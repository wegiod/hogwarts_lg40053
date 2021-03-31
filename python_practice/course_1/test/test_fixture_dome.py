# -*- coding: utf-8 -*-
# @Time      :2021/3/26 3:23 下午
# @Author    :jxd
# @File      :test_fixture_dome.py
import pytest
@pytest.fixture()
def login_r(request):
    return request.param
@pytest.mark.parametrize('login_r',datas,indirect=True)
def test_case1(login_r):
    print(f"case{login_r}")




def test_calc_dome(calc_init):
    assert calc_init.mul(1, 2) == 2


def test_calc_dome2(calc_init):
    assert calc_init.mul(1, 3) == 3

