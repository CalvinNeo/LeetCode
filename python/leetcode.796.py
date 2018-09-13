class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        return B in A + A

sln = Solution()
print sln.rotateString("abc", "bca")
print sln.rotateString("abc", "acb")
