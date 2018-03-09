class Solution(object):
    def print_case(self, s, leftc, rightc):
        if leftc > 0:
            self.print_case(s + "(", leftc - 1, rightc + 1)
        if rightc > 0:
            self.print_case(s + ")", leftc, rightc - 1)
        if leftc == 0 and rightc == 0:
            self.ans.append(s)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans = []
        self.print_case("", n, 0)
        return self.ans
sln = Solution()
print sln.generateParenthesis(3)
      