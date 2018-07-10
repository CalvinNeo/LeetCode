class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        n = len(hand)
        if n == 0:
            return False
        d = {}
        for i, x in enumerate(hand):
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        maj = sorted(d.keys())

        def check(st):
            for i in xrange(st, st + W):
                if i in d and d[i] > 0:
                    d[i] -= 1
                else:
                    # print "No {}".format(i)
                    return False
            return True

        rest = n
        for i, st in enumerate(maj):
            while d[st] > 0:
                # print "check with st = {}".format(st)
                if not check(st):
                    return False
                else:
                    rest -= W
        return rest == 0