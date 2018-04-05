class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return
        m = len(board[0])

        def inboard(i, j):
            return i >= 0 and i < n and j >= 0 and j < m

        def dfs(i, j):
            if board[i][j] == 'O':
                board[i][j] = 'K'
                if inboard(i, j - 1):
                    dfs(i, j - 1)
                if inboard(i, j + 1):
                    dfs(i, j + 1)
                if inboard(i - 1, j):
                    dfs(i - 1, j)
                if inboard(i + 1, j):
                    dfs(i + 1, j)

        for i in xrange(n):
            dfs(i, 0)
        if m > 1:
            for i in xrange(n):
                dfs(i, m - 1)
        for j in xrange(m):
            dfs(0, j)
        if n > 1:
            for j in xrange(m):
                dfs(n - 1, j)

        # print board
        for i in xrange(n):
            for j in xrange(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in xrange(n):
            for j in xrange(m):
                if board[i][j] == 'K':
                    board[i][j] = 'O'

sln = Solution()
M = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sln.solve(M)
print M