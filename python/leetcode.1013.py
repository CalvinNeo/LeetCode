class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        S = sum(A)
        N = len(A)
        if S % 3 != 0:
            return False
        avr = S / 3
        s = 0
        c = 0
        for x in A:
            s += x
            if s == avr:
                s = 0
                c += 1
        return c >= 3

sln = Solution()
print sln.canThreePartsEqualSum( [0,2,1,-6,6,-7,9,1,2,0,1])
print sln.canThreePartsEqualSum( [0,2,1,-6,6,7,9,-1,2,0,1])
print sln.canThreePartsEqualSum( [3,3,6,5,-2,2,5,1,-9,4])
