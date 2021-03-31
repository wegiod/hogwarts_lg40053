# -*- coding: utf-8 -*-
# @Time      :2021/3/30 5:42 下午
# @Author    :jxd
# @File      :__init__.py.py
import logging


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(msecs)d %(process)d' ,
                    datefmt='%a ,%d %b %Y %H:%M:%S',
                    filemode='login.log',
                    filename="w"
                    )




logger = logging.basicConfig(__name__)


#
# def login_INFO():


