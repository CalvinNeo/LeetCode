# 867 c92.3

# You Must First Print A Table!!
P = [] 
import bisect
class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        index = bisect.bisect_left(P, N)
        return P[index]

sln = Solution()
print sln.primePalindrome(1) # 2
print sln.primePalindrome(6) # 7
print sln.primePalindrome(7) # 7
print sln.primePalindrome(8) # 11
print sln.primePalindrome(13) # 101

def print_table():
    def createPalindrome(inp, b, isOdd):
        n = inp
        palin = inp
        if (isOdd):
            n = n / b
        while (n > 0):
            palin = palin * b + (n % b)
            n = n / b
        return palin

    par = []
    def generatePaldindromes(n):
        for j in range(2):
            i = 1
            while (createPalindrome(i, 10, j % 2) < n):
                par.append( createPalindrome(i, 10, j % 2) )
                i = i + 1

    n = 10 ** 9 + 10

    def isprime(x):
        if x <= 1:
            return False
        elif x == 2:
            return True
        for i in xrange(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    pp = []
    def gen_pp():
        generatePaldindromes(n)
        for x in par:
            if isprime(x):
                pp.append(x)

    gen_pp()
    print len(pp)
    pp.sort()
    # for x in pp:
    #     print x
    print pp