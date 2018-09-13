def lowbit(x):
    return (x & -x) & 0xffffffff

def pushin(arr, x, v, maxn):
    i = x
    while i <= maxn:
        arr[i] += v
        i += lowbit(i)

def count(arr, x):
    i = x
    s = 0
    while i > 0:
        s += arr[i]
        i -= lowbit(i)
    return s

class Solution(object):
    def reconstructQueueTLE(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        peo = [[a, b, b] for [a, b] in people]

        while peo:
            peo.sort(cmp = lambda x, y: cmp(x[0], y[0]) if x[1] == y[1] else cmp(x[1], y[1]))
            v, thres, ori = peo[0]
            n = len(peo)
            for i in xrange(1, n):
                if v >= peo[i][0]:
                    peo[i][1] -= 1
            ans.append([v, ori])
            peo = peo[1:]
        return ans

    def reconstructQueueRE(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        maxn = 11000
        n = len(people)
        arr = [0] * (maxn + 1)

        people.sort(cmp = lambda x, y: cmp(x[0], y[0]))
        for j in xrange(n):
            mi = None
            for (i, [h, k]) in enumerate(people):
                if h == -1:
                    continue
                ch = count(arr, maxn) - count(arr, h - 1 + 1)
                # print "ch = count(x >= {}) = {}, where k = {}".format(h, ch, k)
                if k == ch:
                    if mi == None:
                        mi = i
                    elif people[i][0] < people[mi][0]:
                        mi = i
            if mi != None:
                [h, k] = people[mi]
                ans.append([h, k])
                pushin(arr, h + 1, 1, maxn)
                # print "choose {}, after {}".format(h, count(arr, h))
                people[mi][0] = -1
            # print "============"
        return ans

    def reconstructQueueTLE2(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        maxn = 2500
        n = len(people)
        arr = [0] * (maxn + 1)
        lookup = set()

        people.sort(cmp = lambda x, y: cmp(x[0], y[0]))

        for [h, k] in people:
            lookup |= set([h, h - 1])

        lookup = sorted(list(lookup))

        import bisect
        def pushin_ex(arr, x, v, maxn):
            i = bisect.bisect_left(lookup, x)
            pushin(arr, i + 1, v, maxn)

        def count_ex(arr, x):
            i = bisect.bisect_left(lookup, x)
            return count(arr, i + 1)

        for j in xrange(n):
            mi = None
            for (i, [h, k]) in enumerate(people):
                if h == -1:
                    continue
                ch = count(arr, maxn) - count_ex(arr, h - 1)
                # print "ch = count(x >= {}) = {}, where k = {}".format(h, ch, k)
                if k == ch:
                    if mi == None:
                        mi = i
                    elif people[i][0] < people[mi][0]:
                        mi = i
            if mi != None:
                [h, k] = people[mi]
                ans.append([h, k])
                pushin_ex(arr, h, 1, maxn)
                # print "choose {}, after {}".format(h, count(arr, h))
                people[mi][0] = -1
            # print "============"
        return ans

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        people.sort(cmp = lambda x, y: cmp(x[1], y[1]) if x[0] == y[0] else -cmp(x[0], y[0]))
        for [h, k] in people:
            ans.insert(k, [h, k])
        return ans

# sln = Solution()
# print sln.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
# print sln.reconstructQueue([[2,4],[3,4],[9,0],[0,6],[7,1],[6,0],[7,3],[2,5],[1,1],[8,0]])
# print sln.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]])
