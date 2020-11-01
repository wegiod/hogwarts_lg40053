# -*- coding: utf-8 -*-
# @Time      :2020/10/31 3:08 下午
# @Author    :jxd
# @File      :test_Calc_div.py

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


    @pytest.mark.parametrize('a,b,c', [
        #结果为小数
        [1, 2, 0.5],
        [5,2,2.5],
        [6.24,2.4,2.6],
        [-2,10,-0.2],
        [-2,-10,0.2],

        #结果为整数
        [0.2,0.2,1],
        [-2,0.2, -10],
        [10,5,2],

    ])


    def test_div(self,a,b,c):



        assert self.calc.div(a,b) == c



