class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr = map(int, str(num))
        sarr = sorted(arr, reverse = True)
        n = len(sarr)
        for i in xrange(n):
            if arr[i] != sarr[i]:
                j = n - 1
                while arr[j] != sarr[i]:
                    j -= 1
                arr[i], arr[j] = arr[j], arr[i]
                break
        return int(''.join(map(str, arr)))

sln = Solution()
print sln.maximumSwap(2736)
print sln.maximumSwap(9973)
print sln.maximumSwap(1)
print sln.maximumSwap(1112)
print sln.maximumSwap(0)