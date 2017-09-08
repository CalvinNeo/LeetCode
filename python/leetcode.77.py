# class Solution(object):
#     def combine(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         ans = []
#         chs = range(1, n + 1)
#         def dfs(bk, s):
#             if len(bk) == k:
#                 ans.append(bk)
#                 return
#             for i in xrange(s + 1, n):
#                 nbk = bk + [chs[i]]
#                 if len(nbk) == k:
#                     ans.append(nbk)
#                 else:
#                     dfs(nbk, i)
#         dfs([], -1)
#         return ans

# class Solution:
#     def combine(self, n, k):
#         if k == 0:
#             return [[]]
#         return [pre + [i] for i in range(1, n+1) for pre in self.combine(i-1, k-1)]

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        chs = range(1, n + 1)
        bk = [0] * k
        def dfs(level, s, k):
            if k == 0:
                ans.append(bk)
                return
            for i in xrange(s + 1, n):
                bk[level] = chs[i]
                if k == 1:
                    ans.append(list(bk))
                else:
                    dfs(level+1, i, k - 1)
        dfs(0, -1, k)
        return ans

sln = Solution()
print sln.combine(4, 2)
print sln.combine(1, 1)
print sln.combine(2, 1)
import time
T = time.time()
sln.combine(20, 16)
print time.time() - T