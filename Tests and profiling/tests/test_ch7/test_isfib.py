from unittest import TestCase
from nose.tools import assert_equal
from ch7.isfib import iseven

class Test_isfib(TestCase):
    def test_isfib_ret(self):
        v=10
        res=iseven(v)
        assert_equal(
            [0,2,4,6,8,10],res
        )