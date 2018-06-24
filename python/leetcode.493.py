# coding: utf8
def lowbit(x):
    return (x & -x) & 0xffffffff

def pushin(arr, x, v, maxn):
    i = x
    while i <= maxn:
        arr[i] += v
        i += lowbit(i)

def count(arr, x):
    i = x
    s = 0
    while i > 0:
        s += arr[i]
        i -= lowbit(i)
    return s

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        n = len(nums)
        maxn = 50100
        a = []
        dp = [0 for i in xrange(maxn + 1)]
        ans = 0

        # a 被用来做离散化
        for x in nums:
            a.append(x)

        a = list(set(a))
        a.sort()
        m = len(a)

        for x in nums:
            index = bisect.bisect_left(a, x)
            y = x * 2
            index2 = bisect.bisect_left(a, y) 
            if index2 >= m:
                # Can't find y, because y is larger than all numbers in `a`
                # In this case, there's no contribution made to ans
                pass
            elif a[index2] != y:
                # Can't find y, the number we find at `index2` is smaller than `y`,
                # So we must included it
                ans += count(dp, maxn) - count(dp, index2)
            else:
                ans += count(dp, maxn) - count(dp, index2 + 1)
            pushin(dp, index + 1, 1, maxn)

        return ans

sln = Solution()
print sln.reversePairs([1])
print sln.reversePairs([1,3,2,3,1])
print sln.reversePairs([2,4,3,5,1])
print sln.reversePairs([-5, -5])
