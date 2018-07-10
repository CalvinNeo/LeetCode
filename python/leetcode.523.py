# coding: utf8
class Solution(object):
    def checkSubarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''
        1. 找至i的和mod k为0的子串
        2. 即找至i-1的和mod k为k - i的子串
        用集合维护一下即可
        这道题只能勉强过因为是O(n^k)的，题解是O(n)的：
        如果当前的累加和除以k得到的余数在set中已经存在了，那么说明之前必定有一段子数组和可以整除k
        '''
        n = len(nums)
        mods = 0
        s = set()
        if k == 0:
            for i in xrange(n - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False
        elif k == 1:
            if n <= 1:
                return False
            else:
                return True
        for i, x in enumerate(nums):
            # print s
            if i != 0:
                want = (k - x) % k
                # print "want", want
                if want in s:
                    return True
            ns = set()
            for y in s:
                ns |= set([(y + x) % k])
            ns |= set([x])
            s = ns
        return False

    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        tot = 0
        s = set([0])
        if k == 0:
            for i in xrange(n - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False
        elif k == 1:
            if n <= 1:
                return False
            else:
                return True
        if n <= 1:
            return False
        for i,x in enumerate(nums):
            tot += x
            tot %= k
            # print tot
            if tot in s:
                if x == k:
                    if i > 0 and nums[i - 1] == x:
                        return True
                else:
                    return True
            s |= set([tot])
        return False

sln = Solution()
print sln.checkSubarraySum([23, 2, 4, 6, 7], 6) # True
print sln.checkSubarraySum([23, 2, 6, 4, 7], 6) # True
print sln.checkSubarraySum([1], 6) # False
print sln.checkSubarraySum([], 6) # False
print sln.checkSubarraySum([6], 6) # False
print sln.checkSubarraySum([23,2,6,4,7], 0) # False
print sln.checkSubarraySum([0,0], 0) # True
print sln.checkSubarraySum([0], 0) # False
print sln.checkSubarraySum([1,5,3], 5) # False
print sln.checkSubarraySum([5,3], 5) # False
print sln.checkSubarraySum([0,1,0], 0) # False
print sln.checkSubarraySum([1,2,3], 6) # True
print sln.checkSubarraySum([1,2,3], 4) # False
print sln.checkSubarraySum([1,1], 1) # True
print sln.checkSubarraySum([4,4], 4) # True
print sln.checkSubarraySum([0], -1) # False
