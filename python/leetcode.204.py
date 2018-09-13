def isPrime(x):
    for i in xrange(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1

def make_table(n):
    tb = []
    for i in xrange(n):
        if isPrime(i):
            tb.append(i)
    return tb

# print make_table(200000)

T = [2, 3, 5, 7, 11]

import bisect

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = bisect.bisect_left(T, n)
        return i

sln = Solution()
print sln.countPrimes(10) # 4
print sln.countPrimes(7) # 3
print sln.countPrimes(0) # 0
print sln.countPrimes(1) # 0
print sln.countPrimes(2) # 0
