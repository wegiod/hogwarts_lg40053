# -*- coding: utf-8 -*-
# @Time      :2020/10/31 3:08 下午
# @Author    :jxd
# @File      :test_Calc_div.py

# -*- coding: utf-8 -*-
# @Time      :2020/10/31 10:08 上午
# @Author    :jxd
# @File      :test_calc.py
import allure
import pytest

from python_practice.course_1.core.Calc import Calc

class TestClac:
    # @classmethod
    # def setup_class(cls):
    #     print("setup_class")
    #     cls.call=Calc()
    #初始化变量，每次执行类时，只执行一次
    def setup_class(self):
        print("setup_class")
        self.calc = Calc()

    #每次都执行，不适合这里
    def setup(self):
        pass

    @allure.step
    def simple_step(self,step_param1,step_param2=None):
        pass

    @pytest.mark.parametrize('a,b,c', [
        #结果为小数
        [1,2,0.5],
        [5,2,2.5],
        [6.24,2.4,2.6],
        [-2,10,-0.2],
        [-2,-10,0.2],

        #结果为整数
        [0.2,0.2,1],
        [-2,0.2, -10],
        [10,5,2],
        [9,3,3]

    ])


    def test_div(self,a,b,c):
        #图片地址，名称，类型
        allure.attach.file('/Users/giod/图片素材/23333.jpg',
                           "测试图片",
                           attachment_type=allure.attachment_type.JPG)
        self.simple_step(f'{a}{b}{c}')
        assert self.calc.div(a,b) == c



