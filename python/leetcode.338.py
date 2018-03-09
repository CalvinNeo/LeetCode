class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for x in xrange(num):
            x += 1
            ans.append(ans[x >> 1] + (x & 1))
        return ans

sln = Solution()
print sln.countBits(5)
        