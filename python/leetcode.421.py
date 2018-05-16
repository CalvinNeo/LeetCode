def himask(i):
    # the highest bit is 31-th
    # the lowest bit is 0-th
    # i bits are set to 1
    # if i = 1 then
    # himask returns 0x80000000
    hip = (~(1 << i)) & 0xffffffff
    return (hip << (32 - i)) & 0xffffffff
def high(x, i):
    mask = himask(i)
    return x & mask & 0xffffffff
def trans(x):
    bs = []
    while x:
        b = x & 1
        bs = [b] + bs
        x >>= 1
    if len(bs) < 32:
        bs = [0] * (32 - len(bs)) + bs
    return bs

class Solution(object):
    def findMaximumXOR1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nd = [None, None, False]
        def pushin(x):
            cur = nd
            bs = trans(x)
            print "".join(map(str, bs))
            for b in bs:
                if cur[b] == None:
                    cur[b] = [None, None, False]
                cur = cur[b]
            cur[2] = True

        for x in nums:
            pushin(x)

        def solve(cur, suf):
            while cur:
                if not cur[0] and not cur[1]:
                    return suf
                if cur[0] and cur[1]:
                    return max(solve(cur[0], suf * 2 + 1), solve(cur[1], suf * 2 + 1))
                elif cur[0]:
                    return solve(cur[0], suf * 2)
                elif cur[1]:
                    return solve(cur[1], suf * 2)
        return solve(nd, 0)


    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nd = [None, None, False]

        def pushin(x):
            cur = nd
            bs = trans(x)
            # print "".join(map(str, bs))
            for b in bs:
                if cur[b] == None:
                    cur[b] = [None, None, False]
                cur = cur[b]
            cur[2] = True

        for x in nums:
            pushin(x)

        def exists(cur, x, deep):
            bs = trans(x)
            cur = nd
            for i in xrange(deep):
                b = bs[i]
                if not cur[b]:
                    return False
                cur = cur[b]
            return True

        def solve():
            suf_max = 0
            for i in xrange(1, 33):
                suf_max += (1 << (32 - i))
                flag = 0
                # print "{} find suf {}".format(32 - i, hex(suf_max))
                for n in nums:
                    a = high(n, i)
                    b = suf_max ^ a
                    # print "test a = {}, b = {}, x = {}".format(a, b, suf_max)
                    if exists(nd, b, i):
                        flag = 1
                        break
                if not flag:
                    suf_max -= (1 << (32 - i))
            return suf_max & 0xffffffff

        return solve()

sln = Solution()
# print sln.findMaximumXOR([3])
print sln.findMaximumXOR([2, 3])
print sln.findMaximumXOR([1, 2])
print sln.findMaximumXOR([5, 25])
print sln.findMaximumXOR([3, 10, 5, 25, 2, 8])