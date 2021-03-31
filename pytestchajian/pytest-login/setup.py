# -*- coding: utf-8 -*-
# @Time      :2021/3/30 5:19 下午
# @Author    :jxd
# @File      :setup.py
from setuptools import setup
setup(
    #包的名字
    name = 'pyteest_login',
    #包在github的地址
    url='https://github.com/wegiod/hogwarts_lg40053',
    #包的版本
    version = '1.0',
    #包的作者
    author = 'wegiod',
    #包的作者的邮箱地址
    author_email = '1904123734@qq.com',
    #包的描述
    description = '这是一段概要描述',
    #包的详细描述
    long_description = "这是一段详细描述",
    #包的分类
    classifiers = [# 分类索引,pip对所属包的分类
        #所属框架
        'Framework::Pytest',
        #所属语言
        'Programming Language::Python',
        #所属开发类型
        'Topic::Software Development::Testing',
        #依赖的语言版本
        'Programming Language::Python::3.8',
     ],
    license='proprietary',
    #包的名字
    packages=['pytest_login'],
    #通过哪些关键词可以搜索到这个包
    keywords=[
        'hogwarts','lg4'
    ],
    #需要安装的依赖
    install_requires=[
        'pytest'
    ],
    #入口模块，或者入口函数
    entry_points={
        'pytest11':[
            'pytest-login = pytest-login'
        ]
    },
    zip_safe=False
)
