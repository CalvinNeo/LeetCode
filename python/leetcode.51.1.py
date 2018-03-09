class Solution(object):
    def cancol(self, c, bd):
        for i in xrange(self.n):
            if bd[i * self.n + c] == "Q":
                return False
        return True
    def canrect(self, r, c, bd):

    def doline(self, l, bd):
        st = l * self.n
        for i in xrange(self.n):
            if self.cancol(i, bd) and self.can:
                

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        bd = "." * n * n
        self.n = n
