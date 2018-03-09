class Solution(object):
    def lastRemaining1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        c = -1
        step = 2
        nums = [False for i in xrange(n + 1)]
        l = 1
        r = n
        for i in xrange(n - 1):
            if n >= c + step >= 1:
                c += step
                nums[c] = True
            else:
                step *= -2
                if step < 0:
                    # from right to left now
                    c = r
                    while nums[c] == True:
                        c -= 1
                    r = c
                    nums[c] = True

                elif step > 0:
                    # from left to right now
                    c = l
                    while nums[c] == True:
                        c += 1
                    l = c
                    nums[c] = True

        for i in xrange(1, n + 1):
            if nums[i] == False:
                return i

    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        remain = n
        step = 2
        s = 1
        e = n
        while remain > 1:
            # print "s {}, e {}, step {}".format(s, e, step)
            delta = (e - s) / step + 1
            remain -= delta
            actual_e = (delta - 1) * step + s
            # print "delta {}, e {}, actual_e {}".format(delta, e, actual_e)
            if actual_e != e:
                news = actual_e + step / 2
            else:
                news = e - step / 2
            step = -step
            # k = (abs(s - e) - 1) / abs(step)
            k = (abs(s - news)) / abs(step)
            # print "k =", k
            newe = news + k * step
            step *= 2
            e, s = newe, news
            # print "remain {}, news {}, newe {}".format(remain, s, e)
            # print "================="
        return s

sln = Solution()
# 6 8 2 4 6 6 1 2 2
print sln.lastRemaining(12)
print sln.lastRemaining(10)
print sln.lastRemaining(5)
print sln.lastRemaining(6)
print sln.lastRemaining(8)
print sln.lastRemaining(9)
print sln.lastRemaining(1)
print sln.lastRemaining(2)
print sln.lastRemaining(3)

# for i in xrange(100):
#     # if sln.lastRemaining1(i) != sln.lastRemaining1(i + 1):
#     #     print i
#     print i, sln.lastRemaining1(i)

