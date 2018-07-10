class Solution(object):
    def triangleNumberTLE(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.sort()

        def check(a, b, c):
            # print "{} {} {} {}".format(a, b, c, a + b > c)
            return a + b > c

        ans = 0
        for i in xrange(n):
            for j in xrange(i + 1, n):
                l = j + 1
                r = n - 1
                while l < r:
                    mid = (l + r + 1) / 2
                    if check(nums[i], nums[j], nums[mid]):
                        l = mid
                    else:
                        r = mid - 1
                if l < n and check(nums[i], nums[j], nums[l]):
                    # print "l {} r {} mid {}".format(l, r, mid)
                    ans += (l - j)
                else:
                    ans += min(l - 1 - j, 0)
        return ans

    def triangleNumberWA(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        nums.sort()
        le_n = [0] * 1010
        current_level = 0
        for j, new_level in enumerate(nums):
            if new_level == current_level:
                le_n[current_level] += 1
            else:
                for i in xrange(current_level, new_level):
                    if current_level > 0:
                        le_n[i] = le_n[current_level]
                        # print "Set le_n[{}] to {}".format(current_level, le_n[current_level])
                # print "current_level {} new_level {}".format(current_level, new_level)
                current_level = new_level
                le_n[current_level] = le_n[current_level - 1] + 1
                # print "INC le_n[{}] to {}".format(current_level, le_n[current_level])

        for j in xrange(n):
            for k in xrange(j + 1, n):
                min_third = nums[k] - nums[j]
                not_possible = le_n[min_third]
                ans += max(0, j - not_possible)
                # print "_ {} {} min_third {} not_possible {} possible {} j = {}".format(nums[j], nums[k], min_third, not_possible, j - not_possible, j)
        # print le_n
        return ans
        
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        nums.sort()
        le_n = [0] * 1010
        current_level = 0
        for j, new_level in enumerate(nums):
            if new_level == current_level:
                le_n[current_level] += 1
            else:
                for i in xrange(current_level, new_level):
                    le_n[i] = le_n[current_level]
                    # print "Set le_n[{}] to {}".format(current_level, le_n[current_level])
                # print "current_level {} new_level {}".format(current_level, new_level)
                current_level = new_level
                le_n[current_level] = le_n[current_level - 1] + 1
                # print "INC le_n[{}] to {}".format(current_level, le_n[current_level])

            for k in xrange(j + 1, n):
                min_third = nums[k] - nums[j]
                not_possible = le_n[min(min_third, current_level)]
                ans += max(0, j - not_possible)
                # print "_ {} {} min_third {} not_possible {} possible {} j = {}".format(nums[j], nums[k], min_third, not_possible, j - not_possible, j)
        return ans
sln = Solution()
print sln.triangleNumber([]) # 0
print sln.triangleNumber([2,3,3]) # 1
print sln.triangleNumber([2,2,3,4]) # 3
print sln.triangleNumber([1,1,3,4]) # 0
print sln.triangleNumber([0, 3, 11, 15, 23, 67, 82, 82, 92]) # 17
