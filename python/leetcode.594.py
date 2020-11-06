from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = dict(Counter(nums))
        ck = sorted(list(c.keys()))
        if len(ck) < 2:
            return 0
        else:
            maxk = 0
            maxv = 0
            for i in xrange(len(ck) - 1):
                if ck[i] + 1 == ck[i + 1] and c[ck[i]] + c[ck[i + 1]] > maxv:
                    maxk = ck[i]
                    maxv = c[ck[i]] + c[ck[i + 1]]
            return maxv
            # ans = []
            # for x in nums:
            #     if x == maxk or x == maxk + 1:
            #         ans.append(x)

            # return ans

sln = Solution()
print sln.findLHS([1,3,5,7,9,11,13,15,17])
print sln.findLHS([1,3,2,2,5,2,3,7])
print sln.findLHS([1,1,1,1])
