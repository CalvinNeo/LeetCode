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
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        ans = 0
        maxn = 110
        dp = [0] * (maxn + 1)
        for i, x in enumerate(arr):
            pushin(dp, x + 1, 1, maxn)
            # count [i + 1, maxn]
            tot = count(dp, maxn)
            invc = tot - count(dp, i + 1)
            if invc == 0:
                # print "add {}".format(x)
                ans += 1
        return ans

sln = Solution()
print sln.maxChunksToSorted([]) # 0
print sln.maxChunksToSorted([4,3,2,1,0]) # 1
print sln.maxChunksToSorted([1,0,2,3,4]) # 4
print sln.maxChunksToSorted([2,0,1]) # 1
print sln.maxChunksToSorted([1,2,0,3]) # 2
