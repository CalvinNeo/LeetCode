def isPrime(x):
    for i in xrange(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1

def make_table(n):
    tb = []
    for i in xrange(2, n):
        if isPrime(i):
            tb.append(i)
    return tb

# print make_table(50000)

T = [2,3,5,7]

import bisect

class Solution(object):
    def countPrimesTLE(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 50000:
            i = bisect.bisect_left(T, n)
            return i
        else:
            k = len(T)
            for i in xrange(50000, n):
                if isPrime(i):
                    k += 1 
            return k

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxn = n
        dp = [True] * max((maxn + 1), 10)
        dp[0] = False
        dp[1] = False

        for i in xrange(2, int(maxn ** 0.5) + 1):
            if not dp[i]:
                continue
            for j in xrange(i * i, maxn, i):
                dp[j] = False

        return sum(dp[:maxn])

sln = Solution()
print sln.countPrimes(10) # 4
print sln.countPrimes(7) # 3
print sln.countPrimes(0) # 0
print sln.countPrimes(1) # 0
print sln.countPrimes(2) # 0
print sln.countPrimes(499979) # 41537
