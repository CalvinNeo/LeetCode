class Solution(object):
    def myAtoi(self, ss):
        """
        :type str: str
        :rtype: int
        """
        def f_start(s):
            i = 0
            n = len(s)
            while i < n and s[i] == ' ':
                i += 1
            if i == n:
                return None
            elif s[i] in "+-0123456789":
                return i
            else:
                return None

        n = len(ss)
        i = f_start(ss)
        if i == None:
            return 0
        sn = 1
        if ss[i] == "-":
            sn = -1
            i += 1
        elif ss[i] == "+":
            i += 1
        j = i
        while j < n and ss[j] in "0123456789":
            j += 1
        if j == i:
            return 0
        t = sn * int(ss[i:j])
        if t < - 2 ** 31:
            return - 2 ** 31
        elif t > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return t

# sln = Solution()
# print sln.myAtoi("42")
# print sln.myAtoi("   -42")
# print sln.myAtoi("4193 with words")
# print sln.myAtoi("words and 987")
# print sln.myAtoi("-91283472332")
# print sln.myAtoi("-")