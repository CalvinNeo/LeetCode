# coding: utf8
MAX = 1010
MOD = 10**9+7
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [[0 for j in xrange(2)] for i in xrange(N + 1)]
        dp[0][0] = 1
        '''
        X  XX
        XX X
        '''
        dp[0][1] = 2
        '''
        XX XY
        YY XY
        '''
        dp[1][0] = 2
        '''
        注意后两种不能丢
        XY  XYY XYY XX
        XYY XY  XX  XYY
        '''
        dp[1][1] = 4
        for i in xrange(2, N):
            # 标准的竖着放
            dp[i][0] += dp[i - 1][0]
            # 标准的横着放
            dp[i][0] += dp[i - 2][0]
            # 如果i-2是鼓到了i-1，那么可以放一个L来补齐
            dp[i][0] += dp[i - 2][1]

            # 还可以续个横向的继续鼓，注意这里原来写的是i - 2，但应该是i - 1
            dp[i][1] += dp[i - 1][1]
            # 还可以直接放一个鼓出来
            dp[i][1] += (dp[i - 1][0] * 2)

            dp[i][0] %= MOD
            dp[i][1] %= MOD
        return dp[N - 1][0] % MOD
