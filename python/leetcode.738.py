class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = map(int, str(N))
        n = len(s)
        a = [s[0]]
        for i in xrange(1, n):
            if s[i] < s[i - 1]:
                a[i - 1] -= 1
                j = i - 1
                while j > 0 and a[j] < a[j - 1]:
                    a[j - 1] -= 1
                    j -= 1
                a = a[0:j+1]
                a += [9] * (n - len(a))
                break
            else:
                a.append(s[i])
        return int(''.join(map(str, a)))

sln = Solution()
print sln.monotoneIncreasingDigits(10)
print sln.monotoneIncreasingDigits(1234)
print sln.monotoneIncreasingDigits(233)
print sln.monotoneIncreasingDigits(332)
print sln.monotoneIncreasingDigits(1332)