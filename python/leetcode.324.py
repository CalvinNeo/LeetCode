def fk(arr, fr, to, k):
    if fr >= to:
        return arr[to]
    p = arr[fr]
    l, r = fr, to
    while l < r:
        # Must in front of the next while
        while l < r and arr[r] >= p:
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

def nth_element(arr, n):
    return fk(arr, 0, len(arr) - 1, n)

class Solution(object):      
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2:
            return
        mid = fk(nums, 0, length - 1, (length - 1) / 2)
        l, eq, r = 0, 0, length - 1
        m = lambda i : (1+2*i) % (length|1)
        while eq <= r:
            if nums[m(eq)] > mid:
                nums[m(eq)], nums[m(l)] = nums[m(l)], nums[m(eq)]
                eq += 1
                l += 1
            elif nums[m(eq)] < mid:
                nums[m(eq)], nums[m(r)] = nums[m(r)], nums[m(eq)]
                r -= 1
            else:
                eq += 1

        # kk = []
        # for i in xrange(length):
        #     kk.append(nums[m(i)])
        # print kk

sln = Solution()
nn = [1]
nn = [1,1,1,2,2,2]
nn = [1,1,1,2,2]
# nn = [2,1,1,2,1,3,3,3,1,3,1,3,2]
nn = [1,3,2,2,3,1]
sln.wiggleSort(nn)
print nn