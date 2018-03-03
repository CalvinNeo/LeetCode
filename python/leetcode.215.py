def fk(arr, fr, to, k):
    if fr >= to:
        return arr[to]
    p = arr[fr]
    l, r = fr, to
    while l < r:
        # Must in front of the next while
        while l < r and arr[r] >= p: # use `>=` to enable sequence of identity elements
            r -= 1
        arr[l] = arr[r]
        while l < r and arr[l] <= p:
            l += 1
        arr[r] = arr[l]
    # print arr
    # now set arr[l] as p
    arr[l] = p
    pos = l
    if pos == k:
        return p
    elif pos > k: 
        return fk(arr, fr, pos-1, k)
    else:
        return fk(arr, pos+1, to, k)

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # https://paste.ubuntu.com/26504777/
        # http://blog.csdn.net/a641324093/article/details/78307004
        n = len(nums)
        return fk(nums, 0, n - 1, n - k)

sln = Solution()

print sln.findKthLargest([1,2], 1) # 2
print sln.findKthLargest([1,2], 0) # 1
print sln.findKthLargest([2,1], 0) # 1
print sln.findKthLargest([2,1], 1) # 2
print sln.findKthLargest([3,2,1,5,6,4], 2) # 3
print sln.findKthLargest([1,2,3], 2) # 3
print sln.findKthLargest([-1,2,0], 1) # 0