class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0

        dp = [[0 for i in xrange(m)] for j in xrange(n)]

        for i in xrange(n):
            for j in xrange(m):
                if i == 0 or j == 0:
                    if matrix[i][j] == '1':
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                    continue

                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    if matrix[i - 1][j - 1] == '0':
                        dp[i][j] = 1
                    else:
                        diag = dp[i - 1][j - 1]
                        x = i
                        while x >= i - diag:
                            if matrix[x][j] == '0':
                                break
                            x -= 1
                        x += 1
                        y = j
                        while y >= j - diag:
                            if matrix[i][y] == '0':
                                break
                            y -= 1
                        y += 1
                        # if i == 1 and j == 1:
                        #     print "x, y", x, y
                        w, l = i - x, j - y

                        dp[i][j] = min(diag + 1, w + 1, l + 1)

        ans = 0            
        for i in xrange(n):
            for j in xrange(m):
                ans = max(ans, dp[i][j])
        # print dp[1][2]
        # print dp
        return ans * ans

sln = Solution()
# 1 0 1 4 4 0
print sln.maximalSquare([["1"]])
print sln.maximalSquare([["0"]])
print sln.maximalSquare([["1", "1"], ["0", "0"]])
print sln.maximalSquare([["1", "1"], ["1", "1"]])
print sln.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print sln.maximalSquare([["0", "0"], ["0", "0"]])