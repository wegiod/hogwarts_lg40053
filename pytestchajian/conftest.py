# -*- coding: utf-8 -*-
# @Time      :2021/3/30 3:31 下午
# @Author    :jxd
# @File      :conftest.py
from typing import List

import pytest
import yaml


def pytest_collection_modifyitems(session, config, items:List):
    for item in items:
        #测试用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        #测试用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


#         # 如果login在item.nodeid中，那么就加上marker
#         if 'login' in item.nodeid:
#             item.add_marker(pytest.mark.login)
#     items.reverse()
#
# #注册argparse样式选项和ini样式配置值，在测试运行开始时调用一次
# def pytest_addoption(parser):
#     mygroup = parser.getgroup("hogwarts") # group将下面所有的option都展示在这个group下
#     mygroup.addoption(
#         "--env", #  注册一个命令行选项
#         default='test', #   参数的默认值
#         dest='env', #   存入变量env
#         help='set your run env' #   帮助提示 参数的描述信息
#     )
#
# @pytest.fixture(scope='session')
# def cmdoption(request):
#     env = request.config.getoption('--env',default='test')
#     if env == 'test':
#         print("测试环境")
#         #获取测试路径
#         datapath = "datas/test/datas.yaml"
#     else:
#         print("开发环境")
#         datapath = "datas/dev/datas.yaml"
#     with open(datapath) as f:
#         datas = yaml.safe_load(f)
#     return env,datas
#


