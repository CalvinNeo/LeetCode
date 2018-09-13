#coding: utf8

def count_of_len(length):
    until = 10 ** length - 1
    begin = 10 ** (length - 1)

    cnt = until - begin + 1
    return cnt * length

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        x = n
        step = 1
        cur_len = 1
        while 1:
            cur_len = count_of_len(step)
            if x > cur_len:
                x -= cur_len
                step += 1
            else:
                break
        
        # print "step", step, "x", x
        interval = 10 ** (step - 1)
        # 我们在找第index位的数，0是最高位
        index = (x - 1) % step
        # 这是它的第occur次出现
        occur = (x - 1) / step
        # 这是+1的频率
        delta = 10 ** (step - index - 1)
        print "interval {} cur_len {} x {} index {} occur {} delta {}".format(interval, cur_len, x, index, occur, delta)
        begin = 0
        if index == 0:
            begin = 1
        return (occur / delta + begin) % 10

sln = Solution()
print sln.findNthDigit(1)
print sln.findNthDigit(2)
print sln.findNthDigit(9)
print sln.findNthDigit(10)
print sln.findNthDigit(11)
print sln.findNthDigit(12)
print sln.findNthDigit(13)
print sln.findNthDigit(14)
print sln.findNthDigit(15)
print sln.findNthDigit(10000) # 277(7)

# s = ""
# print "XXX", count_of_len(3) + count_of_len(2) + count_of_len(1)
# for i in xrange(1, 3000):
#     s += str(i)
# print s[2880:2910]