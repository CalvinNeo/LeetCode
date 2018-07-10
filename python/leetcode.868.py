# 868 c92.1
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(A)
        if n == 0:
            return []
        m = len(A[0])
        ans = []
        for i in xrange(m):
            L = [l[i] for l in A]
            ans.append(L)
        return ans

sln = Solution()
print sln.transpose([[1,2,3],[4,5,6],[7,8,9]])
print sln.transpose([[1,2,3],[4,5,6]])