class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """        
        self.sc = 0
        nn = (1 << n) - 1
        lowbit = lambda x: x & (-x)

        def solve(self, row, md, sd, line):
            # md is main diag, sd is second diag
            full = ((~row) == 0)
            if not full:
                choices = (~(row | md | sd)) & nn
                cid = 0
                while choices != 0:
                    current = lowbit(choices)
                    if ((row|current) & nn == nn):
                        self.sc += 1
                    solve(self, row|current, ((md|current)>>1), ((sd|current)<<1), line + 1)
                    choices -= current
                    cid += 1

            else:
                self.sc += 1
        
        solve(self, 0, 0, 0, 0)
        return self.sc

sln = Solution()
import sys
print sln.totalNQueens(4)
