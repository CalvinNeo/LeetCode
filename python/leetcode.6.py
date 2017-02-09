class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        elif numRows == 2:
            return s[0::2] + s[1::2]
        else:
            loop = numRows * 2 - 2
            ans = [""] * numRows
            for i in xrange(len(s)):
                p = 0
                if i % loop < numRows:
                    p = i % loop
                else:
                    p = numRows - ((i % loop - numRows) + 2)
                ans[p] += s[i]
            return ''.join(ans)
sln = Solution()
print sln.convert("PAYPALISHIRING", 3) 