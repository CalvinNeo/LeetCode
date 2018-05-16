class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        cur = max(nums[0:k])
        ans = [cur]
        for e in xrange(k, n):
            # s is index to be removed
            s = e - k
            # e is index to be append
            l, r = nums[s], nums[e]
            if l < cur:
                # If the element which create record `cur` is CERTAINY not removed
                if r <= cur:
                    # If the newly inserted `r` is not greater than `cur`,
                    # It will surely not break the previous record of `cur`
                    ans.append(cur)
                else:
                    # r > cur
                    # If the newly inserted `r` is not greater than `cur`,
                    # It breaks the previous record of `cur`
                    cur = r
                    ans.append(cur)
            elif l == cur:
                # The element which create record `cur` may be removed
                if r < cur:
                    # re calculate cur
                    cur = max(nums[s+1:e+1])
                    ans.append(cur)
                else:
                    # r > cur
                    cur = r
                    ans.append(cur)
                
            # l can't be greater than cur
        return ans

sln = Solution()
print sln.maxSlidingWindow([1,-1], 1)
print sln.maxSlidingWindow([], 3)
print sln.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
print sln.maxSlidingWindow([1], 1)
