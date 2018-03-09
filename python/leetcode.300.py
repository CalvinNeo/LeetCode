class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from bisect import bisect_left
        import sys
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        dp = [sys.maxint] * n
        for (i, x) in enumerate(nums):
            j = bisect_left(dp, x)
            dp[j] = x

        j = n - 1
        while j >= 0:
            if dp[j] != sys.maxint:
                return j + 1
            j -= 1
        return 0

sln = Solution()
print sln.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
print sln.lengthOfLIS([10])
print sln.lengthOfLIS([10, 20])
print sln.lengthOfLIS([2, 2])