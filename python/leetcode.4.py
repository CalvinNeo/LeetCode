import bisect
class Solution(object):
    # up midval
    def f1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        m1 = (len1 - 1) / 2
        m2 = (len2 - 1) / 2 
        if len1 == 0:
            if len2 % 2 == 0:
                return (nums2[m2] + nums2[m2 + 1]) / 2.0
            else:
                return nums2[m2]
        elif len2 == 0:
            if len1 % 2 == 0:
                return (nums1[m1] + nums1[m1 + 1]) / 2.0
            else:
                return nums1[m1]
        mid1 = nums1[m1]
        mid2 = nums2[m2]
        if len1 == 1 and len2 == 1:
            return min(nums1[0], nums2[0])
        elif len1 == 1:
            if len2 % 2 == 0:
                if mid1 >= nums2[m2 + 1]:
                    return nums2[m2 + 1]
                elif mid1 <= nums2[m2]:
                    return nums2[m2]
                else:
                    return mid1
            else:
                if mid1 >= nums2[m2 + 1]:
                    return (nums2[m2 + 1] + nums2[m2]) / 2.0
                elif mid1 <= nums2[m2 - 1]:
                    return (nums2[m2 - 1] + nums2[m2]) / 2.0
                else:
                    return (nums2[m2] + mid1) / 2.0
        elif len2 == 1:
            if len1 % 2 == 0:
                if mid2 >= nums1[m1 + 1]:
                    return nums1[m1 + 1]
                elif mid2 <= nums1[m1]:
                    return nums1[m1]
                else:
                    return mid2
            else:
                if mid2 >= nums1[m1 + 1]:
                    return (nums1[m1 + 1] + nums1[m1]) / 2.0
                elif mid2 <= nums1[m1 - 1]:
                    return (nums1[m1 - 1] + nums1[m1]) / 2.0
                else:
                    return (nums1[m1] + mid2) / 2.0

        else:       
            if mid1 == mid2:
                if (len1 % 2 == 0) and (len2 % 2 == 0):
                    return ( min(nums1[m1 + 1] , nums2[m2 + 1]) + mid1) / 2.0
                elif (len1 % 2 == 1) and (len2 % 2 == 1):
                    return mid1
                else:
                    return mid1
            else:
                if mid1 < mid2:
                    cutn = min(len1, len2) / 2
                    return self.f1(nums1[cutn: len1], nums2[0:len2-cutn])
                else:
                    cutn = min(len1, len2) / 2
                    return self.f1(nums2[cutn: len2], nums1[0:len1-cutn])

    # down midval
    def f2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        m1 = (len1) / 2
        m2 = (len2) / 2 
        if len1 == 0:
            if len2 % 2 == 0:
                return (nums2[m2] + nums2[m2 - 1]) / 2.0
            else:
                return nums2[m2]
        elif len2 == 0:
            if len1 % 2 == 0:
                return (nums1[m1] + nums1[m1 - 1]) / 2.0
            else:
                return nums1[m1]
        mid1 = nums1[m1]
        mid2 = nums2[m2]
        if len1 == 1 and len2 == 1:
            return max(nums1[0], nums2[0])
        elif len1 == 1:
            if len2 % 2 == 0:
                if mid1 >= nums2[m2]:
                    return nums2[m2]
                elif mid1 <= nums2[m2 - 1]:
                    return nums2[m2 - 1]
                else:
                    return mid1
            else:
                if mid1 >= nums2[m2 + 1]:
                    return (nums2[m2 + 1] + nums2[m2]) / 2.0
                elif mid1 <= nums2[m2 - 1]:
                    return (nums2[m2 - 1] + nums2[m2]) / 2.0
                else:
                    return (nums2[m2] + mid1) / 2.0
        elif len2 == 1:
            if len1 % 2 == 0:
                if mid2 >= nums1[m1]:
                    return nums1[m1]
                elif mid2 <= nums1[m1 - 1]:
                    return nums1[m1 - 1]
                else:
                    return mid2
            else:
                if mid2 >= nums1[m1 + 1]:
                    return (nums1[m1 + 1] + nums1[m1]) / 2.0
                elif mid2 <= nums1[m1 - 1]:
                    return (nums1[m1 - 1] + nums1[m1]) / 2.0
                else:
                    return (nums1[m1] + mid2) / 2.0

        else:       
            if mid1 == mid2:
                if (len1 % 2 == 0) and (len2 % 2 == 0):
                    return ( min(nums1[m1 - 1] , nums2[m2 - 1]) + mid1) / 2.0
                elif (len1 % 2 == 1) and (len2 % 2 == 1):
                    return mid1
                else:
                    return mid1
            else:
                if mid1 < mid2:
                    cutn = min(len1, len2) / 2
                    return self.f2(nums1[cutn: len1], nums2[0:len2-cutn])
                else:
                    cutn = min(len1, len2) / 2
                    return self.f2(nums2[cutn: len2], nums1[0:len1-cutn])
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a1 =  self.f1(nums1, nums2)
        a2 =  self.f2(nums1, nums2)
        #print "a1", a1
        #print "a2", a2
        if a1 != a2:
            return (a1 + a2) / 2.0
        else:
            return a1
    
sln = Solution()
#print sln.findMedianSortedArrays([1, 4], [2, 3])
#print sln.findMedianSortedArrays([1, 3], [2])
print sln.findMedianSortedArrays([3, 4, 5], [1, 2, 6, 7, 8])

                #smaller = None
                #bigger = None
                #smallermid = min(mid1, mid2)
                #if mid1 > mid2:
                #    bigger = nums1
                #    smaller = nums2
                #else:
                #    bigger = nums2
                #    smaller = nums1
                #i = bisect.bisect_right(bigger, smallermid)
                #off = (len(bigger) - 1) / 2 - i
                ##if len(smaller) / 2 + off > len(smaller) - 1:
                ##    anslist = bigger
                ##else:
                #small_remain_len = (len(smaller) - 1) / 2
                #bigger_remain_len = len(bigger) - 1 - i
                #curlen = min(small_remain_len, bigger_remain_len)
                #return self.findMedianSortedArrays(smaller[curlen - 1:], bigger[:i])
print bisect.bisect_right([2,3,4], 1)
print bisect.bisect_right([2,3,4], 2)
print bisect.bisect_right([2,3,4], 5)
print bisect.bisect_left([2,3,4], 1)
print bisect.bisect_left([2,3,4], 2)
print bisect.bisect_left([2,3,4], 5)
print bisect.bisect_left([2], 1)
print bisect.bisect_left([2], 2)