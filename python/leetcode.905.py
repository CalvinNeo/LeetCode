class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)

        l, r = 0, n - 1
        while l < r:
            while l < r and not A[l] % 2:
                l += 1
            # l is the first odd, or == r
            while l < r and A[r] % 2:
                r -= 1
            # r is the first odd, or == l
            if l != r:
                A[l], A[r] = A[r], A[l]
        return A
        
# sln = Solution()
# print sln.sortArrayByParity([1,1,1])
# print sln.sortArrayByParity([2,2,2])
# print sln.sortArrayByParity([2])
# print sln.sortArrayByParity([])
# print sln.sortArrayByParity([1,2,1,2])