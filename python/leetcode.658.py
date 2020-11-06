#coding: utf8
import bisect

def last_lt(arr, x):
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = (l + r + 1) / 2
        # print "l {} r {} mid {}".format(l, r, mid)
        if arr[mid] >= x:
            r = mid - 1
        elif arr[mid] < x:
            l = mid
    if arr[l] < x:
        return l
    else:
        return l - 1

def first_gt(arr, x):
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = (l + r) / 2
        if arr[mid] > x:
            r = mid
        else:
            l = mid + 1
    # print "l {}".format(l)
    if arr[l] > x:
        return l
    else:
        return l + 1

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(arr)

        L = 0
        R = n - 1


        lx = last_lt(arr, x)
        rx = first_gt(arr, x)
        # print "lx {} rx {}".format(lx, rx)
        eq_count = rx - lx - 1
        ans = []
        if eq_count >= k:
            return [x] * k
        # 加上所有相等的数
        ans.extend([x] * eq_count)
        rest = k - eq_count
        # print "rest {}".format(rest)
        for i in xrange(rest):
            lv = None
            rv = None
            if lx >= 0:
                lv = arr[lx]
            if rx < n:
                rv = arr[rx]
            # print "lx {} rx {}".format(lx, rx)
            if lv is None and rv is None:
                break
            if lv is None:
                ans.append(rv)
                rx += 1
            elif rv is None:
                ans.append(lv)
                lx -= 1
            else:
                ldiff = x - lv
                rdiff = rv - x
                if rdiff < ldiff:
                    ans.append(rv)
                    rx += 1
                elif rdiff > ldiff:
                    ans.append(lv)
                    lx -= 1
                else:
                    ans.append(lv)
                    lx -= 1
        return sorted(ans)


sln = Solution()
# print last_lt([1], 1) # -1
# print last_lt([1,2,3], 3) # 1
# print last_lt([1,2,3,4,5], 3) # 1
# print last_lt([1,2,4,5], 3) # 1
# print first_gt([1], 1) # 1
# print first_gt([1,2,3], 3) # 3
# print first_gt([1,2,3,4,5], 3) # 3
# print first_gt([1,2,4,5], 3) # 2


print sln.findClosestElements([1,2,3,4,5], k=4, x=3)
print sln.findClosestElements([1,2,3,4,5], k=4, x=-1)
print sln.findClosestElements([1,2,4,5], k=4, x=-1)