# -*- coding: utf-8 -*-
# @Time      :2020/10/31 10:08 上午
# @Author    :jxd
# @File      :test_calc.py
import pytest
import yaml

from python_practice.course_1.core.Calc import Calc

def load_data( path='data'):
    with open('data.yaml') as f:
        data = yaml.safe_load(f)
        keys=",".join(data[0].keys())
        values=[d.values() for d in data]
        return {'keys':keys,'values':values}

class TestClac:

    #初始化变量，每次执行类时，只执行一次
    def setup_class(self):
        self.calc = Calc()

    #每次都执行，不适合这里
    def setup(self):
        pass
    #pytest提供的可以执行参数化的内置方法parametrize;a,b,c为变量名称，后面可跟数组或字典，用来传参
    @pytest.mark.parametrize(load_data()['keys'],load_data()['values'])
    #self代表是类中的实例
    def test_mul(self,a,b,c):

        assert self.calc.mul(a,b) == c


