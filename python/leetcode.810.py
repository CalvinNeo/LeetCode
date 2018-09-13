class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0
        tot = 0
        for x in nums:
            tot ^= x
        if tot == 0:
            return True

        d = {i: nums.count(i) for i in nums}

        odd, eve = 0, 0
        for k, c in d.iteritems():
            if c & 1:
                odd += 1
            else:
                eve += 1

        if odd & 1:
            return False
        else:
            return True

sln = Solution()
# print sln.xorGame([1, 1, 2])
# print sln.xorGame([1, 2, 3])
print sln.xorGame([1, 2, 3, 3])
print sln.xorGame([1, 2, 3, 4])