import itertools

class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        s = str(N)
        for i in itertools.permutations(s):
            p = ''.join(i)
            if p[0] == '0':
                continue
            check = int(p)
            if (check & (check - 1)) & 0xffffffff == 0:
                return True
        return False

sln = Solution()
# f t t f f t f
print sln.reorderedPowerOf2(0)
print sln.reorderedPowerOf2(1)
print sln.reorderedPowerOf2(2)
print sln.reorderedPowerOf2(20)
print sln.reorderedPowerOf2(10)
print sln.reorderedPowerOf2(16)
print sln.reorderedPowerOf2(24)
