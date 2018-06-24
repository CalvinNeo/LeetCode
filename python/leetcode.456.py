# coding: utf8
import Queue, bisect
class Solution(object):
    def find132patternTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # ai < aj > ak
        # 如果固定ak，是否可以贪最大的aj？不对，假设最大的aj在0位置
        # 应该是for k in [n-1..0]，找第一个合法的j，这样我们只要检查nums[k]和nums[i]，其中i<j
        # 或者我们for j，找到合法的最大的k，这种解法需要O(n^2)
        n = len(nums)
        inf = 555555555
        if n < 3:
            return False
        l = [inf] * n
        for i in xrange(1, n):
            l[i] = min(l[i - 1], nums[i - 1])
        r = [-inf] * n
        for i in xrange(n - 1):
            for j in xrange(i, n):
                if nums[j] < nums[i]:
                    r[i] = max(r[i], nums[j])
        # print l
        # print r
        for i in xrange(n - 1):
            # print "nums[{}] = {}, l = {}".format(i, nums[i], l[i])
            a = l[i]
            b = r[i]
            c = nums[i]
            if a < b < c:
                return True
        return False

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        inf = 555555555
        if n < 3:
            return False
        l = [inf] * n
        for i in xrange(1, n):
            l[i] = min(l[i - 1], nums[i - 1])

        def check(a, b, c):
            return b > c > a
        # a b c
        s = []
        for i in xrange(n - 1, -1, -1):
            x = nums[i]
            while len(s) > 0 and s[-1] < x:
                if check(l[i], nums[i], s[-1]):
                    return True
                else:
                    # 没有这样的a，说明我们的b不够大
                    s.pop()
            # 当前的b比最小的c还要小，那对不起，进栈吧
            s.append(x)
        return False
