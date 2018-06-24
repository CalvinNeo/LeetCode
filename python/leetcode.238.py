class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l = [1] * (n + 2)
        r = [1] * (n + 2)
        for i in xrange(0, n):
            l[i] = l[i - 1] * nums[i]
        for i in xrange(n - 1, -1, -1):
            r[i] = r[i + 1] * nums[i]

        ans = [1] * n
        for i in xrange(n):
            # print i, i - 1, i + 1
            ans[i] = l[i - 1] * r[i + 1]
        return ans