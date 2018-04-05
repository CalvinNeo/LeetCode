import bisect
class Solution(object):
    def maxSumSubmatrix1(self, matrix, k, n, m):
        csum = [[0 for j in xrange(m)] for i in xrange(n)]
        for j in xrange(m):
            for i in xrange(n):
                if i == 0:
                    csum[i][j] = matrix[i][j]
                else:
                    csum[i][j] = matrix[i][j] + csum[i - 1][j]

        arr = [0] * (m + 1)
        max_ans = None
        for up in xrange(0, n):
            for down in xrange(up, n):
                for j in xrange(0, m):
                    if up == 0:
                        arr[j + 1] = arr[j] + csum[down][j]
                    else:
                        arr[j + 1] = arr[j] + (csum[down][j] - csum[up - 1][j])

                posi = []
                for i in xrange(1, m + 1):
                    # arr[j] must >= min_before, so arr[i] - arr[j] <= k
                    if arr[i] <= k:
                        max_ans = max(max_ans, arr[i])

                    min_before = arr[i] - k
                    j = bisect.bisect_left(posi, min_before)
                    if j < len(posi):
                        new_ans = arr[i] - posi[j]
                        # if arr == [0, 5, 1, -2, 2]:
                        #     print "find {} in {}, new_ans = {} - {} = {}".format(min_before, str(posi), arr[i], posi[j], new_ans) 
                        # print "new_ans", new_ans, up, down, i, j, arr, posi, arr[i], posi[j]
                        if new_ans <= k:
                            max_ans = new_ans if max_ans == None else max(max_ans, new_ans)
                        # bisect.insort(posi, new_ans)

                    # bisect.insort(posi, arr[i])
                    posi.append(arr[i])
                    posi.sort()
        return 0 if max_ans == None else max_ans

    def maxSumSubmatrix2(self, matrix, k, n, m):
        rsum = [[0 for j in xrange(m)] for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(m):
                if j == 0:
                    rsum[i][j] = matrix[i][j]
                else:
                    rsum[i][j] = matrix[i][j] + rsum[i][j - 1]

        arr = [0] * (n + 1)
        max_ans = None
        for left in xrange(0, m):
            for right in xrange(left, m):
                for j in xrange(0, n):
                    if left == 0:
                        arr[j + 1] = arr[j] + rsum[j][right]
                    else:
                        arr[j + 1] = arr[j] + (rsum[j][right] - rsum[j][left - 1])

                posi = []
                for i in xrange(1, n + 1):
                    # arr[j] must >= min_before, so arr[i] - arr[j] <= k
                    if arr[i] <= k:
                        max_ans = max(max_ans, arr[i])

                    min_before = arr[i] - k
                    j = bisect.bisect_left(posi, min_before)
                    
                    # if j < len(posi):
                    #     print posi
                    #     print "min_before {}, posi[j] {}, left {}, right {}, i {}".format(min_before, posi[j], left, right, i)
                    # else:
                    #     pass

                    if j < len(posi):
                        new_ans = arr[i] - posi[j]
                        if new_ans <= k:
                            max_ans = new_ans if max_ans == None else max(max_ans, new_ans)

                    # bisect.insort(posi, arr[i])
                    posi.append(arr[i])
                    posi.sort()
        return 0 if max_ans == None else max_ans

    def maxSumSubmatrix(self, matrix, k):
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0

        return self.maxSumSubmatrix2(matrix, k, n, m)
        if n > m:
            return self.maxSumSubmatrix2(matrix, k, n, m)
        else:
            return self.maxSumSubmatrix1(matrix, k, n, m)

sln = Solution()      
print sln.maxSumSubmatrix([[28,4,-19,18,-7,-10,27,19,1,16,0,10,-17,11,11,27,-1,10,12,-1],[-2,-19,17,4,25,-20,4,3,4,28,-10,7,16,-14,-3,-19,6,17,-4,-7],[2,8,18,-17,-2,10,-6,-5,11,10,22,-6,19,-16,6,-4,18,5,22,-17],[-14,-7,-20,13,-19,-20,-15,21,-11,-10,-8,-9,10,13,6,-10,15,9,-15,-2],[-18,26,12,8,2,16,-17,12,0,-5,9,-3,-12,-11,3,-6,-18,16,-7,-14],[5,29,25,22,11,-3,-2,-15,4,13,-17,-2,0,-2,20,10,-18,6,25,-20],[5,-7,8,5,15,22,8,-5,22,-18,-5,-14,23,2,-8,12,-16,-18,12,-12],[27,18,4,11,-3,12,-4,-8,-3,25,-9,24,-14,5,11,-9,-17,0,25,-15],[26,-7,18,4,4,18,-17,9,-19,-9,-19,-8,-4,-13,10,-11,6,-16,-12,12],[28,22,7,11,-6,13,8,22,7,-14,17,14,10,29,16,9,-3,18,-9,10],[27,19,-10,-9,1,3,14,1,7,3,-3,16,-2,9,14,-7,-19,-5,23,19],[-17,7,-20,8,-5,-6,-2,25,29,16,23,4,4,27,16,17,9,20,-6,22],[2,9,-13,1,-18,25,4,7,25,26,-4,8,-19,18,6,-7,-5,7,21,-8],[-2,11,1,29,6,-16,-8,3,7,11,10,-2,-1,-20,20,4,19,5,29,-7],[29,-12,-3,17,6,19,23,12,-19,13,19,5,27,22,-17,27,10,-12,12,23],[24,16,4,25,15,13,24,-19,1,-7,-19,13,-13,14,13,26,9,18,-9,-18],[-17,4,-18,-18,-19,3,-13,12,23,-17,-10,-20,14,2,18,21,-12,27,-3,4],[27,13,12,14,16,-9,-2,-15,-20,8,-2,24,18,15,26,21,27,17,-15,-3],[25,-8,17,-10,-16,13,26,-11,-15,6,-5,-13,23,2,24,-4,5,8,-15,-1],[15,-12,18,5,-3,7,5,11,-4,-13,28,20,0,-4,-13,-5,-13,-8,-16,3]], -123)
