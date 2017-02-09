import sys
int_max = 2 ** 31 - 1
int_max_neg = 0 - 2 ** 31
#print int_max, int_max_neg
#print reduce(lambda x, y: x * 10 + y, [2,3,4], 0)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        v = -x if x < 0 else x
        lst = reversed([int(s) for s in str(v)])
        ans = reduce(lambda a, b: a * 10 + b, lst, 0)
        ans = -ans if x < 0 else ans
        if ans < int_max_neg or ans > int_max:
            return 0
        else:
            return ans
    