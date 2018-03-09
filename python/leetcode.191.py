class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        t = 0
        while n:
            t += 1
            n = n & (n - 1)
        return t