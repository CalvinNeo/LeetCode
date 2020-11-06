#coding: utf8

class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        stk = []
        ans = 0
        for i, x in enumerate(A):
            if (not stk) or x < A[stk[-1]]:
                stk.append(i)
            else:
                l = 0
                r = len(stk) - 1
                while l < r:
                    mid = (l + r) / 2
                    if x >= A[stk[mid]]:
                        # 说明mid是可行的，尝试往左边找
                        r = mid
                    else:
                        l = mid + 1
                # print "l {} r {} stk {}".format(stk[l], i, stk)
                ans = max(ans, i - stk[l])
        return ans

sln = Solution()
print sln.maxWidthRamp([6,0,8,2,1,5]) # 4
print sln.maxWidthRamp([9,8,1,0,1,9,4,0,4,1]) # 7
print sln.maxWidthRamp([1, 2, 1, 0, -1, -2, 0]) # 3