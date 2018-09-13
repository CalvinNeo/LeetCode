class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        def dfs(n, k):
            if n == 0:
                return 0
            prev = dfs(n - 1, k / 2)
            if k & 1 == 1:
                # The second
                if prev & 1:
                    return 0
                else:
                    return 1
            else:
                # The first
                if prev & 1:
                    return 1
                else:
                    return 0
        return dfs(N - 1, K - 1)

# sln = Solution()
# print sln.kthGrammar(1, 1) # 0
# print sln.kthGrammar(2, 1) # 0
# print sln.kthGrammar(2, 2) # 1
# print sln.kthGrammar(4, 5) # 1
# print sln.kthGrammar(3, 1) # 0
