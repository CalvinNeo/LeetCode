dp = [0] * 100000
dp[1] = 3
for i in xrange(1, 100000):
    dp[i] = i * 3 + i * (i - 1)

import bisect

class Solution(object):
    def bulbSwitchTLE(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in xrange(n):
            t = 1
            for j in xrange(2, n + 1):
                if i % j == j - 1:
                    t = 1 - t
            ans += t
        return ans
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bisect.bisect_right(dp, n - 1)

sln = Solution()
for i in xrange(1, 25):
    print sln.bulbSwitch(i), 