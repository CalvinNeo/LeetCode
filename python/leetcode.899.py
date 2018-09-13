class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K == 1:
            s = S + S
            n = len(S)
            ans = S
            for i in xrange(1, n):
                if s[i:i+n] < ans:
                    ans = s[i:i+n]
            return ans
        else:
            return ''.join(sorted(S))

# sln = Solution()
# print sln.orderlyQueue("cba", 1)
# print sln.orderlyQueue("baaca", 3)
