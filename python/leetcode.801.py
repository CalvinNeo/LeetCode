class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        inf = 555555555555
        n = len(A)
        S = [inf] * n
        NS = [inf] * n
        S[0] = 1
        NS[0] = 0
        for i in xrange(1, n):
            A[i - 1], B[i - 1] = B[i - 1], A[i - 1]
            # swap i - 1 
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                # Swap is valid
                S[i] = min(S[i], S[i - 1] + 1)
            else:
                S[i] = min(S[i], inf)

            if A[i - 1] >= A[i] or B[i - 1] >= B[i]:
                # Need swap
                NS[i] = min(NS[i], inf)
            else:
                NS[i] = min(NS[i], S[i - 1])
            A[i - 1], B[i - 1] = B[i - 1], A[i - 1]

            # no swap i - 1 
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                # Swap is valid
                S[i] = min(S[i], NS[i - 1] + 1)
            else:
                S[i] = min(S[i], inf)

            if A[i - 1] >= A[i] or B[i - 1] >= B[i]:
                # Need swap
                NS[i] = min(NS[i], inf)
            else:
                NS[i] = min(NS[i], NS[i - 1])

        # print S
        # print NS
        return min(S[n - 1], NS[n - 1])

sln = Solution()
print sln.minSwap([1,3,5,4], [1,2,3,7]) # 1
print sln.minSwap([1], [2]) # 0
print sln.minSwap([1,7,5], [2,3,9]) # 1
print sln.minSwap([3,3,8,9,10], [1,7,4,6,8]) # 1