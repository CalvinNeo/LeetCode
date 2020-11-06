def toint(nums):
    m = 0
    for x in nums:
        m *= 10
        m += x
    return m

class Solution(object):
    def maxNumberTLE(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def make_wrong(nums, req):
            n = len(nums)
            if n < req or req == 0:
                return []
            ans = nums[0:req]
            mindex = ans.index(min(ans))
            for i in xrange(req, n):
                if nums[i] >= ans[mindex]:
                    ans = ans[0:mindex] + ans[mindex+1:] + [nums[i]]
                    mindex = ans.index(min(ans))
            return ans

        def make_wrong2(nums, req):
            n = len(nums)
            if n < req or req == 0:
                return []
            ans = nums[0:req]
            mindex = ans.index(min(ans))
            i = 1
            while i < n:
                leading_len = n - i
                if leading_len > req:
                    leading_len = req
                replace_start = req - leading_len
                flag = False
                # print "i {}, n {}, req {}, leading_len {}, replace_start {}".format(i, n, req, leading_len, replace_start)
                for j in xrange(leading_len):
                    if ans[replace_start + j] < nums[i + j]:
                        flag = True
                        break
                    elif ans[replace_start + j] > nums[i + j]:
                        flag = False
                        break
                if flag:
                    # print "replace {} with {}".format(str(ans[replace_start:]), str(nums[i: i + leading_len]))
                    ans[replace_start:] = nums[i: i + leading_len]
                    i += 1
                else:
                    i += 1
            return ans


        def make(nums, req):
            n = len(nums)
            if n < req or req == 0:
                return []
            ans = []
            for i in xrange(0, n):
                while len(ans) > 0 and len(ans) + n - i > req and nums[i] > ans[-1]:
                    ans.pop()
                if len(ans) < req:
                    ans.append(nums[i])
            return ans

        def merge(lp, rp):
            ans = []
            n = len(lp)
            m = len(rp)
            i = 0
            j = 0
            while i < n or j < m:
                if i < n and j < m:
                    choosel = None
                    ii = i
                    jj = j
                    while ii < n and jj < m:
                        if lp[ii] < rp[jj]:
                            choosel = False
                            break
                        elif lp[ii] > rp[jj]:
                            choosel = True
                            break
                        else:
                            ii += 1
                            jj += 1
                    if choosel == None:
                        if ii >= n:
                            choosel = False
                        else:
                            choosel = True
                    if choosel:
                        ans.append( lp[i] )
                        i += 1
                    else:
                        ans.append( rp[j] )
                        j += 1
                elif i < n:
                    ans.append( lp[i] )
                    i += 1
                elif j < m:
                    ans.append( rp[j] )
                    j += 1
            return ans

        # print make(nums1, 2)
        # print make(nums2, 3)
        # print merge([0,5,6], [0])

        mans = []
        mint = 0
        n = len(nums1)
        m = len(nums2)
        if n + m < k:
            return []

        for i in xrange(0, k + 1):
            lp = make(nums1, i)
            rp = make(nums2, k - i)
            # print "---------"
            # print lp
            # print rp
            merged = merge(lp, rp)
            newint = toint(merged)
            if newint > mint:
                mint = newint
                mans = merged

        return mans

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n1 = len(nums1)
        n2 = len(nums2)

        def select(A, m):
            # Choose m from A such that they make the biggest number
            n = len(A)
            stk = []
            for i, x in enumerate(A):
                while stk and stk[-1] < x and len(stk) + n - (i + 1) >= m:
                    stk.pop()
                stk.append(x)
            return stk[:m]

        def greater(A, i, B, j):
            nn1 = len(A)
            nn2 = len(B)
            while i < nn1 and j < nn2 and A[i] == B[j]:
                i += 1
                j += 1
            if i >= nn1 and j >= nn2:
                # Equal
                return True
            elif i >= nn1:
                # B greater
                return False
            elif j >= nn2:
                return True
            else:
                return A[i] > B[j]

        def merge(A, B):
            nn1 = len(A)
            nn2 = len(B)
            i = 0
            j = 0
            r = []
            while i < nn1 and j < nn2:
                if greater(A, i, B, j):
                    r.append(A[i])
                    i += 1
                else:
                    r.append(B[j])
                    j += 1
            if i < nn1:
                r.extend(A[i:])
            if j < nn2:
                r.extend(B[j:])
            return r

        current = 0
        ans = []
        for a in xrange(0, k + 1):
            b = k - a
            if a > n1 or b > n2:
                continue
            la = select(nums1, a)
            lb = select(nums2, b)
            p = merge(la, lb)
            np = toint(p)
            if np > current:
                current = np
                ans = p
        return ans

# sln = Solution()
# # [9, 8, 6, 5, 3]
# # [6, 7, 6, 0, 4]
# # [9, 8, 9]
# # [9, 7, 5]
# # [9, 9, 8, 7]
# # [6, 9, 7, 0, 5, 6, 0]
# # [0, 6, 5, 7, 6, 2, 0]
# print sln.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
# print sln.maxNumber([6, 7], [6, 0, 4], 5)
# print sln.maxNumber([3, 9], [8, 9], 3)
# print sln.maxNumber([8, 6, 9], [1, 7, 5], 3) # 9 7 5
# print sln.maxNumber([8,7,1,5], [9,7,9,1], 4)
# print sln.maxNumber([6,9,7,0], [0,5,6], 7)
# print sln.maxNumber([0], [0,6,5,7,6,2], 7)
# print sln.maxNumber([2,5,6,4,4,0], [7,3,8,0,6,5,7,6,2], 15)
