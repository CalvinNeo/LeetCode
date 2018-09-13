import random, bisect

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        n = len(w)
        self.r = [0] * n
        for i in xrange(n):
        	if i == 0:
        		self.r[i] = w[i]
        	else:
        		self.r[i] = w[i] + self.r[i - 1]

    def pickIndex(self):
        """
        :rtype: int
        """
        n = len(self.w)
        ran = random.randint(1, self.r[-1])
        return bisect.bisect_left(self.r, ran)

# # Your Solution object will be instantiated and called as such:
# obj = Solution([1,1,1,1])
# print obj.pickIndex()
# print obj.pickIndex()
# print obj.pickIndex()
# print obj.pickIndex()