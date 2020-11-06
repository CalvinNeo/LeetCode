class Solution(object):
    def countBinarySubstringsTLE(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0

        def check(x):
            m = len(x)
            f1, f0 = x[:m/2].count('1'), x[:m/2].count('0')
            l1, l0 = x[m/2:].count('1'), x[m/2:].count('0')
            return (f0 == 0 and l1 == 0) or (f1 == 0 and l0 == 0)

        for l in xrange(2, n + 1, 2):
            for i in xrange(n - l + 1):
                if check(s[i:i+l]):
                    ans += 1
        return ans

    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        lst = []
        prev = None

        i = 0
        l = 0
        while i < n:
            if s[i] != prev:
                if l:
                    lst.append(l * (-1 if prev == '0' else 1))
                prev = s[i]
                l = 1
            else:
                l += 1
            i += 1

        if l:
            lst.append(l * (-1 if prev == '0' else 1))

        # print lst
        m = len(lst)
        for i in xrange(m - 1):
            ans += min(abs(lst[i]), abs(lst[i + 1]))

        return ans

# sln = Solution()
# print sln.countBinarySubstrings("00110011") # 6
# print sln.countBinarySubstrings("10101") # 4
# print sln.countBinarySubstrings("00110") # 3