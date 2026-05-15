class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        inf = 99999999
        top = []
        topv = -inf
        left = []
        leftv = inf
        right = []
        rightv = -inf
        bottom = []
        bottomv = inf

        for [blX, blY, trX, trY] in rectangles:
            if blX < leftv:
                leftv = blX
                left = [[blY, trY]]
            elif blX == leftv:
                left.append([blY, trY])

            if trX > rightv:
                rightv = trX
                right = [[blY, trY]]
            elif trX == rightv:
                right.append([blY, trY])

            if blY < bottomv:
                bottomv = blY
                bottom = [[blX, trX]]
            elif blY == bottomv:
                bottom.append([blX, trX])

            if trY > topv:
                topv = trY
                top = [[blX, trX]]
            elif trY == topv:
                top.append([blX, trX])
                
        # print "bottomv {} topv {} leftv {} rightv {}".format(bottomv, topv, leftv, rightv)
        # print "bottom {} top {} left {} right {}".format(bottom, top, left, right)

        area = (topv - bottomv) * (rightv - leftv)

        def validate(l, r, arr):
            arr.sort(cmp = lambda a, b: cmp(a[1], b[1]) if a[0] == b[0] else cmp(a[0], b[0]))
            n = len(arr)
            for i in xrange(n - 1):
                [a1, b1] = arr[i]
                [a2, b2] = arr[i + 1]
                if a1 <= a2 <= b1:
                    pass
                else:
                    # print "FALSE {} {}".format([a1, b1], [a2, b2])
                    return False
            ans = arr[0][0] == l and arr[-1][1] == r
            # print "ans {} {}".format(arr[0][0], arr[-1][1])
            return ans

        if not validate(leftv, rightv, top):
            return False
        if not validate(leftv, rightv, bottom):
            return False
        if not validate(bottomv, topv, left):
            return False
        if not validate(bottomv, topv, right):
            return False

        def h(x, y):
            return x * 100000 + y

        area = (topv - bottomv) * (rightv - leftv)
        a2 = 0
        for [a, b, c, d] in rectangles:
            a2 += (c - a) * (d - b)

        if area != a2:
            return False

        c = {}
        for [blX, blY, trX, trY] in rectangles:
            hh = h(blX, blY)
            if hh not in c:
                c[hh] = 1
            else:
                c[hh] += 1
            hh = h(blX, trY)
            if hh not in c:
                c[hh] = 1
            else:
                c[hh] += 1
            hh = h(trX, trY)
            if hh not in c:
                c[hh] = 1
            else:
                c[hh] += 1
            hh = h(trX, blY)
            if hh not in c:
                c[hh] = 1
            else:
                c[hh] += 1


        cn1 = 0
        for (k, v) in c.items():
            if v == 1:
                cn1 += 1
            else:
                if v % 2 == 1:
                    return False

        # print("cn1", cn1)
        # print("c", c)
        return cn1 == 4

    def isRectangleCoverWA(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        inf = 99999999
        top = []
        topv = -inf
        left = []
        leftv = inf
        right = []
        rightv = -inf
        bottom = []
        bottomv = inf

        for [blX, blY, trX, trY] in rectangles:
            if blX < leftv:
                leftv = blX
                left = [[blY, trY]]
            elif blX == leftv:
                left.append([blY, trY])

            if trX > rightv:
                rightv = trX
                right = [[blY, trY]]
            elif trX == rightv:
                right.append([blY, trY])

            if blY < bottomv:
                bottomv = blY
                bottom = [[blX, trX]]
            elif blY == bottomv:
                bottom.append([blX, trX])

            if trY > topv:
                topv = trY
                top = [[blX, trX]]
            elif trY == topv:
                top.append([blX, trX])

        print "bottomv {} topv {} leftv {} rightv {}".format(bottomv, topv, leftv, rightv)
        print "bottom {} top {} left {} right {}".format(bottom, top, left, right)

        area = (topv - bottomv) * (rightv - leftv)

        def validate(l, r, arr):
            arr.sort(cmp = lambda a, b: cmp(a[1], b[1]) if a[0] == b[0] else cmp(a[0], b[0]))
            n = len(arr)
            for i in xrange(n - 1):
                [a1, b1] = arr[i]
                [a2, b2] = arr[i + 1]
                if a1 <= a2 <= b1:
                    pass
                else:
                    # print "FALSE {} {}".format([a1, b1], [a2, b2])
                    return False
            ans = arr[0][0] == l and arr[-1][1] == r
            # print "ans {} {}".format(arr[0][0], arr[-1][1])
            return ans

        if not validate(leftv, rightv, top):
            return False
        if not validate(leftv, rightv, bottom):
            return False
        if not validate(bottomv, topv, left):
            return False
        if not validate(bottomv, topv, right):
            return False

        a2 = 0
        for [a, b, c, d] in rectangles:
            a2 += (c - a) * (d - b)

        return area == a2

    def isRectangleCoverTLE(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        inf = 99999999
        top = []
        topv = -inf
        left = []
        leftv = inf
        right = []
        rightv = -inf
        bottom = []
        bottomv = inf

        for [blX, blY, trX, trY] in rectangles:
            if blX < leftv:
                leftv = blX
                left = [[blY, trY]]
            elif blX == leftv:
                left.append([blY, trY])

            if trX > rightv:
                rightv = trX
                right = [[blY, trY]]
            elif trX == rightv:
                right.append([blY, trY])

            if blY < bottomv:
                bottomv = blY
                bottom = [[blX, trX]]
            elif blY == bottomv:
                bottom.append([blX, trX])

            if trY > topv:
                topv = trY
                top = [[blX, trX]]
            elif trY == topv:
                top.append([blX, trX])

        # print "bottomv {} topv {} leftv {} rightv {}".format(bottomv, topv, leftv, rightv)

        # if topv - bottomv != rightv - leftv:
        #     return False

        # print "bottom {} top {} left {} right {}".format(bottom, top, left, right)

        # top and bottom is exactly [leftv, rightv]
        # left and right is exactly [bottomv, topv]

        def validate(l, r, arr):
            arr.sort(cmp = lambda a, b: cmp(a[1], b[1]) if a[0] == b[0] else cmp(a[0], b[0]))
            n = len(arr)
            for i in xrange(n - 1):
                [a1, b1] = arr[i]
                [a2, b2] = arr[i + 1]
                if a1 <= a2 <= b1:
                    pass
                else:
                    # print "FALSE {} {}".format([a1, b1], [a2, b2])
                    return False
            ans = arr[0][0] == l and arr[-1][1] == r
            # print "ans {} {}".format(arr[0][0], arr[-1][1])
            return ans

        if not validate(leftv, rightv, top):
            return False
        if not validate(leftv, rightv, bottom):
            return False
        if not validate(bottomv, topv, left):
            return False
        if not validate(bottomv, topv, right):
            return False

        def point_in_rect(px, py, r):
            [blX, blY, trX, trY] = r
            if blX < px < trX and blY < py < trY:
                return True
            return False

        def rect_overlap(r1, r2):
            # [blX, blY, trX, trY] = r1
            # if point_in_rect(blX, blY, r2):
            #     # print "point_in_rect {} {} {}".format(blX, blY, r2)
            #     return True
            # if point_in_rect(blX, trY, r2):
            #     # print "point_in_rect {} {} {}".format(blX, trY, r2)
            #     return True
            # if point_in_rect(trX, blY, r2):
            #     # print "point_in_rect {} {} {}".format(trX, blY, r2)
            #     return True
            # if point_in_rect(trX, trY, r2):
            #     # print "point_in_rect {} {} {}".format(trX, trY, r2)
            #     return True
            # return False
            [r1left, r1bottom, r1right, r1top] = r1
            [r2left, r2bottom, r2right, r2top] = r2
            if r1left >= r2right:
                return False
            if r1top <= r2bottom:
                return False
            if r2left >= r1right:
                return False
            if r2top <= r1bottom:
                return False
            return True

        n = len(rectangles)
        for i in xrange(n):
            for j in xrange(n):
                if i != j and rect_overlap(rectangles[i], rectangles[j]):
                    # print "overlap {} {} {} {}".format(i, j, rectangles[i], rectangles[j])
                    return False

        return True


sln = Solution()
print sln.isRectangleCover([[0,0,3,3],[1,1,2,2],[1,1,2,2]]) # False
print sln.isRectangleCover([[0,0,1,1],[0,1,1,2],[0,2,1,3],[1,0,2,1],[1,0,2,1],[1,2,2,3],[2,0,3,1],[2,1,3,2],[2,2,3,3]]) # False
print sln.isRectangleCover([[0,0,4,1],[0,0,4,1]]) # False
print sln.isRectangleCover([[0,0,4,1],[7,0,8,2],[6,2,8,3],[5,1,6,3],[4,0,5,1],[6,0,7,2],[4,2,5,3],[2,1,4,3],[0,1,2,2],[0,2,2,3],[4,1,5,2],[5,0,6,1]]) # True
print sln.isRectangleCover([[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]) # False
print sln.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]) # True
print sln.isRectangleCover([[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]) # False