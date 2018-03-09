class Solution(object):
    def maxProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * (n + 1)
        import sys
        # important, 0 is not enough here, e.g. [-2]
        m = -sys.maxint

        i = 0
        j = 1
        while i < n:
            if nums[i] == 0:
                # in case of [0]
                m = max(m, 0)
                for x in xrange(0, j):
                    for y in xrange(x + 1, j):
                        m = max(m, dp[y] / dp[x])
                j = 1
            else:
                dp[j] = dp[j - 1] * nums[i]
                j += 1

            i += 1

        for x in xrange(0, j):
            for y in xrange(x + 1, j):
                m = max(m, dp[y] / dp[x])
        return m


    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        n = len(nums)
        if n == 0:
            return 0
        maxprod = [0] * n
        minprod = [0] * n
        maxprod[0] = minprod[0] = nums[0]
        m = nums[0]
        for i in xrange(1, n):
            maxprod[i] = max(maxprod[i - 1] * nums[i], minprod[i - 1]* nums[i])
            maxprod[i] = max(maxprod[i], nums[i])
            minprod[i] = min(maxprod[i - 1]* nums[i], minprod[i - 1] * nums[i])
            minprod[i] = min(minprod[i], nums[i])
            m = max(m, maxprod[i])
        return m

sln = Solution()
# 25 0 0 2 -2 0 0
print sln.maxProduct([2,3,-2,4,0,5,5,0,1])
print sln.maxProduct([0,0,0])
print sln.maxProduct([0,0])
print sln.maxProduct([1,2])
print sln.maxProduct([-2])
print sln.maxProduct([0])
print sln.maxProduct([-2,0,-1])
