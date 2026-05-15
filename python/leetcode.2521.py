class Solution(object):
    def __init__(self):
        L = [set() for i in xrange(1001)]
        for i in xrange(1001):
            flag = False
            for j in xrange(2, i):
                if i % j == 0:
                    flag = True
                    L[i] = L[i / j] | set([j])
                    break
            if not flag:
                L[i] = set([i])
        self.L = L

    def distinctPrimeFactors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = set([])
        for i in nums:
            ans = ans | self.L[i]
        return len(ans)

