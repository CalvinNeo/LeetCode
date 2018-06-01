# coding: utf8
M = 10 ** 9 + 7
P = [0] * (100003)
L = [0] * (100003)
P[0] = L[0] = 1
P[1] = L[1] = 2
for i in xrange(2, 100003):
    # 第i天出勤则第i-1天可以出勤或者不出勤
    P[i] = (L[i - 1] + P[i - 1]) % M
    # 第i天不出勤，要么第i-1天出勤，要么第i-2天出勤，不能两天都不出勤
    L[i] = (P[i - 2] + P[i - 1]) % M

class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """

        all_attend = (P[n - 1] + L[n - 1]) % M
        # print "all_attend", all_attend
        tot = all_attend
        for i in xrange(n):
            mul = 1
            left = i - 1
            if left >= 0:
                mul *= (P[left] + L[left]) % M
                mul %= M
            right = (n - 1) - (i + 1)
            if right >= 0:
                mul *= (P[right] + L[right]) % M
                mul %= M
            tot += mul
            tot %= M

        return tot % M

sln = Solution()
print sln.checkRecord(1) # 3
print sln.checkRecord(2) # 8
print sln.checkRecord(3) # 19
print sln.checkRecord(4) # 43
print sln.checkRecord(5) # 94
