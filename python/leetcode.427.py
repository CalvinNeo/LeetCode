# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def G(x1, y1, x2, y2):
            return [l[y1:y2+1] for l in grid[x1:x2+1]]

        def all_same(x1, y1, x2, y2):
            g = G(x1, y1, x2, y2)
            s = sum([sum(i) for i in g])
            l = (y2 - y1 + 1) * (x2 - x1 + 1)
            # print "g {}, s {} l {}".format(g, s, l)
            if s == l or s == 0:
                return (True, 1 if s == l else 0)
            else:
                return (False, None)

        def C(x1, y1, x2, y2):
            b, v = all_same(x1, y1, x2, y2)
            if b:
                # print "[{}, {}] - [{}, {}]. v {}, b {}".format(x1, y1, x2, y2, v, b)
                return Node(v, b, None, None, None, None)


            mx = (x1 + x2) / 2
            my = (y1 + y2) / 2
            topLeft = C(x1, y1, mx, my)
            topRight = C(mx+1, y1, x2, my)
            bottomLeft = C(x1, my+1, mx, y2)
            bottomRight = C(mx+1, my+1, x2, y2)

            # print "[{}, {}] - [{}, {}]. v {}, b {}".format(x1, y1, x2, y2, v, b)
            return Node(v, b, topLeft, bottomLeft, topRight , bottomRight)

        n = len(grid)
        return C(0, 0, n-1, n-1)
        # print all_same(1, 0, 1, 0)

sln = Solution()
# print sln.construct([[0]])
# print sln.construct([[0, 0], [1, 1]])
# print sln.construct([[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1]])
T = sln.construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])
print T.topLeft.val, T.topLeft.isLeaf
print T.topRight.val, T.topRight.isLeaf
print T.bottomLeft.val, T.bottomLeft.isLeaf
print T.bottomRight.val, T.bottomRight.isLeaf
