# dp = [[0 for w in xrange(1010)] for n in xrange(22)]
class Solution(object):

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def pack(nums, target):
            n = len(nums)
            dp = [[0 for i in xrange(target + 5)] for j in xrange(n + 5)]
            dp[0][0] = 1
            for i in xrange(1, n + 1):
                for w in xrange(0, target + 1, 1):
                    if w - nums[i - 1] >= 0:
                        dp[i][w] = dp[i - 1][w] + dp[i - 1][w - nums[i - 1]]
                    else:
                        dp[i][w] = dp[i - 1][w]
            return dp[n][target]

        A = sum(nums)
        if A < S or (A + S) % 2 == 1:
            return 0
        target = (A + S) / 2
        ans = pack(nums, target)
        return ans

sln = Solution()
print sln.findTargetSumWays([1, 1, 1, 1, 1], 3)
print sln.findTargetSumWays([1,2,7,9,981], 1000000000)
print sln.findTargetSumWays([0,0,0,0,0,0,0,1000], -1000)
