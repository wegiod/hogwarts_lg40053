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
    # 初始化变量，每次执行类时，只执行一次
    def setup_class(self):
        self.calc = Calc()

    # 每次都执行，不适合这里
    def setup(self):
        pass

    @pytest.mark.parametrize('a,b', [
        #除0
        [2,0],
        [-1,0],
        [-0.1,0],

    ])
    def test_div(self, a, b):
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(a,b)



