import bisect
class STP:
    def __init__(self, x, y):
        self.fr = x
        self.to = y
        
    def __cmp__(self, other):
        return cmp(self.fr, other)

    def __getitem__(self, index):
        if index == 0:
            return self.fr
        else:
            return self.to

    def __str__(self):
        return "({}->{})".format(self.fr, self.to)

class Solution(object):
    def output(self, tps):
        ans = []
        for t in tps:
            if t[0] == t[1]:
                ans.append( "{}".format(t[0]) )
            else:
                ans.append( "{}->{}".format(t[0], t[1]) )
        return ans

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        data = []
        n = len(nums)

        for i in xrange(n):
            x = nums[i]
            index = bisect.bisect_left(data, x)
            # print "find {} at {} with is {}".format(x, index, str(data[index]))
            if index < len(data):
                # insert before index
                if data[index][0] - 1 == x:
                    data[index] = STP(x, data[index][1])
                if index - 1 >= 0 and data[index - 1][1] + 1 == x:
                    data[index - 1] = STP(data[index][0], x)
                if index - 1 >= 0 and data[index][0] == data[index - 1][1]:
                    # merge
                    # print "merge {} with {}".format(data[index - 1][0], data[index][1])
                    data[index] = STP(data[index - 1][0], data[index][1])
                    data.pop(index - 1)
            else:
                # the max
                # print "new {}".format(x)
                data.append(STP(x, x))
                if index - 1 >= 0 and data[index][0] == data[index - 1][1] + 1:
                    # merge
                    data[index] = STP(data[index - 1][0], data[index][1])
                    data.pop(index - 1)

        return self.output(data)

sln = Solution()
print sln.summaryRanges([0,1,2,4,5,7])
print sln.summaryRanges([0,2,3,4,6,8,9])

