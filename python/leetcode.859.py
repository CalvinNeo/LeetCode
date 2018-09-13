class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        n1 = len(A)
        n = len(B)
        if n != n1:
            return False

        index = []
        for i in xrange(n):
            if A[i] != B[i]:
                index.append(i)

        if len(index) == 0:
            if len(list(set(A))) == n:
                # Important
                return False
            return True
        if len(index) != 2:
            return False
        if A[index[0]] == B[index[1]] and B[index[0]] == A[index[1]]:
            return True
        return False

# sln = Solution()
# print sln.buddyStrings("ab", "ab")
# print sln.buddyStrings("a", "a")