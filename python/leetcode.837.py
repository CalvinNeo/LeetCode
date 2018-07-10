class Solution(object):
    def new21GameTLE(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        dp = [0] * (N + 1)
        dp[0] = 1.0
        for i in xrange(K):
            for d in xrange(1, W + 1):
                if i + d <= N:
                    dp[i + d] += (1.0 / W) * dp[i]
                else:
                    break
        print dp
        ans = 0.0
        for i in xrange(K, N + 1):
            ans += dp[i]
        return ans

    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        dp = [0] * (N + 1)
        dp[0] = 1.0
        tot = 0.0
        for i in xrange(1, N + 1):
            if i <= W:
                # i can be reached from [0, i)
                if i - 1 < K:
                    tot += dp[i - 1]
                dp[i] = tot / W
            else:
                tot -= dp[i - 1 - W]
                if i - 1 < K:
                    tot += dp[i - 1]
                dp[i] = tot / W
        # print dp
        ans = 0.0
        for i in xrange(K, N + 1):
            ans += dp[i]
        return ans

sln = Solution()
print sln.new21Game(10, 1, 10) # 1.0
print sln.new21Game(6, 1, 10) # 0.6
print sln.new21Game(21, 17, 10) # 0.73278