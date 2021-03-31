# -*- coding: utf-8 -*-
# @Time      :2021/3/30 5:42 下午
# @Author    :jxd
# @File      :__init__.py.py
import logging
from typing import List

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(msecs)d %(process)d',
                    datefmt='%a ,%d %b %Y %H:%M:%S',
                    filemode='login.log',
                    filename="w",
                    )

logger = logging.getLogger(__name__)

def pytest_collection_modifyitems(session, config, items:List):
    for item in items:
        #测试用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        #测试用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    items.reverse()

