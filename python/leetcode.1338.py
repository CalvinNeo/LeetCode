from collections import Counter

class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lst = [(k, v) for k, v in Counter(arr).iteritems()]
        n = len(arr)

        toremove = (n + 1) / 2
        slst = sorted(lst, key = lambda x: x[1], reverse=True)

        ans = 0
        tot = 0
        for (k, v) in slst:
            ans += 1
            tot += v
            if tot >= toremove:
                break
        return ans

sln = Solution()
print sln.minSetSize([3,3,3,3,5,5,5,2,2,7]) # 2
print sln.minSetSize([7,7,7,7,7,7]) # 1
print sln.minSetSize([1,9]) # 1
print sln.minSetSize([1000,1000,3,7]) # 1
print sln.minSetSize([1,2,3,4,5,6,7,8,9,10]) # 5
