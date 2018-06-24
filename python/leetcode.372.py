class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        bb = 0
        for x in b:
            bb *= 10
            bb += x
        newb = bb
        if newb > 1140:
            newb = bb % 1140 + 1140
        # print newb
        def fp(a, p):
            if p == 0:
                return 1
            elif p == 1:
                return a
            elif p % 2 == 1:
                return ((fp(a, p / 2) ** 2) * a) % 1337
            else:
                return (fp(a, p / 2) ** 2) % 1337
        return fp(a, newb) % 1337

def compute_euler(x):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    ans = 0
    for i in xrange(1, x + 1):
        if gcd(x, i) == 1:
            ans += 1
    return ans

# print compute_euler(1337) # = 1140