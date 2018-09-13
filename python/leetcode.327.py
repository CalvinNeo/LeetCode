import bisect
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        ans = 0
        n = len(nums)
        acc = 0
        s = {}
        for i in xrange(n):
            acc += nums[i]
            want_least = acc - upper
            want_most = acc - lower
            

sln = Solution()
print sln.countRangeSum([-2,5,-1], -2, 2)