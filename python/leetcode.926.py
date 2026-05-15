class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        n1_before = [0] * (n + 2)
        n0_within_after = [0] * (n + 2)

        for i, x in enumerate(s):
            if x == '1':
                n1_before[i + 1] = n1_before[i] + 1
            else:
                n1_before[i + 1] = n1_before[i]


        for i in xrange(n - 1, -1, -1):
            x = s[i]
            if x == '0':
                n0_within_after[i] = n0_within_after[i + 1] + 1
            else:
                n0_within_after[i] = n0_within_after[i + 1]

        ans = 99999999999999
        for i in xrange(0, n+1):
            a = n1_before[i] + n0_within_after[i]
            ans = min(ans, a)

        return ans