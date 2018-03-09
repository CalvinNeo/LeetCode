class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def lowbit(x):
            return x & (-x)

        mixed = 0
        for x in nums:
            mixed = mixed ^ x

        h = lowbit(mixed)

        s1 = 0; s2 = 0
        for x in nums:
            if x & h == 0:
                s1 = s1 ^ x
            else:
                s2 = s2 ^ x

        return [s1, s2]

sln = Solution()
print sln.singleNumber([])
print sln.singleNumber([1,1,2,2,3,4])
print sln.singleNumber([1, 2, 1, 3, 2, 5])