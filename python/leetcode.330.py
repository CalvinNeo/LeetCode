class Solution(object):
    def minPatchesWA(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        s = set()
        ll = len(nums)
        for i in xrange(ll):
            x = nums[i]
            ns = set()
            ns.add(x)
            for y in s:
                ns.add(x + y)
            s |= ns

        self.ans = 0


        for i in xrange(1, n + 1):
            if not i in s:
                handle_missing(i)

        return self.ans

    def minPatchesWA(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        ll = len(nums)
        nums.sort()
        r = 0
        i = 0
        ans = 0
        while r < n:
            # print "r = {}, i = {}, ans = {}".format(r, i, ans)
            if i < ll:
                if nums[i] <= r + 1:
                    r += nums[i]
                    i += 1
                elif nums[i] > r + 1:
                    ans += 1
                    r += (r + 1)
                    r += nums[i]
                    i += 1
            else:
                r += (r + 1)
                ans += 1
        return ans

    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        ll = len(nums)
        nums.sort()
        r = 0
        i = 0
        ans = 0
        while r < n:
            if i < ll:
                if nums[i] <= r + 1:
                    r += nums[i]
                    i += 1
                elif nums[i] > r + 1:
                    # Do not use `nums[i]`
                    ans += 1
                    r += (r + 1)
            else:
                r += (r + 1)
                ans += 1
        return ans

sln = Solution()
print sln.minPatches(nums = [1,3], n = 6) # 1
print sln.minPatches(nums = [1,5,10], n = 20) # 2
print sln.minPatches(nums = [1,2,2], n = 5) # 0
print sln.minPatches(nums = [], n = 5) # 3
print sln.minPatches(nums = [], n = 0) # 0
print sln.minPatches([1,2,31,33], 2147483647) # 28
