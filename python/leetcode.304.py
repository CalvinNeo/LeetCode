class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        n = len(matrix)
        if not n:
            return
        m = len(matrix[0])
        if not m:
            return
        dp = [[0 for j in xrange(m + 1)] for i in xrange(n + 1)]

        for i in xrange(n + 1):
            for j in xrange(m + 1):
                dp[i][j] = matrix[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        self.dp = dp

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # (row1, col1) - (row2+1, col2+1)
        dp = self.dp
        return dp[row2+1][col2+1] - dp[row2+1][col1] - dp[row1][col2+1] + dp[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ])
# print obj.sumRegion(2, 1, 4, 3) # -> 8
# print obj.sumRegion(1, 1, 2, 2) # -> 11
# print obj.sumRegion(1, 2, 2, 4) # -> 12

# obj = NumMatrix(matrix = [[]])
