class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = map(int, str(n))
        m = len(s)
        i = m - 1
        import sys
        if n > 2147483647:
            return -1
        while i > 0:
            if s[i] > s[i - 1]:
                mi_index = None
                for j in xrange(m - 1, i - 1, -1):
                    if s[j] > s[i - 1]:
                        if mi_index == None:
                            mi_index = j
                        elif s[mi_index] > s[j]:
                            mi_index = j
                if mi_index == None:
                    return -1
                # print i, mi_index
                s[i - 1], s[mi_index] = s[mi_index], s[i - 1]
                # print s
                s[i:] = sorted(s[i:])
                ans = int(''.join(map(str, s)))
                if ans > 2147483647:
                    return -1
                return ans 
            i -= 1
        return -1
sln = Solution()
print sln.nextGreaterElement(12)
print sln.nextGreaterElement(21)
print sln.nextGreaterElement(12443322)
print sln.nextGreaterElement(199999)
print sln.nextGreaterElement(230241)
print sln.nextGreaterElement(1999999999)