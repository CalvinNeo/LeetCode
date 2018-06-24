# coding: utf8

primes = []
def gen_prime(N):
    for i in xrange(2, N):
        flag = 0
        for j in xrange(2, i):
            if i % j == 0:
                flag = 1
                break
        if not flag:
            primes.append(i)

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        A -> A: P
        AA -> AAAA: P2 or C1P1
        永远是能复制就复制
        '''
        if len(primes) == 0:
            gen_prime(1111)
        ans = 0
        s = 0
        rest = n
        for i in primes:
            if rest == 1:
                break
            while rest % i == 0:
                rest /= i
                ans += i
        return ans