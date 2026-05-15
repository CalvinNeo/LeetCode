import bisect
def is_self_dividing(n):
    x = n
    while x:
        b = x % 10
        if b == 0:
            return False
        elif b == 1:
            x /= 10
            continue
        if n % b != 0:
            return False
        x /= 10
    return True

class Solution(object):
    def __init__(self):
        self.L = []
        for i in xrange(1, 10010):
            if is_self_dividing(i):
                self.L.append(i)
        self.n = len(self.L)

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        n = self.n
        l = bisect.bisect_left(self.L, left)
        if l + 1 < n and self.L[l + 1] == left:
            l += 1

        r = bisect.bisect_left(self.L, right)
        if r < n and self.L[r] > right:
            r -= 1

        return self.L[l:r+1]

sln = Solution()
print sln.selfDividingNumbers(1, 22)