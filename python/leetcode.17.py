class Solution(object):
    def make_number(self, mm, s, l):
        if len(s) == 0:
            if len(l) != 0:
                self.ans.append(''.join(l))
            return
        i = int(s[0])
        l.append("")
        for ch in mm[i]:
            l[-1] = ch
            self.make_number(mm, s[1:], l)
        del l[-1]
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mm = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.ans = []
        self.make_number(mm, digits, [])
        return self.ans
sln = Solution()
print sln.letterCombinations("")
print sln.letterCombinations("0")
print sln.letterCombinations("23")