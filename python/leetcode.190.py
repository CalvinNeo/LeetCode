class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in xrange(32):
            ans *= 2
            ans |= (n & 1)
            n /= 2
        return ans & 0xffffffff
# sln = Solution()
# print sln.reverseBits(43261596)
# print sln.reverseBits(0)
# print sln.reverseBits(1)