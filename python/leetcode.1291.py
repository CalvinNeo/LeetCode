class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        def g(l, f):
            s = []
            for i in xrange(f, f + l):
                s.append(i)
            return int(''.join(map(str, s)))

        def end_len(l, f):
            return 1 if l + f > 10 else 0

        def nxt(l, f):
            ans = 0
            if end_len(l, f + 1):
                return l + 1, 1
            else:
                return l, f + 1

        def get_first():
            l = len(str(low))
            f = int(str(low)[0])
            if end_len(l, f):
                return nxt(l, f)
            if g(l, f) >= low:
                return l, f
            return nxt(l, f)

        l, f = get_first()
        ans = []
        while 1:
            x = g(l, f)
            if x > high:
                return ans
            l, f = nxt(l, f)
            ans.append(x)
        return ans


sln = Solution()
print sln.sequentialDigits(100, 100)
print sln.sequentialDigits(100, 300)
print sln.sequentialDigits(low = 1000, high = 13000)
print sln.sequentialDigits(low = 234, high = 2314)
print sln.sequentialDigits(low = 8888, high = 23333)