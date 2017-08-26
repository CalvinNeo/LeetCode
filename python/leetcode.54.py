class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m = len(matrix) 
        n = len(matrix[0]) 

        if n == 1:
            # special case for [[7],[9],[6]]
            ans = []
            for i in matrix:
                ans.append(i[0])
            return ans

        pulse = 0

        ans = matrix[0]
        x = 0
        y = n - 1
        while True:
            sg = 1 if (pulse % 4) in [0, 3] else -1
            delta = pulse / 2 + 1
            term = pulse % 2
            # print "(x, y) = (%d, %d), pulse = %d" % (x, y, pulse)
            if term == 0:
                # move m(x)
                if m - delta == 0:
                    break
                newx = x + (m - delta) * sg
                nr = []
                if newx > x:
                    for i in xrange(x + 1, newx + 1):
                        nr.append(matrix[i][y])
                else:
                    for i in xrange(x - 1, newx - 1, -1):
                        nr.append(matrix[i][y])
                ans.extend(nr)
                # print "pulse = %d, delta = %d, m - delta = %d, sg = %d, newx = %d, oldx = %d, y = %d" % (pulse, delta, m - delta, sg, newx, x, y)
                # print "nr", nr

                # ans.extend(matrix[fr:to+1][y])

                x = newx
            else:
                # move n(y)
                if n - delta == 0:
                    break
                newy = y + (n - delta) * sg
                nr = []
                if newy > y:
                    for i in xrange(y + 1, newy + 1):
                        nr.append(matrix[x][i])
                else:
                    for i in xrange(y - 1, newy - 1, -1):
                        nr.append(matrix[x][i])
                ans.extend(nr)
                # print "pulse = %d, delta = %d, n - delta = %d, sg = %d, newy = %d, oldy = %d, x = %d" % (pulse, delta, n - delta, sg, newy, y, x)
                # print "nr", nr
                y = newy
            pulse += 1
        return ans
sln = Solution()
arr = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

# print range(5, 1)
# print arr[1:2][0]
# print sln.spiralOrder([[7],[9],[6]])
print sln.spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]])

