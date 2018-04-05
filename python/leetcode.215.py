def fk1(arr, fr, to, k):
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
        return fk1(arr, fr, pos-1, k)
    else:
        return fk1(arr, pos+1, to, k)

def fk2(arr, fr, to, k):
    if fr >= to:
        return arr[to]
    p = arr[fr]
    l, r = fr, to
    while l < r:
        # Must in front of the next while
        while l < r and arr[r] >= p:
            r -= 1
        while l < r and arr[l] <= p:
            l += 1
        if l == r:
            arr[l], arr[fr] = arr[fr], arr[l]
        else:
            arr[l], arr[r] = arr[r], arr[l]
    pos = l
    if pos == k:
        return p
    elif pos > k: 
        return fk2(arr, fr, pos-1, k)
    else:
        return fk2(arr, pos+1, to, k)

def fk2(arr, fr, to, k):
    # Error
    if fr >= to:
        return arr[to]
    p = arr[fr]
    l, r = fr, to

    while l < r:
        # r: >= p
        if arr[r] < p:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
        else:
            r -= 1

    pos = l
    if arr[l] == p:
        l -= 1
    if pos == k:
        return arr[l]
    elif pos > k: 
        return fk2(arr, fr, l, k)
    else:
        return fk2(arr, r + 1, to, k)

def fk3(arr, fr, to, k):
    # for index >= j: value >= p
    # for index > i: value < p
    # for index <= i: not sorted
    # for index == fr: swap eventually
    if fr >= to:
        return arr[to]
    p = arr[fr]

    j = to + 1
    for i in xrange(to, fr, -1):
        if arr[i] >= p:
            j -= 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[fr], arr[j - 1] = arr[j - 1], arr[fr]
    pos = j - 1

    if pos == k:
        return arr[pos]
    elif pos > k: 
        return fk3(arr, fr, pos - 1, k)
    else:
        return fk3(arr, pos + 1, to, k)

def hk1(arr, fr, to, k):
    def push_down(arr, cur, end):
        lson = 2 * cur + 1
        rson = 2 * cur + 2
        if lson > end:
            return
        max_index = lson
        if rson <= end and arr[rson] > arr[lson]:
            max_index = rson
        if arr[cur] < arr[max_index]:
            arr[cur], arr[max_index] = arr[max_index], arr[cur]
            push_down(arr, max_index, end)

    def build(arr, to):
        for i in xrange((to - 1) / 2, -1, -1):
            push_down(arr, i, to)

    def pop(arr, end):
        arr[0], arr[end] = arr[end], arr[0]
        push_down(arr, 0, end - 1)
        return arr[end]

    end = to
    build(arr, to)
    x = 0
    for i in xrange(k):
        x = pop(arr, end - i)
    return x


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
        # return fk3(nums, 0, n - 1, k)
        # return fk3(nums, 0, n - 1, n - k)
        return hk1(nums, 0, n - 1, k)

sln = Solution()
# K-th smallest 2 1 1 2 3 3 0 2 5 5

print sln.findKthLargest([1,2], 1) # 2
print sln.findKthLargest([1,2], 0) # 2
print sln.findKthLargest([2,1], 0) # 2
print sln.findKthLargest([2,1], 1) # 2
print sln.findKthLargest([3,2,1,5,6,4], 2) # 5
print sln.findKthLargest([1,2,3], 2) # 2
print sln.findKthLargest([-1,2,0], 1) # 2
print sln.findKthLargest([3,2,1], 1) # 3
print sln.findKthLargest([3,2,1,5,6,4], 4) # 3
print sln.findKthLargest([4,6,5], 1) # 6
