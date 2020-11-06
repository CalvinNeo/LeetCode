class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        size = 0
        i = 0
        n = len(S)
        for i in xrange(n):
            x = S[i]
            if x.isalpha():
                size += 1
            else:
                size *= int(x)
            if K <= size:
                break

        for j in range(i, -1, -1):
            x = S[j]
            # print "j {} size {} K {} x {}".format(j, size, K, x)
            if x.isalpha():
                if K == size or K == 0:
                    return x
                size -= 1
            else:
                size /= int(x)
                # Important
                # not k %= int(x)
                # Now k > size
                K %= size

# sln = Solution()
# print sln.decodeAtIndex("leet2code3", 10) # o
# print sln.decodeAtIndex(S = "ha22", K = 5) # h
# print sln.decodeAtIndex(S = "a2345678999999999999999", K = 1) # a
# print sln.decodeAtIndex("vk6u5xhq9v", 554) # k