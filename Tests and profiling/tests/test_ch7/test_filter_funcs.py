from unittest import TestCase
from mock import patch,call 
from nose.tools import assert_equal
from ch7.filter_funcs import filter_ints,is_positive

class FilterIntsTestCase(TestCase):

    @patch('ch7.filter_funcs.is_positive') # 6
    def test_filter_ints(self, is_positive_mock):
        # preparation
        v = [3, -4, 1, 5, 8]

        # execution
        filter_ints(v)

        # verification
        assert_equal(
            [call(3), call(-4), call(1), call(5), call(8)],
            is_positive_mock.call_args_list
        )

    def test_filter_ints_return(self):
        #prep
        v=[3,-4,0,5,9]
        #exec
        res=filter_ints(v)
        #ver
        assert_equal(
            [3,5,9],res)

    def test_filter_ints_return_two(self):
        v1 = [3, -4, 0, -2, 5, 8, -1]
        v2 = [7, -3, 0, 0, 9, 1]

        assert_equal(
            [3,5,8],filter_ints(v1)
        )
        assert_equal(
            [7,9,1],filter_ints(v2)
        )

    def test_is_positive(self):
        #boundaries boundary, the > in the inequality is how we
        #behave with regards to this boundary. Typically, when you set a boundary, you
        # divide the space into three areas: what lies before the boundary, after the boundary,
        # and on the boundary itself
        assert_equal(False, is_positive(-1))
        assert_equal(False, is_positive(0))
        assert_equal(True, is_positive(1))

    def test_is_positive_return(self):
        assert_equal(False,is_positive(0))
        for i in range(1,10**4):
            assert_equal(True, is_positive(i))
            assert_equal(False, is_positive(-i))