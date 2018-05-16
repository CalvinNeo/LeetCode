class Solution(object):
    def combinationSum4_C(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [[0 for j in xrange(target + 1)] for i in xrange(n + 1)]
        dp[0][0] = 1
        for i in xrange(1, n + 1):
            for v in xrange(target + 1):
                # print "compute {} {}".format(i, v)
                for k in xrange(v / nums[i - 1] + 1):
                    prev = v - k * nums[i - 1]
                    # print "add dp[{}][{}] = {}".format(i - 1, prev, dp[i - 1][prev])
                    dp[i][v] += dp[i - 1][prev]
                # print "final = {}".format(dp[i][v])
        # print dp
        return dp[n][target]

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [0 for j in xrange(target + 1)]
        dp[0] = 1
        for i in xrange(0, target + 1):
            for j in nums:
                if i + j <= target:
                    dp[i + j] += dp[i]

        return dp[target]

sln = Solution()
print sln.combinationSum4([1, 2, 3], 4)