from collections import deque as dequeue
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
        stk = dequeue()
        ans = []
        for i, x in enumerate(nums):
            if i >= k:
                # need pop
                (idx, y) = stk[0]
                if idx + k <= i:
                    # need pop idx
                    stk.popleft()
            # try add
            while len(stk):
                (idx, y) = stk[-1]
                if y <= x:
                    stk.pop()
                else:
                    break
            stk.append((i, x))
            if i >= k - 1:
                ans.append(stk[0][1])
        return ans

    def maxSlidingWindowAC(self, nums, k):
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
print sln.maxSlidingWindow([1,-1], 1) # [1, -1]
print sln.maxSlidingWindow([], 3) # []
print sln.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) # [3, 3, 5, 5, 6, 7]
print sln.maxSlidingWindow([1], 1) # 1
print sln.maxSlidingWindow([7,2,4], 2) # [7, 4]
