class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        n = len(board)
        m = len(board[0])
        ans = 0

        def hasLeft(i, j):
            if i - 1 < 0:
                return False
            return board[i - 1][j] == "X"

        def hasTop(i, j):
            if j - 1 < 0:
                return False
            return board[i][j - 1] == "X"

        for i in xrange(n):
            for j in xrange(m):
                if board[i][j] == "X" and not hasLeft(i, j) and not hasTop(i, j):
                    ans += 1
        return ans