class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n == 0:
            return 0

        l, r = 0, n - 1

        while l < r:
            mid = (l + r) / 2
            # print "l {} r {} mid {}".format(l, r, mid)
            if mid + 1 >= n:
                return mid
            if A[mid] < A[mid + 1]:
                l = mid + 1
            elif A[mid] > A[mid + 1]:
                r = mid
        return l

# sln = Solution()
# # 0 0 1 2 2 2
# print sln.peakIndexInMountainArray([])
# print sln.peakIndexInMountainArray([1])
# print sln.peakIndexInMountainArray([1,2,1])
# print sln.peakIndexInMountainArray([1,2,3,1])
# print sln.peakIndexInMountainArray([1,2,3])
# print sln.peakIndexInMountainArray([1,2,3,1])