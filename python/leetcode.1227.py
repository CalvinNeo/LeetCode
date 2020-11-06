# coding: utf8

class Solution(object):
    def nthPersonGetsNthSeatTLE(self, n):
        """
        :type n: int
        :rtype: float
        """
        dp = [[0 for i in xrange(n+1)] for j in xrange(n+1)]

        for i in xrange(1, n + 1):
            dp[1][i] = 1.0 / n

        for i in xrange(2, n + 1):
            for j in xrange(1, n + 1):
                # 位置i被占的概率，
                # 等于前面所有人[1..(i-1)]坐在i位置的概率之和
                occ = 0
                for k in xrange(1, i):
                    occ += dp[k][i]
                # print "dp[{}][{}]={}: occ {}".format(i, j, dp[i][j], occ)
                dp[i][i] = 1 - occ
                # 当位置i被占用后，i可以坐到任何没有被占用的位置
                for k in xrange(1, i):
                    # 乘上没有被占用的概率
                    # 人i在剩下的n-i+1个椅子里面随机选一个，因此还要除以一下
                    dp[i][k] = occ * (1 - sum(dp[:][k][1:i])) / (n - i + 1)
                for k in xrange(i + 1, n + 1):
                    dp[i][k] = occ * (1 - sum(dp[:][k][1:i])) / (n - i + 1)
        # print dp
        return dp[n][n]

    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        return 1 if n == 1 else 0.5


sln = Solution()
# print sln.nthPersonGetsNthSeat(1) # 1
# print sln.nthPersonGetsNthSeat(2) # 0.5
# print sln.nthPersonGetsNthSeat(3) # 0.5
# print sln.nthPersonGetsNthSeat(4) # 0.5
# print sln.nthPersonGetsNthSeat(200) # 0.5
# for i in xrange(1, 30):
#     print "{} {}".format(i, sln.nthPersonGetsNthSeat(i))