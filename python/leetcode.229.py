class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        class Candidate(object):
            def __init__(self, k, v):
                self.k = k
                self.v = v

        pq = []
        def find_x(x):
            for i, c in enumerate(pq):
                if c.k == x:
                    return i
            return -1

        for (i, x) in enumerate(nums):
            if len(pq) <= 3:
                j = find_x(x)
                if j == -1:
                    # print "insert {}".format(x)
                    pq.append(Candidate(x, 1))
                else:
                    # print "inc {}".format(x)
                    pq[j].v += 1
            else:
                newpq = []
                for j in xrange(len(pq)):
                    newv = pq[j].v - 1
                    if newv >= 1:
                        newpq.append(Candidate(pq[j].k, newv))
                    else:
                        # print "delete {}".format(pq[j].k)
                        pass
                pq = newpq

        def check(x):
            return nums.count(x) > n / 3

        ans = []
        for c in pq:
            # print "{} is in pq".format(c.k)
            if check(c.k):
                ans.append(c.k)
        return ans
