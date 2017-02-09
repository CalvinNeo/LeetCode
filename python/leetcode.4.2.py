from bisect import *
def findkth(nums1, nums2, k):
    n1 = len(nums1)
    n2 = len(nums2)
    l = min(nums1[0], nums2[0])
    r = max(nums1[-1], nums2[-1])
    while l <= r:
        mid = (l + r + 1) / 2
        i = bisect_left(nums1, mid)
        j = bisect_left(nums2, mid)
        if i + j == k:
            if i >= n1 or j >= n2:
                l = mid + 1
            elif nums1[i] == mid or nums2[j] == mid:
                return mid
            else:
                #l = mid + 1
                return min(nums1[i], nums2[j] )
        elif i + j < k:
            l = mid + 1
        elif i + j > k:
            r = mid - 1
    return r

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0:
            return (nums2[len(nums2) / 2]  + nums2[(len(nums2) - 1)/ 2]) / 2.0
        elif n2 == 0:
            return (nums1[len(nums1) / 2]  + nums1[(len(nums1) - 1)/ 2]) / 2.0
        elif (n1 + n2) % 2:
            return findkth(nums1, nums2, (n1 + n2) / 2)
        elif (n1 + n2) % 2 == 0:
            return (findkth(nums1, nums2, (n1 + n2) / 2) + findkth(nums1, nums2, (n1 + n2 - 1) / 2)) / 2.0

sln = Solution()
print sln.findMedianSortedArrays([1, 2], [3, 4, 5, 6])
#print sln.findMedianSortedArrays([1, 3], [2])
#print sln.findMedianSortedArrays([1, 1, 3, 3], [1, 1, 3, 3])