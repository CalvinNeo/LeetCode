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

def nth_element(arr, n):
    return fk(arr, 0, len(arr) - 1, n)

# https://paste.ubuntu.com/26511493/
class Solution(object):      
    def wiggleSort1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2:
            return
        mid = nth_element(nums, (length - 1) / 2)
        l, eq, r = 0, 0, length - 1
        # 1 3 5 0 2 4 ...
        f = lambda i : (1+2*i) % (length|1)
        def p():
            print "f", [f(i) for i in range(length)]
            print "r", [nums[f(i)] for i in range(length)]
            print "o", [nums[i] for i in range(length)]
        p()
        while eq <= r:
            if nums[f(eq)] > mid:
                nums[f(eq)], nums[f(l)] = nums[f(l)], nums[f(eq)]
                eq += 1
                l += 1
            elif nums[f(eq)] < mid:
                nums[f(eq)], nums[f(r)] = nums[f(r)], nums[f(eq)]
                r -= 1
            else:
                eq += 1
            p()

    def wiggleSortWA(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        mid = nth_element(nums, (n - 1) / 2)
        def f(i):
            if i < (n + 1) / 2:
                return i * 2
            else:
                return (i - (n + 1) / 2) * 2 + 1

        def p():
            print "f", [f(i) for i in range(n)]
            print "r", [nums[f(i)] for i in range(n)]
            print "o", [nums[i] for i in range(n)]

        # p()
        i, eq, j = -1, -1, -1
        while j + 1 <= n - 1:
            if nums[f(j + 1)] > mid:
                j += 1
            elif nums[f(j + 1)] == mid:
                j += 1
                eq += 1
                nums[f(j)], nums[f(eq)] = nums[f(eq)], nums[f(j)]
            else:
                j += 1
                eq += 1
                i += 1
                t = nums[f(j)]
                nums[f(j)] = nums[f(eq)]
                nums[f(eq)] = nums[f(i)]
                nums[f(i)] = t
            # p()

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        mid = nth_element(nums, (n - 1) / 2)
        def f(i):
            return (1+2*i) % (n|1)

        def p():
            print "f", [f(i) for i in range(n)]
            print "r", [nums[f(i)] for i in range(n)]
            print "o", [nums[i] for i in range(n)]

        # p()
        i, eq, j = -1, -1, -1
        while j + 1 <= n - 1:
            if nums[f(j + 1)] < mid:
                j += 1
            elif nums[f(j + 1)] == mid:
                j += 1
                eq += 1
                nums[f(j)], nums[f(eq)] = nums[f(eq)], nums[f(j)]
            else:
                j += 1
                eq += 1
                i += 1
                t = nums[f(j)]
                nums[f(j)] = nums[f(eq)]
                nums[f(eq)] = nums[f(i)]
                nums[f(i)] = t
            # p()

sln = Solution()
nn = [1] # 1
nn = [4,5,5,6] # 5 6 4 5
# nn = [1,1,2,2] # 1 2 1 2
nn = [1,1,1,2,2,2] # 1 2 1 2 1 2
# nn = [1,1,1,2,2]
# nn = [2,1,1,2,1,3,3,3,1,3,1,3,2]
# nn = [1,3,2,2,3,1]
sln.wiggleSort(nn)
print (nn)