#coding: utf8

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        dp = [[0 for j in xrange(target + f + 1)] for i in xrange(d + 1)]
        MOD = 10 ** 9 + 7

        for t in xrange(1, f + 1):
            dp[0][t] = 1

        for i in xrange(1, d):
            for cf in xrange(1, f + 1):
                # 假如投了cf
                for ot in xrange(1, target + 1):
                    # 旧的target
                    dp[i][ot + cf] += dp[i - 1][ot]
                    dp[i][ot + cf] = dp[i][ot + cf] % MOD

        return dp[d - 1][target]

sln = Solution()
print sln.numRollsToTarget(d = 1, f = 6, target = 3) # 1
print sln.numRollsToTarget(d = 2, f = 6, target = 7) # 6
print sln.numRollsToTarget(d = 2, f = 5, target = 10) # 1
print sln.numRollsToTarget(d = 1, f = 2, target = 3) # 0
print sln.numRollsToTarget(d = 30, f = 30, target = 500) # 222616187