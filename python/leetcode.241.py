class Solution(object):
    def diffWaysToComputeWA(self, I):
        """
        :type I: str
        :rtype: List[int]
        """
        d = {}
        ops = {'+': lambda x,y: x + y, '-': lambda x,y: x - y, '*': lambda x,y: x * y}

        def gen(op, l, r):
            s = set([])
            for ll in l:
                for rr in r:
                    s.add(op(ll, rr))
            return s

        def parse(s):
            if s in d:
                return d[s]
            d[s] = []
            if not s:
                return []
            l = len(s)
            has_op = False
            for i in xrange(l):
                c = s[i]
                if c in ops.keys():
                    has_op = True
                    left = s[0: i]
                    right = s[i+1: ]
                    lans = parse(left)
                    rans = parse(right)
                    # print "s {} left {} right {} lans {} rans {}".format(s, left, right, lans, rans)
                    d[s] |= gen(ops[c], lans, rans)

            if not has_op:
                d[s] = set([eval(s)])
            return d[s]

        ans = parse(I)
        return list(ans)

    def diffWaysToCompute(self, I):
        """
        :type I: str
        :rtype: List[int]
        """
        d = {}
        ops = {'+': lambda x,y: x + y, '-': lambda x,y: x - y, '*': lambda x,y: x * y}

        def gen(op, l, r):
            s = []
            for ll in l:
                for rr in r:
                    s.append(op(ll, rr))
            return s

        def parse(s):
            if s in d:
                return d[s]
            d[s] = []
            if not s:
                return []
            l = len(s)
            has_op = False
            for i in xrange(l):
                c = s[i]
                if c in ops.keys():
                    has_op = True
                    left = s[0: i]
                    right = s[i+1: ]
                    lans = parse(left)
                    rans = parse(right)
                    # print "s {} left {} right {} lans {} rans {}".format(s, left, right, lans, rans)
                    d[s] .extend( gen(ops[c], lans, rans) )

            if not has_op:
                d[s] = [eval(s)]
            return d[s]

        ans = parse(I)
        return list(ans)


sln = Solution()
print sln.diffWaysToCompute("2-1-1")
print sln.diffWaysToCompute("2*3-4*5")