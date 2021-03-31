# -*- coding: utf-8 -*-
# @Time      :2021/3/30 3:27 下午
# @Author    :jxd
# @File      :test_mm.py

import pytest
@pytest.mark.parametrize('name',[
    "哈利",
    "赫敏"
])
def test_mm(name):
    print(name)


def test_login():
    pass

def test_login_fail():
    pass

def test_search():
    pass

def test_env(cmdoption):
    # print(cmdoption)
    env,datas = cmdoption
    host = datas['env']['host']
    port = datas['env']['port']
    url = host + ':' + str(port)
    print(url)