class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])

        def f(i, j):
            c = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if 0 <= i + di < n and 0 <= j + dj < m and not (di == 0 and dj == 0):
                        c += (board[i + di][j + dj] & 1)
            return c

        for i in xrange(n):
            for j in xrange(m):
                c = f(i, j)
                if (board[i][j] & 1) == 0:
                    if c == 3:
                        # print "({},{}) REBORN for {}".format(i, j, c)
                        board[i][j] |= 2
                    # else:
                        # print "({},{}) NOBORN for {}".format(i, j, c)
                else:
                    if c < 2 or c > 3:
                        # print "({},{}) DIE for {}".format(i, j, c)
                        board[i][j] &= 1
                    else:
                        # print "({},{}) LIVE for {}".format(i, j, c)
                        board[i][j] |= 2

        # print board
        for i in xrange(n):
            for j in xrange(m):
                board[i][j] /= 2

sln = Solution()
b = [[1,1],[1,1]]
sln.gameOfLife(b)
print b
b = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
sln.gameOfLife(b)
print b