def count_bits(x):
    c = 0
    while x:
        x /= 2
        c += 1
    return c

def get_bit(x, i):
    mask = (1 << i)
    return int(not(not(x & mask)))

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        flag = 0
        mc = count_bits(m)
        nc = count_bits(n)
        nn = max(nc, mc)
        ans = 0
        # print "nn", nn
        for i in xrange(nn-1, -1, -1):
            mi = get_bit(m, i)
            ni = get_bit(n, i)
            # print "mi {} ni {}".format(mi, ni)
            ans *= 2
            if mi != ni:
                flag = 1
            elif mi == 0:
                pass
            elif mi == 1:
                if not flag:
                    ans |= 1
        return ans

# sln = Solution()
# print sln.rangeBitwiseAnd(5,7)
# print sln.rangeBitwiseAnd(1,0)
# print sln.rangeBitwiseAnd(1,3)

# print count_bits(1)
# print count_bits(2)
# print count_bits(3)
# print count_bits(4)

# print get_bit(2, 1)
# print get_bit(2, 0)
        