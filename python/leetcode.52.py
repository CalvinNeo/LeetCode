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
                # print "==============="
                cid = 0
                while choices != 0:
                    # print "line %d, choices[%d] " % (line, cid)
                    current = lowbit(choices)
                    # print "++NEW line %d, choices[%d] %s, CHOOSE %s, act.row %s, row %s, md %s, sd %s" % (line, cid, bin(choices), bin(lowbit(choices)), row, bin((row|current) & nn), bin(((md|current)>>1) & nn), bin(((sd|current)<<1) & nn))
                    # print "DETAIL", bin((current<<1)), sd
                    if ((row|current) & nn == nn):
                        # print "((((((((((((((((((==="
                        self.sc += 1
                    solve(self, row|current, ((md|current)>>1), ((sd|current)<<1), line + 1)
                    choices -= current
                    cid += 1

                # print "row", bin((~row) & nn), row
            else:
                self.sc += 1
        
        solve(self, 0, 0, 0, 0)
        return self.sc

sln = Solution()
import sys
print sln.totalNQueens(4)
