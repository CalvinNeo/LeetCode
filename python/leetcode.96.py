maxn = 1000
dp = [-1] * maxn
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n <= 2:
            return n
        if n < maxn and dp[n] != -1:
            return dp[n]
        ans = 0
        for i in xrange(0, n):
            l = self.numTrees(i)
            r = self.numTrees(n - 1 - i)
            # print "[{}, {}] l {} r {}".format(i, n - 1 - i, l, r)
            ans += (l * r)
        if n < maxn:
            dp[n] = ans
        return ans

# sln = Solution()
# print sln.numTrees(1)
# print sln.numTrees(2)
# print sln.numTrees(3)