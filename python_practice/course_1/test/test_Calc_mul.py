# -*- coding: utf-8 -*-
# @Time      :2020/10/31 10:08 上午
# @Author    :jxd
# @File      :test_calc.py
import pytest

from python_practice.course_1.core.Calc import Calc


class TestClac:
    #初始化变量，每次执行类时，只执行一次
    def setup_class(self):
        self.calc = Calc()

    #每次都执行，不适合这里
    def setup(self):
        pass
    #pytest提供的可以执行参数化的内置方法parametrize;a,b,c为变量名称，后面可跟数组或字典，用来传参
    @pytest.mark.parametrize('a,b,c',[
        #结果为整数
        [1,2,2],
        [2,5,10],
        [10,10,100],
        [1000,1000,1000000],
        [-1,-1,1],
        #结果为小数
        [0.2,0.2,0.04],
        [0.1,1,0.1],
        [0.11,10,1.1],
        [0.11,10,1.10],
        #结果为负数
        [1,-1,-1],
        [-0.1, 1, -0.1],
        [1,-0.1,-0.1],
        [-0.1,0.1,-0.01],

        #结果为0
        [0,0,0],
        [0,1,0],
        [1,0,0],
        [0.1,0,0],
        [-1,0,0],
        [-0.22,0,0],
        #结果为两位小数
        [0.6,0.7,0.42],
        #结果为两位小数，输入为三位小数
        [0.005,0.002,0.01],
        #结果为三位小数，输出为三位小数
        [0.005, 0.002, 0.010]



    ])
    #self代表是类中的实例
    def test_mul(self,a,b,c):

        assert self.calc.mul(a,b) == c


