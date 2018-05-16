from utils import *

class Solution(object):
    def calculateMinimumHP1(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n = len(dungeon)
        if n == 0:
            return 0
        m = len(dungeon[0])

        import sys
        max_hp = [[-sys.maxint for j in xrange(m + 1)] for i in xrange(n + 1)]
        need = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]
        dp = [[sys.maxint for j in xrange(m + 1)] for i in xrange(n + 1)]

        max_hp[0][1] = max_hp[1][0] = max_hp[0][0] = 0
        dp[0][1] = dp[1][0] = dp[0][0] = 0

        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                max_hp[i][j] = dungeon[i - 1][j - 1] + max(max_hp[i - 1][j], max_hp[i][j - 1])

        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                need[i][j] = 1 - max_hp[i][j]
                if need[i][j] <= 0:
                    need[i][j] = 1
        print "max_hp"
        print_mat(max_hp)
        print "need" 
        print_mat(need)
        for i in xrange(1, n + 1):
            for j in xrange(1, m + 1):
                dp[i][j] = max(need[i][j], min(dp[i - 1][j], dp[i][j - 1]))
        print "dp"
        print_mat(dp)
        return dp[n][m]
        # return 1 if dp[n][m] == 0 else dp[n][m]

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        import sys
        n = len(dungeon)
        if n == 0:
            return 0
        m = len(dungeon[0])

        mat = [[0 for i in xrange(m + 2)]] + map(lambda line: [0] + line + [0], dungeon) + [[0 for j in xrange(m + 2)]]
        need = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]

        for i in xrange(n, -1, -1):
            for j in xrange(m, -1, -1):
                if i == 0 or j == 0:
                    if i == 0 and j ==0:
                        need[0][0] = need[1][1] - mat[1][1]
                elif i == n and j == m:
                    need[i][j] = 1
                elif i == n:
                    need[i][j] = need[i][j + 1] - mat[i][j + 1]
                elif j == m:
                    need[i][j] = need[i + 1][j] - mat[i + 1][j]
                else:
                    need[i][j] = min(need[i][j + 1] - mat[i][j + 1], need[i + 1][j] - mat[i + 1][j])
                if need[i][j] < 1:
                    need[i][j] = 1
                # print "[{},{}] we_need = {}".format(i, j, we_need)
        # print need
        return need[0][0]

sln = Solution()
print sln.calculateMinimumHP([[0]]) # 1
print sln.calculateMinimumHP([[100]]) # 1
print sln.calculateMinimumHP([[200]]) # 1
print sln.calculateMinimumHP([[-200]]) # 201
print sln.calculateMinimumHP([[1,-2,3],[2,-2,-2]]) # 2
print sln.calculateMinimumHP([[0,-40,100],[-30,-30,1],[30,30,0]]) # 31
