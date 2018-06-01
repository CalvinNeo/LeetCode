class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        avr = s / 2
        if s % 2 == 1:
            return False

        n = len(nums)
        dp = [[0 for i in xrange(avr + 2)] for j in xrange(n + 1)]

        for i in xrange(n):
            for v in xrange(0, avr + 1):
                if v >= nums[i]:
                    dp[i][v] = max(dp[i - 1][v], dp[i - 1][v - nums[i]] + nums[i])

        return dp[i - 1][avr] == avr

sln = Solution()
print sln.canPartition([1, 5, 11, 5])
print sln.canPartition([1, 2, 3, 5])
