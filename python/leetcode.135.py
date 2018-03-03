class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        segs = [1]
        flag = [0]
        last_candy = [1] * length
        last_candy[0] = 1
        res = 0
        # 0 same
        # 1 inc
        # -1 dec
        for i in xrange(1, length):
            if ratings[i] > ratings[i-1]:
                # inc now
                if flag[-1] < 0:
                    segs.append(1)
                    flag.append(1)
                elif flag[-1] == 0:
                    segs.append(1)
                    flag.append(1)
                else:
                    segs[-1] += 1
            elif ratings[i] == ratings[i-1]:
                # same now
                if flag[-1] < 0:
                    segs.append(1)
                    flag.append(0)
                elif flag[-1] == 0:
                    segs[-1] += 1
                else:
                    segs.append(1)
                    flag.append(0)
            else:
                # dec now
                if flag[-1] < 0:
                    segs[-1] += 1
                elif flag[-1] == 0:
                    segs.append(1)
                    flag.append(-1)
                else:
                    segs.append(1)
                    flag.append(-1)
        ls = len(segs)
        # print segs
        # print flag
        for i in xrange(ls):
            if flag[i] == -1:
                if i > 0 and last_candy[i-1] <= segs[i]:
                    res -= last_candy[i-1]
                    last_candy[i-1] = segs[i] + 1
                    res += last_candy[i-1]
                res += ((1 + segs[i]) * segs[i] / 2)
                # print "DEC i=%d, res=%d, last_candy=%d, s=%d, segs[i]=%d" % (i, res, last_candy[i], s, segs[i])
            elif flag[i] == 0:
                last_candy[i] = 1
                res += max(0, segs[i])
                # print "SAME i=%d, res=%d, last_candy=%d" % (i, res, last_candy[i])
            else:
                # inc
                s = 1
                if i != 0:
                    s = last_candy[i-1] + 1
                last_candy[i] = s + segs[i] - 1
                res += ((s + last_candy[i]) * segs[i] / 2)
                # print "INC i=%d, res=%d, last_candy=%d, s=%d, segs[i]=%d" % (i, res, last_candy[i], s, segs[i])
        return res
sln = Solution()
# print sln.candy([2,2])
# print sln.candy([1,2,3,4,3,2,1])
# print sln.candy([1,2,2])
# print sln.candy([1,2,3,3,4,5,5,3,1])
# print sln.candy([5,5,3])
# print sln.candy([1,2,3,3,4,5])