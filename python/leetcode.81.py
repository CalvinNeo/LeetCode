# coding: utf8

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return False
        if n == 1:
            return nums[0] == target

        def is_decline(i):
            # 可以mod一下，不过这里展开写要清楚一点
            if i + 1 < len(nums):
                return nums[i] > nums[i + 1]
            else:
                return nums[i] > nums[0]

        def find_decline(l, r):
            if l > r:
                return None
            if l == r:
                if is_decline(l):
                    return l
                else:
                    return None

            if nums[l] < nums[r]:
                if is_decline(r):
                    return r
                else:
                    return None

            m = (l + r) / 2
            ans = find_decline(l, m)
            if not ans is None:
                return ans

            ans = find_decline(m + 1, r)
            if not ans is None:
                return ans

            if ans is None:
                return 0

        splitter = find_decline(0, n - 1)
        print 'splitter', splitter
        def bs(l, r):
            if l > r:
                return False
            elif l == r:
                return nums[l] == target

            m = (l + r) / 2
            if nums[m] == target:
                return True
            if bs(l, m - 1):
                return True
            if bs(m + 1, r):
                return True
            return False

        ans = bs(0, splitter)
        if ans:
            return True
        ans = bs(splitter + 1, n - 1)
        if ans:
            return True
        return False


sln = Solution()
print sln.search(nums = [5,6,7,5], target = 0)
print sln.search(nums = [6,7,1,2], target = 0)
print sln.search(nums = [1,2], target = 0)
print sln.search(nums = [1,2,3,4], target = 0)
print sln.search(nums = [2,5,6,0,0,1,2], target = 0)
print sln.search([1,1], 0)