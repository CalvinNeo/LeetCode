class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        if (k % 2 == 0 or k % 5 == 0):
            return -1
     
        n = 0
        for l in xrange(1, k+1):
            n = (n * 10) % k + (1 % k)
            if n % k == 0:
                return l
     
        return -1

sln = Solution()
print sln.smallestRepunitDivByK(1)