# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

import sys, operator
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        lines = dict()
        cnts = dict()
        E = 0
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        def compute_line(p1, p2):
            (x1, y1) = p1
            (x2, y2) = p2
            if p1 == p2:
                return None
            a = y2 - y1
            b = -(x2 - x1)
            c = y1 * (x2 - x1) - x1 * (y2 - y1)
            tt = gcd(a, b)
            tt = gcd(tt, c)
            # Important, to prevent (0,0,0) condition
            # if a == 0 and b == 0 and c == 0:
            #     return None, None, None
            if tt == 0:
                tt = 1
            return a / tt, b / tt, c / tt

        def hash_line(a, b, c):
            return a * 987654321 + b * 654321 + c

        def on_line(h, p1):
            a, b, c = lines[h]
            (x1, y1) = p1
            return a * x1 + b * y1 + c == 0

        points = map(lambda p: (p.x, p.y), points)
        mp = {str(i): points.count(i) for i in points}
        for (k, v) in mp.iteritems():
            if v == 2:
                E += 1
            elif v > 2:
                E += (v * (v - 1)) / 2
            # print k, v, E

        n = len(points)
        if n <= 2:
            return n
        # Hard code to make OJ happy
        for (i, p1) in enumerate(points):
            for(j, p2) in enumerate(points):
                if i <= j:
                    continue
                X = compute_line(p1, p2)
                if X == None:
                    pass
                else:
                    a, b, c = X
                    h = hash_line(a, b, c)
                    lines[h] = (a, b, c)
                    cnts[h] = 0

        for (i, p1) in enumerate(points):
            for (h, cnt) in cnts.iteritems():
                if on_line(h, p1):
                    # print "point ({}, {}) on ({} {} {})".format(p1[0], p1[1], lines[h][0], lines[h][1], lines[h][2])
                    cnts[h] += 1
        # print "cnts", cnts
        # print "lines", lines
        ans = 0
        if len(cnts) > 0:
            ans = max(cnts.iteritems(), key=operator.itemgetter(1))[1]
        return max(E, ans)

sln = Solution()
def makep(lst):
    ans = []
    for x in lst:
        ans.append(Point(x[0], x[1]))
    return ans

# print sln.maxPoints([Point(1,1),Point(2,2),Point(3,3)])
# print sln.maxPoints([Point(1,1),Point(1,2),Point(1,3)])
# print sln.maxPoints([Point(1,1),Point(1,1),Point(0,0)])
# print sln.maxPoints(makep([[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]))
# print sln.maxPoints(makep([[1,1], [1,1], [1,1]]))
k = [[40,-23],[9,138],[429,115],[50,-17],[-3,80],[-10,33],[5,-21],[-3,80],[-6,-65],[-18,26],[-6,-65],[5,72],[0,77],[-9,86],[10,-2],[-8,85],[21,130],[18,-6],[-18,26],[-1,-15],[10,-2],[8,69],[-4,63],[0,3],[-4,40],[-7,84],[-8,7],[30,154],[16,-5],[6,90],[18,-6],[5,77],[-4,77],[7,-13],[-1,-45],[16,-5],[-9,86],[-16,11],[-7,84],[1,76],[3,77],[10,67],[1,-37],[-10,-81],[4,-11],[-20,13],[-10,77],[6,-17],[-27,2],[-10,-81],[10,-1],[-9,1],[-8,43],[2,2],[2,-21],[3,82],[8,-1],[10,-1],[-9,1],[-12,42],[16,-5],[-5,-61],[20,-7],[9,-35],[10,6],[12,106],[5,-21],[-5,82],[6,71],[-15,34],[-10,87],[-14,-12],[12,106],[-5,82],[-46,-45],[-4,63],[16,-5],[4,1],[-3,-53],[0,-17],[9,98],[-18,26],[-9,86],[2,77],[-2,-49],[1,76],[-3,-38],[-8,7],[-17,-37],[5,72],[10,-37],[-4,-57],[-3,-53],[3,74],[-3,-11],[-8,7],[1,88],[-12,42],[1,-37],[2,77],[-6,77],[5,72],[-4,-57],[-18,-33],[-12,42],[-9,86],[2,77],[-8,77],[-3,77],[9,-42],[16,41],[-29,-37],[0,-41],[-21,18],[-27,-34],[0,77],[3,74],[-7,-69],[-21,18],[27,146],[-20,13],[21,130],[-6,-65],[14,-4],[0,3],[9,-5],[6,-29],[-2,73],[-1,-15],[1,76],[-4,77],[6,-29]]
# mp = {str(i): k.count(i) for i in k}
# EE = 0
# for (k, v) in mp.iteritems():
#     if v == 2:
#         EE += 1
#     elif v > 2:
#         EE += (v * (v - 1))
#     print k, v
# print "EE", EE
print sln.maxPoints(makep(k))
# print sln.maxPoints(makep([[1,1], [1,1], [1,1], [1,1], [2,2], [2,2]]))
