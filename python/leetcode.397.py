class Solution(object):
    def integerReplacementWA(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n >= 1:
            # print "n", n
            while n & 1 == 0:
                n /= 2
                ans += 1
            if n == 1:
                return ans
            if n & 7 == 7:
                n += 1
                ans += 1
                continue
            n -= 1
            ans += 1

    def integerReplacementCorrect(self, n):
        i = 0;
        while n > 3:
            i += 2 if n & 1 else 1
            n = (n >> 1) + ((n & 3) == 3)

        return i + n - 1

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n >= 1:
            # print "n", n
            if n == 1:
                return ans
            if n & 1 == 0:
                n /= 2
            # elif (n & 3 == 3) and (n != 3):
            #     n += 1
            # else:
            #     n -= 1
            elif n & 7 == 7:
                n += 1
            else:
                if n == 3 or not n & 3 == 3:
                    n -= 1
                else:
                    n += 1
            ans += 1
        return ans

sln = Solution()
for i in xrange(100):
    if sln.integerReplacementCorrect(i) != sln.integerReplacement(i):
        print "at {} should be {}, but is {}".format(i, sln.integerReplacementCorrect(i), sln.integerReplacement(i))

print sln.integerReplacement(1) # 0
print sln.integerReplacement(3) # 2
print sln.integerReplacement(8) # 3
print sln.integerReplacement(7) # 4
print sln.integerReplacement(1234) # 14
print sln.integerReplacement(10000) # 16 
print sln.integerReplacement(100000000) # 31