class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k = n % 4
        if k == 0:
            return False
        return True