#coding: utf8
class Solution(object):
    def subarraySumWA(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        l = 0
        r = 0
        c = nums[0]
        ans = 0
        while l < n:
            # print "BEF l {}, r {}, c {}".format(l, r, c)
            while c < k:
                r += 1
                if r >= n:
                    break
                c += nums[r]
            # print "AFT l {}, r {}, c {}".format(l, r, c)
            if c == k:
                # print "HIT"
                ans += 1
            c -= nums[l]
            if l < r:
                l += 1
            else:
                l += 1
                r = l
                if l < n:
                    c += nums[l]
        return ans

    def subarraySumT(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        acc = [0] * n
        for i in xrange(n):
            if i == 0:
                acc[i] = nums[i]
            else:
                acc[i] = nums[i] + acc[i - 1]
        ans = 0
        for i in xrange(n):
            for j in xrange(i, n):
                prev = 0
                if i - 1 >= 0:
                    prev = acc[i - 1]
                if acc[j] - prev == k:
                    ans += 1
        return ans

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        s = {}
        s[0] = 1
        # 是否存在j使得sum[i]-sum[j] == k
        # 对于任意的i，是否存在sum[j] == sum[i]-k
        c = 0
        ans = 0
        for i in xrange(n):
            c += nums[i]
            if c - k in s:
                ans += s[c - k]
            if not c in s:
                s[c] = 0
            s[c] += 1
        return ans
## May be Negative

# sln = Solution()
# print sln.subarraySum([1,1,1], 2) # 2
# print sln.subarraySum([100,1,2,3,4], 3) # 2
# print sln.subarraySum([28,54,7,-70,22,65,-6], 100) # 1