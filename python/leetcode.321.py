class Solution(object):
    def maxNumber(self, nums1, nums2, k):
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


        def toint(nums):
            m = 0
            for x in nums:
                m *= 10
                m += x
            return m

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

sln = Solution()
# print sln.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5)
# print sln.maxNumber([6, 7], [6, 0, 4], 5)
# print sln.maxNumber([3, 9], [8, 9], 3)
# print sln.maxNumber([8, 6, 9], [1, 7, 5], 3) # 9 7 5
# print sln.maxNumber([8,7,1,5], [9,7,9,1], 4)
# print sln.maxNumber([6,9,7,0], [0,5,6], 7)
print sln.maxNumber([0], [0,6,5,7,6,2], 7)
